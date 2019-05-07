
``` python
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from mybbs import models
# Create your views here.
from django.core.exceptions import ValidationError
import json
from django.contrib import auth


def login(request):
    back_msg = {'user': None, 'msg': None}

    if request.is_ajax():
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        code = request.POST.get('code')

        if code.upper() == request.session['code'].upper():
            user = auth.authenticate(request, username=name, password=pwd)
            # user=models.UserInfo.objects.filter(username=ss,password=33).first()
            if user:
                # 在auth模块注册
                auth.login(request, user)
                back_msg['user'] = name
                back_msg['msg'] = '登录成功'
                # data=json.dumps(back_msg)
                return JsonResponse(back_msg)
            else:
                back_msg['msg'] = '用户名或密码错误'
                return JsonResponse(back_msg)
        else:
            back_msg['msg'] = '验证码错误'
            return JsonResponse(back_msg)

    return render(request, 'login.html')


def get_random_color():
    import random
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_code(request):
    import random
    # with open('static/img/lhf.jpg','rb') as f:
    #     data=f.read()
    # pip3 install pillow
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    import random
    img = Image.new("RGB", (270, 40), color=get_random_color())

    draw = ImageDraw.Draw(img)
    kumo_font = ImageFont.truetype("static/font/kumo.ttf", size=32)

    valid_code_str = ""
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(95, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        # x,y 的坐标   要写的字   字的颜色    字体
        draw.text((i * 50 + 20, 5), random_char, get_random_color(), font=kumo_font)

        # 保存验证码字符串
        valid_code_str += random_char

    print("valid_code_str", valid_code_str)
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()
    request.session['code'] = valid_code_str

    # with open(r'D:\lqz\BBS\lhf.jpg','rb') as f:
    #     data=f.read()
    return HttpResponse(data)


def index(request):
    articles_list = models.Article.objects.all()
    return render(request, 'index.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('/index/')


from django import forms
from django.forms import widgets


class RegForms(forms.Form):
    name = forms.CharField(max_length=20, min_length=2, label='用户名',
                           widget=widgets.TextInput(attrs={'class': 'form-control'}),
                           error_messages={'max_length': '太长了', 'min_length': '太短了'}
                           )
    pwd = forms.CharField(max_length=20, min_length=2, label='密码',
                          widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
                          error_messages={'max_length': '太长了', 'min_length': '太短了'}
                          )
    re_pwd = forms.CharField(max_length=20, min_length=2, label='确认密码',
                             widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
                             error_messages={'max_length': '太长了', 'min_length': '太短了'}
                             )
    email = forms.EmailField(label='邮箱',
                             widget=widgets.EmailInput(attrs={'class': 'form-control'}),
                             )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        user = models.UserInfo.objects.filter(username=name).first()
        if user:
            raise ValidationError('用户已经存在')
        else:
            return name

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')
        if pwd == re_pwd:
            return self.cleaned_data
        else:
            # __all__
            raise ValidationError('两次密码不一致')


def register(request):
    form_obj = RegForms()
    back_msg = {}
    if request.is_ajax():
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        re_pwd = request.POST.get('re_pwd')
        email = request.POST.get('email')
        myfile = request.FILES.get('myfile')
        print(myfile)
        print(re_pwd)
        form_obj = RegForms(request.POST)
        if form_obj.is_valid():
            # form_obj.cleaned_data
            # form_obj.errors
            if myfile:
                user = models.UserInfo.objects.create_user(username=name, password=pwd, email=email, avatar=myfile)
            else:
                user = models.UserInfo.objects.create_user(username=name, password=pwd, email=email)
            back_msg['user'] = name
            back_msg['msg'] = '注册成功'
        else:
            back_msg['msg'] = form_obj.errors
            print(form_obj.errors)
            print(type(form_obj.errors))
        return JsonResponse(back_msg)

    return render(request, 'register.html', {'form_obj': form_obj})


# def test(request,xx):
#     print(xx)
#     return HttpResponse('ok')
def homesite(request, username, **kwargs):
    print(kwargs)
    username=username
    user = models.UserInfo.objects.filter(username=username).first()
    if not user:
        return render(request, 'errors.html')
    blog = user.blog
    article_list = models.Article.objects.filter(user=user)
    if kwargs:
        condition=kwargs.get('condition')
        search=kwargs.get('search')
        if condition=='tag':
            article_list = models.Article.objects.filter(user=user).filter(tags__title=search)
        elif condition=='category':
            article_list = models.Article.objects.filter(user=user).filter(category__title=search)
        elif condition=='time':
            ll=search.split('-')
            article_list=models.Article.objects.filter(user=user).filter(create_time__year=ll[0],create_time__month=ll[1])
        else:
            return render(request, 'errors.html')

    # print(article_list)
    from django.db.models import Count
    # 查询每个标签下的文章数(分组查询)
    # 分组查询1 group by谁，用谁做基表
    #         2 filter在前，表示查询  ,filter在后，表示过滤，having
    #          3 values在前，表示group by  在后，取字段
    # 查询当前站点下每个标签下的文章数(分组查询)
    # tag_count = models.Tag.objects.filter(blog=blog).annotate(c=Count("article__title")).values_list('title', 'c')
    tag_count = models.Tag.objects.all().values('pk').filter(blog=blog).annotate(c=Count("article__title")).values_list('title', 'c')
    # 查询当前站点下每个分类下的文章数
    category_count = models.Category.objects.filter(blog=blog).annotate(c=Count('article__nid')).values_list('title',
                                                                                                             'c')
    from django.db.models.functions import TruncMonth
    # 查询当前站点每个月份下的文章数
    # time_count=models.Article.objects.annotate(y_m=TruncMonth('create_time'))
    # for i in time_count:
    #     print(i.title)
    #     print(i.y_m)
    time_count=models.Article.objects.filter(user=user).annotate(y_m=TruncMonth('create_time')).values('y_m').annotate(
        c=Count('y_m')).values_list('y_m', 'c')

    print(tag_count)
    print(category_count)
    print(time_count)

    # 统计每个出版社书籍个数
    # Publish.object.all().annotate(Count('book__title'))

    return render(request, 'homesite.html', locals())

from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def back_home(request):

    article_list=models.Article.objects.filter(user=request.user)

    return render(request,'back/back_home.html',locals())
from bs4 import BeautifulSoup
# 安装 pip3 install lxml
# pip3 install BeautifulSoup4
@login_required(login_url='/login/')
def addarticle(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        # content='<p>sddd</p><a>oooo</a><script>alert(123)</script>'
        #生成一个soup的对象，传两个参数，第一个是要解析的html，第二个是使用的解析器
        soup=BeautifulSoup(content,'html.parser')
        print(str(soup))
        # 拿到html内的文本内容
        desc=soup.text[0:150]+'...'
        # 查找html内所有的标签，放到一个列表里
        ll=soup.find_all()
        # print(ll)
        for tag in ll:
            print(tag.name)
            print(type(tag))
            # tag.name 标签的名称
            if tag.name=='script':
                # 从整个html文档里删掉当前标签
                tag.decompose()
        # print(ll)
        # aa=soup.find(name='script')
        # print(aa)
        # print(str(soup))

        models.Article.objects.create(title=title,content=str(soup),desc=desc,user=request.user)
        return redirect('/backhome/')

    return render(request,'back/article_add.html')


def article_detail(request,username,pk):
    # 正常情况下应该有一堆安全性校验
    #
    user=models.UserInfo.objects.filter(username=username).first()
    blog=user.blog
    article=models.Article.objects.filter(pk=pk).first()
    # 获取当前文章下所有评论
    comment_list=models.Comment.objects.filter(article_id=pk)

    from django.db.models import Count
    # 查询每个标签下的文章数(分组查询)
    # 分组查询1 group by谁，用谁做基表
    #         2 filter在前，表示查询  ,filter在后，表示过滤，having
    #          3 values在前，表示group by  在后，取字段
    # 查询当前站点下每个标签下的文章数(分组查询)
    # tag_count = models.Tag.objects.filter(blog=blog).annotate(c=Count("article__title")).values_list('title', 'c')
    tag_count = models.Tag.objects.all().values('pk').filter(blog=blog).annotate(c=Count("article__title")).values_list(
        'title', 'c')
    # 查询当前站点下每个分类下的文章数
    category_count = models.Category.objects.filter(blog=blog).annotate(c=Count('article__nid')).values_list('title',
                                                                                                             'c')
    from django.db.models.functions import TruncMonth
    # 查询当前站点每个月份下的文章数
    # time_count=models.Article.objects.annotate(y_m=TruncMonth('create_time'))
    # for i in time_count:
    #     print(i.title)
    #     print(i.y_m)
    time_count = models.Article.objects.filter(user=user).annotate(y_m=TruncMonth('create_time')).values(
        'y_m').annotate(
        c=Count('y_m')).values_list('y_m', 'c')

    return render(request,'article_detail.html',locals())

import json
from django.db.models import F
def diggit(request):
    back_msg={'status':None,'msg':None}
    if request.user.is_authenticated:
        #     先查询是否已经点过
        #    如果没有点过，去点赞表存数据
        #    去文章表修改点赞数据
        article_id=request.POST.get('article_id')
        # 注意：
        is_up=request.POST.get('is_up')
        print(type(is_up))
        is_up=json.loads(is_up)
        ret=models.ArticleUpDown.objects.filter(user=request.user,article_id=article_id)
        if not ret:
            models.ArticleUpDown.objects.create(user=request.user,article_id=article_id,is_up=is_up)
            if is_up:
                models.Article.objects.filter(pk=article_id).update(up_count=F('up_count')+1)
                back_msg['status']=1
                back_msg['msg'] = '点赞成功'
            else:
                models.Article.objects.filter(pk=article_id).update(down_count=F('down_count') + 1)
                back_msg['status'] = 1
                back_msg['msg'] = '点踩成功'
        else:
            back_msg['status'] = 0
            back_msg['msg'] = '您已经点过了'
    else:
        back_msg['status'] = 0
        back_msg['msg'] = '您没有登录'
    return JsonResponse(back_msg)

from django.db import transaction
def comment(request):
    back_msg={'status':False,'msg':None}
    if request.user.is_authenticated:
        #    评论表添加数据
        #    文章表，修改评论个数
        article_id=request.POST.get('article_id')
        comment=request.POST.get('comment')
        par_id=request.POST.get('par_id')
        # 事物
        with transaction.atomic():
            ret=models.Comment.objects.create(user=request.user,article_id=article_id,content=comment,parent_comment_id=par_id)
            models.Article.objects.filter(pk=article_id).update(comment_count=F('comment_count')+1)
            if par_id:
                back_msg['par_name']=ret.parent_comment.user.username
                back_msg['par_content']=ret.parent_comment.content
            back_msg['status']=True
            back_msg['user_name']=ret.user.username
            back_msg['time']=ret.create_time.strftime('%Y-%m-%d')
            back_msg['content']=ret.content
            back_msg['msg']='评论成功'
    else:
        back_msg['status'] = False
        back_msg['msg'] = '您没有登录'

    return JsonResponse(back_msg)


```








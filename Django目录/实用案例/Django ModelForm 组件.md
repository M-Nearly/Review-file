



- 自动生成HTML标签
- 表单验证



<https://blog.csdn.net/chuzhong1074/article/details/100828836>







### form 生成html  和 验证

```python
import random
from django import forms
from web import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from utils.tencent.sms import send_sms_single
from django_redis import get_redis_connection


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label="手机号",
                                   validators=[RegexValidator(r'{1[3|4|5|6|7|8|9]\d{9}$}', '手机号格式错误')], )
    password = forms.CharField(label="密码",
                               widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="重复密码", widget=forms.PasswordInput())
    code = forms.CharField(label="验证码",
                           widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ["username", "email", "password", "confirm_password", "mobile_phone", "code"]

    def __init__(self, *args, **kwargs):
        super(RegisterModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = "请输入{}".format(field.label)


class SendSmsForm(forms.Form):
    mobile_phone = forms.CharField(label="手机号", validators=[RegexValidator(r'1[3|4|5|6|7|8|9]\d{9}$', '手机号格式错误')],
                                   error_messages={
                                       "required": "不能为空"
                                   })

    def __init__(self, request, *args, **kwargs):
        super(SendSmsForm, self).__init__(*args, **kwargs)
        self.request = request

    def clean_mobile_phone(self):
        """
        手机号校验
        :return:
        """
        mobile_phone = self.cleaned_data["mobile_phone"]

        # 判断短息模板是否有问题
        tpl = self.request.GET.get("tpl")
        template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
        if not template_id:
            raise ValidationError("短信模板参数错误")

        # 校验数据库中是否已有手机号
        exits = models.UserInfo.objects.filter(mobile_phone=mobile_phone)
        if exits:
            raise ValidationError("手机号已存在")

        # 发短息
        code = random.randrange(1000, 9999)
        # sms = send_sms_single(mobile_phone, template_id, [code, ])
        # if sms['result'] != 0:
        #     raise ValidationError("短信发送失败,{}".format(sms['errormsg']))

        # 验证码写入redis (django-redis)
        conn = get_redis_connection()
        conn.set(mobile_phone, code, ex=60)

        return mobile_phone
```





### views

```python
from django.shortcuts import render, HttpResponse
from web.forms.account import RegisterModelForm, SendSmsForm
from django.http import JsonResponse


def register(request):
    form = RegisterModelForm()
    return render(request, "register.html", {"form": form})


def send_sms(request):
    print(request.GET.dict())
    form = SendSmsForm(request, data=request.GET)
    if form.is_valid():
        print(form.cleaned_data)
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})
```




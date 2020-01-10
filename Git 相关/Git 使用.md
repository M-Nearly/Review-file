
## 版本库创建 repository
1. 创建目录
2. cd 目录
3. git init 
创建一个空的仓库

## 把文件添加到版本库
1. 创建文件     			
	`vim xxx.txt`
2. git add 	把文件添加到仓库  
	`git add xxx.txt`
3. git commit , 把文件提交到仓库
	`git commit -m "描述信息"`
	

可以设置名字和邮件地址,来区分是谁提交的代码
​	`git config --global --edit`
``` shell
$ git add file1.txt
$ git add file2.txt file3.txt
$ git commit -m "add 3 files."
```



## 添加tag

``` shell
git tag # 查询当前所有tag
git tag -a v1.0 -m "对tag的描述信息"
git push origin --tags
```



# 代码回滚

## 代码修改并提交
1. 修改代码内容
2. git status 查看状态 (提示代码被修改,)
3. git diff xxx.txt   对比内容差异
4. git add .(代表当前目录所有文件)  / git commit -m "描述信息"
5. git status

## 代码回滚
1. git log 查看提交历史 (内容详细)
2. git log --pretty=oneline (只显示 commit id 版本号信息)
3. 在git中 使用HEAD表示当前版本, 上一个版本就是HEAD^，上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100。
	使用 `git reset` 命令
``` python
$ git reset --hard HEAD^
HEAD is now at be02137 update again
```
4. Git log 查看没有之前的版本,如果在想回去之前的版本,从上面的命令窗口找到 commit id
	`git reset hard commit id ` (不需要写全,前几位就可以,注意重复)
	就可指定回到版本
5. 如果找不到之前的commit id,Git提供了一个命令 git reflog 记录每一次命令
	`git reflog`  记录每一次命令
	


# 工作区 和 暂存区
##  工作区 Working Directory
	就是在电脑里能看到的目录,比如我们创建的文件夹就是一个工作区
##  版本库 Repository
	工作区内有一个隐藏目录 .git,这个不算工作区,而是Git的版本库
	Git的版本库存了很多东西,其中最重要的就是成为stage(或者index)的暂存区,还有Git为我们自动创建的第一个分支master,以及指向master的一个指针叫HEAD
	当git add的时候 ,会把代码add到暂存区
	当git commit 的时候,会把代码提交到分支


# 撤销修改
> 当我们代码修改错了,想撤回

## git checkout -- filename 可以丢弃工作区的修改 (只修改文件,但是还有git add)
	`git checkout -- filename` 文件修改了,但是还没有 git add .

## 文件修改了,并且git add .
	1. 用命令git reset HEAD file可以把暂存区的修改撤销掉（unstage），重新放回工作区  
	`git reset HEAD filename`
	2. git status 查看状态,暂存区是干净的,但是工作有修改
	` git checkout -- filename`丢弃工作区的修改 


命令git checkout -- readme.md意思就是，把readme.md文件在工作区的修改全部撤销，这里有两种情况：
- 一种是readme.md自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
- 一种是readme.md已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。
- 总之，就是让这个文件回到最近一次git commit或git add时的状态

**git checkout -- file** 命令中的--很重要，没有--，就变成了“切换到另一个分支”的命令，我们在后面的分支管理中会再次遇到git checkout命令。


# 删除操作 (在Git中删除操作)
1. 添加一个新文件到Git 并且提交,一般情况下,通常直接在文件管理器中把没用的文件删了,或者用rm命令删除
2. 这个时候,Git知道你删除了文件,因此,工作区和版本库就不一致了,`git status` 命令会立刻告诉你哪些文件被删除了
3. 现在你有两个选择,
	①. 一种情况是,确实要从版本库中删除
	​	那就用 `git rm` 删掉,并且 `git commit`,文件就从版本库中删除了
	②. 另一种情况是,删错了,因为版本里还有呢,所以可以很轻松的吧误删的文件恢复到最新版本
	​	`git checkout -- test.txt`
	​	git checkout 其实是用版本里的版本替换工作区的版本,无论工作区是修改还是删除,都可以'一键还原'

# 远程仓库

1. 创建SSH KEY. (在用户的主目录下,看看有没有.ssh目录.如果有看下有没有 id_rsa 和 id_rsa.pub两个文件,如果有直接跳过,或者创建SSH KEY
`ssh-keygen -t rsa -C "youremail@example.com"`
	id_rsa : 私钥,不要透露出去
	rsa.pub : 公钥,可以放心告诉其他人
2. 登录Github,打开"Account settings" -> "SSH Keys" -> 点击" Add SSH Key ",填写title,在Key文本框里粘贴id_rsa.pub文件的内容,add


## 创建远程连接仓库 (你已经在本地创建了一个Git仓库后，又想在GitHub创建一个Git仓库，并且让这两个仓库进行远程同步)
1. 在Github上创建仓库
2. 创建好仓库,三种方式
	①. 通过命令行在本地创建一个repo,并推到这个刚创建的远程仓库上来
	``` bash
        …or create a new repository on the command line
    echo "# document" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/M-Nearly/document.git
    git push -u origin master
   ```
    ②. 把你已有的本地仓库推到远程来
	``` bash
	…or push an existing repository from the command line
    git remote add origin https://github.com/M-Nearly/document.git
    git push -u origin master
   ```
	③. 
	``` bash
	…or import code from another repository
    You can initialize this repository with code from a Subversion, Mercurial, or TFS project.
   ```

----
``` bash
$ git remote add origin git@github.com:triaquae/oldboy_website.git ＃添加远程仓库
$ git push -u origin master #实际上是把当前分支master推送到远程。　　
```

连接好后,只要本地做了提交,就可以通过命令:
​	`git push origin master`


完整步骤
1. git add
2. git commit -m "描述信息"
3. git push origin master



## 从远程库克隆(先创建远程库，然后，从远程库克隆) https/ssh
1. 登录github,创建一个仓库,我们勾选Initialize this repository with a README，这样GitHub会自动为我们创建一个README.md文件。创建完毕后，可以看到README.md文件
2. 远程库已经准备好了，下一步是用命令`git clone`克隆一个本地库
3. 在本地找一个想存放这个远程仓库的目录,然后在本地命令行用 `git clone`来克隆这个远程仓库
`git clone git@github.com:M-Nearly/gitskills.git`


# 分支管理

## 创建与合并分支
1. 创建dev分支，然后切换到dev分支
`git checkout -b dev`
`git checkout` 命令加上-b参数表示创建并切换,相当于一下两条命令:
    ``` bash
    $ git branch dev
    $ git checkout dev
    Switched to branch 'dev'
    ```
然后,用`git branch` 命令查看当前分支
	``` bash
	$ git branch
    * dev
      master
   ```
`git branch` 命令会列出所有分支，当前分支前面会标一个*号。

然后,我们就可以在dev分支上正常提交,比如对readme.txt做个修改,加上一行文字

然后提交

现在,dev分支的工作完成,我们就可以切换回master分支:
​	``` bash
​	$ git checkout master
​    Switched to branch 'master'
​    ```
切换回master分支后,在查看一个readme.txt文件,刚才添加的内容不见了.
因为那个提交时在dev分支上,而master分支此刻的提交点并没有变.

现在我们把dev分支的工作成果合并到master分支上.
``` bash
$ git merge dev
Updating d17efd8..fec145a
Fast-forward
 readme.txt |    1 +
 1 file changed, 1 insertion(+)
```
`git merge` 命令用于合并指定分支到当前分支,合并后,在查看readme.txt的内容,就可以看到,和dev扥之的最新提交时完全一样的.
注意到上面的Fast-forward信息,git告诉我们,这次合并是"快进模式",也就是直接把master指向dev的当前提交,所以合并速度非常快.

合并完成后,就可以放心的删除dev分支了.
`$ git branch -d dev`
`Deleted branch dev (was fec145a).`

删除后,查看branch,就只剩下master分支了.
`git branch`

因为创建,合并和删除分支非常快,所以git鼓励你使用分支完成某个人物,合并后再删除掉分支,这和直接在master分支上工作效果是一样的,但过程更安全


## 解决冲突
当我们在不同分支上修改同一个文件,并提交后,这种情况下,git无法执行 "快速合并",只能试图把各自的修改合并起来,但这种合并和能会有冲突
`git merge feature1`
`git status`
查看冲突文件
Git用<<<<<<<，=======，>>>>>>>标记出不同分支的内容，我们修改如下后保存：
修改冲突内容在提交

可以用带参数 `git log` 也可以看到分支的合并情况

## 分支策略
首先master分支应该是非常稳定的,也就是仅用来发布新版本,
你和你的小伙伴们每个人都在dev分支上干活,每个人都有自己的分支,时不时的往dev分支上合并就可以了.


## Bug 分支
软件开发中,bug就像家常便饭一样,有了bug就要修复,在git中,由于分支是如此的的强大,所以,每个bug都可以通过一个新的临时分支来修复,修复后,合并分支,然后将临时分支删除.

当你接到一个修复一个代号101的bug的任务时,很自然地,你想创建一个分支issue-101来修复它,但是,当前正在dev上进行的工作还没有提交

并不是你想提交,而是工作只进行到一半,还没法提交,但是,必须在两个小时内修复该bug,怎么办?

幸好,Git还提供了一个stash功能,可以把当前工作 "储藏" 起来,等以后恢复现场后继续工作.

`git stash`

现在用git status 查看工作区,是干净的,因此可以放心的创建分支来修复bug

首先确定要在哪个分支上修复bug，假定需要在master分支上修复，就从master创建临时分支：

``` bahs
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 6 commits.
$ git checkout -b issue-101
Switched to a new branch 'issue-101'
```

现在修复bug，需要把“Git is free software ...”改为“Git is a free software ...”，然后提交：
``` bash
$ git add readme.txt
$ git commit -m "fix bug 101"
[issue-101 cc17032] fix bug 101
 1 file changed, 1 insertion(+), 1 deletion(-)
```
修复完成后，切换到master分支，并完成合并，最后删除issue-101分支：
``` bash
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 2 commits.
$ git merge --no-ff -m "merged bug fix 101" issue-101
Merge made by the 'recursive' strategy.
 readme.txt |    2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git branch -d issue-101
Deleted branch issue-101 (was cc17032).
```


太棒了，原计划两个小时的bug修复只花了5分钟！现在，是时候接着回到dev分支干活了！

``` bash
$ git checkout dev
Switched to branch 'dev'
$ git status
# On branch dev
nothing to commit (working directory clean)
```


工作区是干净的，刚才的工作现场存到哪去了？用git stash list命令看看：
``` bash
$ git stash list
stash@{0}: WIP on dev: 6224937 add merge
```
工作现场还在，Git把stash内容存在某个地方了，但是需要恢复一下，有两个办法：
一是用git stash apply恢复，但是恢复后，stash内容并不删除，你需要用git stash drop来删除；
另一种方式是用git stash pop，恢复的同时把stash内容也删了：

``` bash
$ git stash pop
# On branch dev
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#       new file:   hello.py
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#       modified:   readme.txt
#
Dropped refs/stash@{0} (f624f8e5f082f2df2bed8a4e09c12fd2943bdd40)
```

再用git stash list查看，就看不到任何stash内容了：
`git stash list`
你可以多次stash，恢复的时候，先用git stash list查看，然后恢复指定的stash，用命令：
` git stash apply stash@{0}`



# 多人协作
当你从远程仓库克隆时，实际上Git自动把本地的master分支和远程的master分支对应起来了，并且，远程仓库的默认名称是origin。

要查看远程库的信息,用`git remote`
``` bash
$ git remote
origin
```
或者,用git remote -v 显示更详细的信息
``` bash
$ git remote -v
origin  git@github.com:triaquae/gitskills.git (fetch)
origin  git@github.com:triaquae/gitskills.git (push)　
```
上面显示可以抓取和推送的origin的地址.若果没有推送权限,就看不到push的地址.


## 推送分支
推送分支，就是把该分支上的所有本地提交推送到远程库。推送时，要指定本地分支，这样，Git就会把该分支推送到远程库对应的远程分支上：
`git push origin master`
如果要推送其他分支，比如dev，就改成：
`git push origin dev`

但是，并不是一定要把本地分支往远程推送，那么，哪些分支需要推送，哪些不需要呢？

- master分支是主分支，因此要时刻与远程同步；
- dev分支是开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步；
- bug分支只用于在本地修复bug，就没必要推到远程了，除非老板要看看你每周到底修复了几个bug；
- feature分支是否推到远程，取决于你是否和你的小伙伴合作在上面开发。

总之，就是在Git中，分支完全可以在本地自己藏着玩，是否推送，视你的心情而定！

## 抓取分支
多人协作时，大家都会往master和dev分支上推送各自的修改。

现在，模拟一个你的小伙伴，可以在另一台电脑（注意要把SSH Key添加到GitHub）或者同一台电脑的另一个目录下克隆：
``` bash
$ git clone git@github.com:triaquae/gitskills.git
Cloning into 'gitskills'...
remote: Counting objects: 16, done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 16 (delta 0), reused 10 (delta 0), pack-reused 0
Receiving objects: 100% (16/16), done.
Checking connectivity... done.
```
当你的小伙伴从远程库clone时，默认情况下，你的小伙伴只能看到本地的master分支。不信可以用git branch命令看看：
``` bash
$ git branch
* master
```
现在，你的小伙伴要在dev分支上开发，就必须创建远程origin的dev分支到本地，于是他用这个命令创建本地dev分支：
` git checkout -b dev origin/dev`
现在，他就可以在dev上继续修改，然后，时不时地把dev分支push到远程：
``` bash
$ git add .
$ git commit -m "small updates"

[dev f1b762e] small updates
 2 files changed, 5 insertions(+), 1 deletion(-)
Alexs-MacBook-Pro:gitskills alex$ git push origin dev
Counting objects: 4, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 438 bytes | 0 bytes/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To git@github.com:triaquae/gitskills.git
   33ec6b4..f1b762e  dev -> dev
```

你的小伙伴已经向origin/dev分支推送了他的提交，而碰巧你也对同样的文件作了修改，并试图推送:
``` bash
$ git add .
$ git commit -m "add Dog class"
[dev 7e7b1bf] add Dog class
 2 files changed, 7 insertions(+)

$ git push origin dev
To git@github.com:triaquae/gitskills.git
 ! [rejected]        dev -> dev (fetch first)
error: failed to push some refs to 'git@github.com:triaquae/gitskills.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again. #提示你了，先把远程最新的拉下来再提交你的
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
推送失败，因为你的小伙伴的最新提交和你试图推送的提交有冲突，解决办法也很简单，Git已经提示我们，先用git pull把最新的提交从origin/dev抓下来，然后，在本地合并，解决冲突，再推
``` bash
$ git pull
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 4 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.
From github.com:triaquae/gitskills
   33ec6b4..f1b762e  dev        -> origin/dev
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> dev
```
git pull也失败了，原因是没有指定本地dev分支与远程origin/dev分支的链接，根据提示，设置dev和origin/dev的链接：
``` bash
$ git branch --set-upstream-to=origin/dev dev
Branch dev set up to track remote branch dev from origin.
```
再pull：
``` bash
$ git pull
Auto-merging hello.py
CONFLICT (content): Merge conflict in hello.py
Auto-merging branch_test.md
CONFLICT (content): Merge conflict in branch_test.md
Automatic merge failed; fix conflicts and then commit the result.
```
这回git pull成功，但是合并有冲突，需要手动解决，解决的方法和分支管理中的解决冲突完全一样。解决后，提交，再push：　　

``` bash
$ git add .
$ git commit -m "merge & fix hello.py"
[dev 93e28e3] merge & fix hello.py

$ git push origin dev

Counting objects: 8, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (7/7), done.
Writing objects: 100% (8/8), 819 bytes | 0 bytes/s, done.
Total 8 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To git@github.com:triaquae/gitskills.git
   f1b762e..93e28e3  dev -> dev
```

因此，多人协作的工作模式通常是这样：

1. 首先，可以试图用git push origin branch-name推送自己的修改；
2. 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并
3. 如果合并有冲突，则解决冲突，并在本地提交
4. 没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功！
5. 如果git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream branch-name origin/branch-name。

这就是多人协作的工作模式，一旦熟悉了，就非常简单。


# Github 使用
如何参与一个开源项目呢？比如人气极高的bootstrap项目，这是一个非常强大的CSS框架，你可以访问它的项目主页https://github.com/twbs/bootstrap，点“Fork”就在自己的账号下克隆了一个bootstrap仓库，然后，从自己的账号下clone：
git clone git@github.com:michaelliao/bootstrap.git
一定要从自己的账号下clone仓库，这样你才能推送修改。如果从bootstrap的作者的仓库地址git@github.com:twbs/bootstrap.git克隆，因为没有权限，你将不能推送修改。

Bootstrap的官方仓库twbs/bootstrap、你在GitHub上克隆的仓库my/bootstrap，以及你自己克隆到本地电脑的仓库，他们的关系就像下图显示的那样：
https://images2015.cnblogs.com/blog/720333/201610/720333-20161005123118145-703025311.png

如果你想修复bootstrap的一个bug，或者新增一个功能，立刻就可以开始干活，干完后，往自己的仓库推送。

如果你希望bootstrap的官方库能接受你的修改，你就可以在GitHub上发起一个pull request。当然，对方是否接受你的pull request就不一定了。


小结
- 在GitHub上，可以任意Fork开源仓库；
- 自己拥有Fork后的仓库的读写权限；
- 可以推送pull request给官方仓库来贡献代码。

# 忽略特殊文件.gitignore

有些时候，你必须把某些文件放到Git工作目录中，但又不能提交它们，比如保存了数据库密码的配置文件啦，等等，每次git status都会显示Untracked files ...，有强迫症的童鞋心里肯定不爽。

好在Git考虑到了大家的感受，这个问题解决起来也很简单，在Git工作区的根目录下创建一个特殊的.gitignore文件，然后把要忽略的文件名填进去，Git就会自动忽略这些文件。

不需要从头写.gitignore文件，GitHub已经为我们准备了各种配置文件，只需要组合一下就可以使用了。所有配置文件可以直接在线浏览：https://github.com/github/gitignore

忽略文件的原则是：
- 忽略操作系统自动生成的文件，比如缩略图等；
- 忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如Java编译产生的.class文件；
- 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。

举个例子：

假设你在Windows下进行Python开发，Windows会自动在有图片的目录下生成隐藏的缩略图文件，如果有自定义目录，目录下就会有Desktop.ini文件，因此你需要忽略Windows自动生成的垃圾文件：
```  bash
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini
```
然后，继续忽略Python编译产生的.pyc、.pyo、dist等文件或目录：
``` bash
# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build
```
加上你自己定义的文件，最终得到一个完整的.gitignore文件，内容如下：
``` bash
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini
 
# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build
 
# My configurations:
db.ini
deploy_key_rsa
```

最后一步就是把.gitignore也提交到Git，就完成了！当然检验.gitignore的标准是git status命令是不是说working directory clean。

使用Windows的童鞋注意了，如果你在资源管理器里新建一个.gitignore文件，它会非常弱智地提示你必须输入文件名，但是在文本编辑器里“保存”或者“另存为”就可以把文件保存为.gitignore了。

有些时候，你想添加一个文件到Git，但发现添加不了，原因是这个文件被.gitignore忽略了：
``` bash
$ git add App.class
The following paths are ignored by one of your .gitignore files:
App.class
Use -f if you really want to add them.
```
如果你确实想添加该文件，可以用-f强制添加到Git：
`git add -f App.class`
或者你发现，可能是.gitignore写得有问题，需要找出来到底哪个规则写错了，可以用git check-ignore命令检查：

``` bash
$ git check-ignore -v App.class
.gitignore:3:*.class    App.class　
```

Git会告诉我们，.gitignore的第3行规则忽略了该文件，于是我们就可以知道应该修订哪个规则。
小结
​	- 忽略某些文件时，需要编写.gitignore；
​	- .gitignore文件本身要放到版本库里，并且可以对.gitignore做版本管理！

# 修改远程仓库地址
方法有三种：
1.修改命令
git remote origin set-url [url]

2.先删后加
git remote rm origin
git remote add origin [url]

3.直接修改config文件

``` bash
usage: git remote [-v | --verbose]
   or: git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
   or: git remote rename <old> <new>
   or: git remote remove <name>
   or: git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
   or: git remote [-v | --verbose] show [-n] <name>
   or: git remote prune [-n | --dry-run] <name>
   or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
   or: git remote set-branches [--add] <name> <branch>...
   or: git remote get-url [--push] [--all] <name>
   or: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand

```


``` 
Administrator@MicroWin10-1554 MINGW64 /e/gitfiles (master)
$ git push origin master
To https://github.com/M-Nearly/Review-file.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/M-Nearly/Review-file.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Administrator@MicroWin10-1554 MINGW64 /e/gitfiles (master)
$ git pull -rebase origin master
error: Invalid value for --rebase: ebase
```
出现错误的主要原因是github中的README.md文件不在本地代码目录中

可以通过如下命令进行代码合并【注：pull=fetch+merge]

执行上面代码后可以看到本地代码库中多了README.md文件

此时再执行语句 git push -u origin master即可完成代码上传到github
git pull --rebase origin master

# git push时修改用户名密码

修改.git 的文件中的config文件

原文件

[remote "origin"]
​    url = http://xxxxx/start/start.git
​    fetch = +refs/heads/*:refs/remotes/origin/*

修改后：

[remote "origin"]
​    url = http://username:password@git.qoschain.io/start/start.git
​    fetch = +refs/heads/*:refs/remotes/origin/*
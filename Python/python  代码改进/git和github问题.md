### Git给GitHub上传和下载文件

> 操作载体：windows10

GitHub 在线上传文件

`git bash` 是 git 在 Windows 上为了方便使用所设置的一个 Unix 的环境. 如果你是 Windows 用户, 之后的教程你也能用这个来学习使用 git.

#### 第一种方法

GitHub在线上传文件夹

```python
点击upload files——>choose your files——>只能上传单个文件
```

---

#### 第二种方法

首次：通过git工具上传本地文件夹（本地项目）

```python
git add . # 将文件提交到暂缓区(.号可以用具体文件替代)
# 提交到版本库
git remote add origin https://github.com/VikenBrain/Machinelearning.git # GitHub地址
git pull --rebase origin master # 将文件合并（因为github上面有个readme文件）
git push -u origin master # 第一次推送
git push origin master # 以后的推送
```

第二次：

```python
git add . # 将文件提交到暂缓区(.号可以用具体文件替代)
git commit -m "the initial edition" 说明——版本管理   # 提交到版本库
git push origin master # 以后的推送
```



  为了更好地使用git，我们同事记录每一个施加修改的人

```python
git config -global user.name "viken"
git config -global user.email "viken@gmail.com"
```

在这个文件夹中建立git的管理文件

```python
git init # 将文件变成git可管理的仓库（初始化）
```

查看文件夹中的所有文件（包括隐藏文件）

```python
ls -a
```

查看版本库的状况

```python
git status
---------------------
# 输出
On branch master    # 在 master 分支
Initial commit
Untracked files:    
  (use "git add <file>..." to include in what will be committed)
	1.py        # 1.py 文件没有被加入版本库 (unstaged)
nothing added to commit but untracked files present (use "git add" to track)
```

提交改变（commit）

```python
git commit -m "the initial edition" 说明——版本管理
```

修改记录log

```python
git log
-----------------------
# 输出
commit 13be9a7bf70c040544c6242a494206f240aac03c
Author: Morvan Zhou <mz@email.com>
Date:   Tue Nov 29 00:06:47 2016 +1100
    create 1.py # 这是我们上节课记录的修改信息
    
    
```

回退版本：

```python
git reset --hard xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```




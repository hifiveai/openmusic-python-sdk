 ## pypi打包

- #### 项目文件

> 项目中需要加入README 、setup.py和LICENSE。其中setup.py必须存在文件中install_requires包含所需三方包

> 目前已经调整，不需要更改。

- #### 打包
> 1.准备工作，如果当前python没有安装twine 命令行下使用pip安装： `pip install twine`。
> 2.检查setup.py是否存在问题： `Python setup.py check`，出现`running check`代表正常。
> 3.直接使用python执行`python setup.py sdist bdist_wheel`。产生dist目录和2个文件，其中tar.gz 是源文件，.whl 分发文件。

- #### 配置pypi登录信息

- ###### MACOS、Ubuntu
> 1、在根目录中新建一个文件`vi ~/.pypirc`,输入以下内容：
> ```
> [distutils]
>index-servers =
>  pypi
>
>[pypi]
>username=HIFIVE
>password=hifive.ai123
> ```
> 2、设置权限。`chmod 600 ~/.pypirc`

- ###### WINDOWS
> 不使用提前配置的pypi配置文件而直接进行下一步，会在命令行中输入username和password。
> 

- #### 上传
> 1.直接使用 twine 将打包文件上传到pypi的仓库 `twine upload dist/*`。
> 2.如果提前配置了.pypirc不会提示登录信息否则需要输入登录名和密码：HIFIVE   hifive.ai123
> 3.没有报错就上传成功
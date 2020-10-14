# 安装Python  
## 下载Python.exe文件
1. [Python官网](https://www.python.org)
从[Python Download](https://www.python.org/downloads/)找到release版本（这里选择3.9.0）
<img src="../../blob/main/Images/BuildEnvPython/1.png" width="75%">  
2. 点击Download到下载页面
<img src="../../blob/main/Images/BuildEnvPython/2.png" width="75%">  
3. 选择Windows x86-64 executable installer下载
## 安装Python
1. 使用管理员模式运行安装Python  
<img src="../../blob/main/Images/BuildEnvPython/3.png" width="75%">
2. 勾选Add Python XX to PATH 
<img src="../../blob/main/Images/BuildEnvPython/4.png" width="75%">
3. 选择Customize installation
<img src="../../blob/main/Images/BuildEnvPython/5.png" width="75%">
4. 保持选线，选择下一步
<img src="../../blob/main/Images/BuildEnvPython/6.png" width="75%">
5. 更改安装路径,这里我选择了D:\PY39
<img src="../../blob/main/Images/BuildEnvPython/7.png" width="75%">
<img src="../../blob/main/Images/BuildEnvPython/8.png" width="75%">
6. 安装完成
<img src="../../blob/main/Images/BuildEnvPython/9.png" width="75%">
<img src="../../blob/main/Images/BuildEnvPython/12.png" width="75%">
7. 测试安装是否成功,打开Command Prompt,输入py --version,显示python版本表示安装成功  
<img src="../../blob/main/Images/BuildEnvPython/10.png" width="75%">
8. 设置环境变量
- 我的电脑->属性  
<img src="../../blob/main/Images/BuildEnvPython/11.png" width="75%">
- 点击高级系统设置
<img src="../../blob/main/Images/BuildEnvPython/13.png" width="75%">
- 点击环境变量,在系统变量中找到Path，选择编辑
<img src="../../blob/main/Images/BuildEnvPython/14.png" width="75%">
<img src="../../blob/main/Images/BuildEnvPython/15.png" width="75%">
- 找到将Python的安装路径和PIP路径
PIP是Python的包管理工具,稍后会介绍如何使用
<img src="../../blob/main/Images/BuildEnvPython/16.png" width="75%">
<img src="../../blob/main/Images/BuildEnvPython/17.png" width="75%">
添加路径到Path变量中,当前的例子中为;D:\PY39;D:\PY39\Scripts
<img src="../../blob/main/Images/BuildEnvPython/18.png" width="75%">
9. 验证Python和PIP环境变量是否成功
打开Command Prompt,输入python,如果看到python信息,表示环境变量生效
<img src="../../blob/main/Images/BuildEnvPython/19.png" width="75%">
输入pip,看到如下信息，表示环境变量生效
<img src="../../blob/main/Images/BuildEnvPython/20.png" width="75%">
到现在为止,python已经安装成功，并且可以正常使用了
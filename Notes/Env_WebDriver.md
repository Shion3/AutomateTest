# 安装配置WebDriver
WebDriver是一个中间件，开发人员通过API调用WebDriver，WebDriver根据API调用浏览器，实现自动化测试。通过访问[Driver Requirments](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#quick-reference)找到对应版本的WebDriver  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/1.png" width="50%">  
WebDriver的版本需要和浏览器的版本一致，首先查找自己浏览器的版本，通过截图的方式，选择About Google Chrome  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/3.png" width="50%">  
当前的Chrome版本为86.0.4240.75
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/4.png" width="50%">   
访问对应Chrome的Downloads链接,可以看到很多版本,我们选择86.0.4240.22,保持大版本一致就可以
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/2.png" width="50%">  
点击下载86.0.4240.22  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/5.png" width="50%">  
解压文件夹  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/6.png" width="50%">  
创建WedDriver文件夹,将chromedriver.exe移动到WebDriver  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/7.png" width="50%">  
将WebDriver添加到环境变量  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/8.png" width="50%">  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/9.png" width="50%">  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/10.png" width="50%">  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/11.png" width="50%">  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/12.png" width="50%">  
打开Command Prompt,输入chromedriver.exe,如果看到如下信息,表示环境变量生效  
<img src="https://github.com/Alex-Ji/AutomateTest/raw/main/Notes/Images/Env_WebDriver/13.png" width="50%">  

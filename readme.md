# 上传和展示pdf

标签： python


----------
郭柱明


----------
## demo ##

[查看地址][1]


[pdf版本readme地址][2]

----------
## 前言 ##
这个是开学前跟别人赌气写下的一个很小的web app，功能是上传pdf文件，然后获得这个文件在线浏览的url，需求很简单。之前为了方便只是把上传到服务器的文件存在flask static文件夹下，会有不便于管理等等问题。这个周末做了如下改进：使用mysql进行存储文件，进行模块的细化。
<p align="right">郭柱明 2018/3/25</p>


----------
## 可行性分析 ##

> 从需求上而言，这个web app仅仅有上传，展示两个功能。
我一个人可以进行开发，但是在人力物力上已经绰绰有余。
在app的服务器部署上，我有一个digital ocean vps可以用来部署，所以部署上也没有太大问题。


----------
## 需求分析 ##


 1. 上传pdf文件
 2. 获得在线浏览此pdf文件的url
 3. 打开这个url可以进行文件的预览
 


----------
## 设计 ##

###大概设计###

![struction.png-12.1kB][3]


整个结构呈现cs结构，server我使用nginx，server使用wsgi接口调用flask app

###详细设计###

 - 包-pdf(整个web app打包为一个包)
  - db.py模块(定义一个包含数据库链接的类以及初始化数据库的函数)
  - f.py模块(定义File类)


----------
## 编码 ##

> 编码情况详细见[github][4]


----------
## 测试与运行 ##
![pdf.gif-631.7kB][5]


----------
## 部署 ##

> 部署有个问题：无法从事先设置的环境变量中加载出mysql的账号和密码，在服务器上调试没问题，但是一旦部署上去就会在这部分出问题，无奈下只能在代码使用mysql的账号密码，有一定的安全风险。



  

   


  [1]: http://138.68.235.123/upload
  [2]: http://138.68.235.123/show?file_name=readme.pdf
  [3]: http://static.zybuluo.com/gzm1997/5de0ll4jozkxxzntxo20ni2x/struction.png
  [4]: https://github.com/gzm1997/pdf
  [5]: http://static.zybuluo.com/gzm1997/v93gqdz11aenv30kisr64r41/pdf.gif
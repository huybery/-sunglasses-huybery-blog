# huybery-blog
>## About Blog
#### 技术栈
前端： bootstrap+flatui 
后端 : flask
数据库 : sqlite 使用 SQLAlchemy 管理
服务器 ： Nignx + WSGI + Supervisor 
#### 为什么要写这个blog?

还记得踏入这一行业最初的目标就是在www上有一个属于自己的blog...

第一版blog折腾了wordpress，接触了前端，接触了SAE，接触了以后绝对不会写的PHP（别问窝为什么..

第二版使用了hexo静态blog 然后托管到了github pages，折腾了一下午终于部署完以后就再也没有更新过blog（失败2333

第三版我决定自己写一个 一是练一练后端 二是折腾一下服务器

>## Development Log

#### 后端：

:neckbeard: welcome fork or start (2016.3.16

:muscle: 构建基本路由，使用bootstrap来保护眼睛 （2016.3.17

:bear: 开发进度有点慢，sad (2016.3.18

:relieved: 构建基本结构，配置选项，使用蓝本 （2016.3.20

:yum: 增加了登陆功能 （2016.3.22

:alien: 增加了文章发布(后端Markdown渲染)，单文章页路由 （2016.3.23

:running: 增加了文章列表分页功能,增加了文章修改功能（管理员权限），使用Migrate数据库迁移（2016.3.24

 :sunglasses: 增加标签系统 一对多数据库建立 后端总算写的差不多了~ （2016.3.25

#### 前端：
:sunglasses:（2016.3.25
 - 增加下滑隐藏nav和上滑显示，页面简单美化
 - 增加header image，底部pagination位置优化
 - 增加页面进程顶部显示

:smirk_cat: (2016.3.26
 - 增加返回顶部按钮,下滑才显示
 - 美化滚动条

:point_up_2:(2016.3.27
 - 美化post显示
 - 更换了字体
 - 4个小时解决了重大bug！！有关flask-pagedown渲染问题(心酸脸
 - 集成highlight.js

:smile_cat:(2016.3.28
 - 增加底部footer
 - 修改了Post和tags顶部图片
 - 增加了多说
 - 修改了多说css 增加圆角头像 旋转
 - 修复多说气泡bug

:trollface:(2016.3.29
 - 增加github star显示

#### 优化：

:racehorse:（2016.3.26
 - post图片使用[七牛](http://www.qiniu.com/)
 - 使用[bootcdn](http://www.bootcdn.cn/)加速静态文件库

#### 部署：
 :speak_no_evil:（2016.3.29
 - 准备开始部署！
 - 配置阿里云,ubuntu 14.04
 - 配置虚拟环境venv

:trollface: ( 2016.3.29
 - 配置uswgi

:scream_cat:( 2016.3.30
 - 折腾一早上vsftpd

:alien:(2016.3.31
  - 被破服务器整的心力憔悴呜呜
  - 成功部署,感谢[@Responsible](https://github.com/responsible)的帮助

:hear_no_evil: （2016.4.1
  - 解决移动端适应bug
  - 绑定域名 [huybery.me](huybery.me)

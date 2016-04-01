# React学习笔记（一）
> 最近想学习一下`React` （主要是啃一下文档和写点见解）
  如果你觉得我写的还不错
  [star](https://github.com/huybery/huybery-blog)或者[follow](https://github.com/huybery)我一下
  就是对我最大的支持 (ง •̀_•́)ง

## 开始

### [JSFiddle](https://jsfiddle.net/reactjs/69z2wepo/)

个人觉得这个东东没什么用..就是个在线环境 让你输出`hello world`爽一爽

### 获得React
- 官方推荐使用 遵循CommonJS规范的 ‘模块系统’ 类似于`browserify` 或者 `webpack`.这种方式直接使用`npm`包就ok.
- 还有一种方式就是直接下载官方提供的[教程包](http://reactjs.cn/react/downloads/react-0.13.0.zip)

### 正式开始
我们在根目录下创建一个`helloworld.html`的文件
内容如下：

    <!DOCTYPE html>
    <html>
     <head>
      <meta charset="UTF-8" />
      <title>Hello React!</title>
      <script src="build/react.js"></script>
      <script src="build/react-dom.js"></script>
      <script
      src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.23/browser.min.js"></script>
    </head>
    <body>
      <div id="example"></div>
      <script type="text/babel">
      ReactDOM.render(
      <h1>Hello, world!</h1>,
      document.getElementById('example')
      );
      </script>
    </body>
    </html>

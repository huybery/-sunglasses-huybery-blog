# 1.JavaScript 简介
## JavaScript简史
  Netscape：JavaScript

  Internet Explorer:JSscript

  ECMA:ECMAScript
## JavaScript的实现
- 核心（ECMAScript）
- 文档对象模型（DOM）
- 浏览器对象模型（BOM）

## 文档对象模型（DOM）

> Document Object Model:是针对XML但经过扩展用于HTML的应用程序编程接口。

- 为什么要使用DOM：通过DOM创建表示文档的树形图，开发人员获得了控制页面内容和结构的主动权，通过DOM提供的API，开发人员可以轻松自如地删除，添加，替换或修改任何节点
- 其他DOM标准：
    - SVG
    - MathML
    - SMIL

## 浏览器对象模型（BOM）
支持可以访问和操作浏览器窗口的浏览器对象模型（Browser Object Model）

# 2.在HTML中使用JavaScript

## script元素

定义了下列六个属性

- `async` 表示应该立即下载脚本，但不妨碍页面中的其他操作，比如下载其他资源或等待加载其他脚本
- `charset` 指定的代码的字符集
- `defer` 表示脚本可以延迟到文档完全被解析和显示之后再执行
- `language` 已经废弃
- `src` 表示包含要执行代码的外部文件
- `type` 表示编写代码使用的脚本语言的内容类型

### 使用的方式有两种
- 使用`<script>`元素嵌入，指定type属性
- 外部引用`<script type='text/javascript' src='example.js'></script>`
  - 不用在`<script></script>`中再嵌入代码，如果嵌入代码智慧下载并执行外部脚本文件，嵌入的代码会被忽略

### 标签的位置
- 放在`<head></head>`中：必须等到全部JavaScript代码都被解析和执行完成以后才能开始呈现页面的内容，这无疑会导致浏览器在呈现页面时出现明显的延迟 而延迟间的浏览器窗口中将是一片空白。
- 放在`<body>`的后面：在解析包含的javascript代码之前，页面的内容完全呈现在浏览器中，用户会因为浏览器窗口显示空白页面的时间缩短而感到打开的页面的速度加快了

## 将代码放入外部文件的优点:

- 可维护性：能够在不触及HTML标记的情况下集中精力编辑`javascript`代码
- 可缓存： 浏览器能够根据具体的设置缓存链接的所有外部文件，最终结果是加快页面加载的速度
- 适应未来：无须考虑蹩脚的XHTML或注释hack

## 文档模式

- 混杂模式
- 标准模式
- 准标准模式

在Html5中，对于文档类型已经统一，直接写法是`<!DOCTYPE html>`即可。

## `<noscript>`元素

支持JavaScript的平稳退化

    <noscript>
      <p>本页面需要浏览器支持javascript</p>
    </noscript>

# 3.基本概念

## 语法
### 区分大小写
变量`huybery`和`Huybery`是两个不同的变量
### 标识符

> 所谓标识符 就是指变量、函数、属性的名字，或者函数的参数。标识符可以按照下列格式规则组合起来的一或多个字符

- 第一个字符必须是字符，下划线_,或者一个美元字符（$）
- 其他字符可以是字母、下划线、美元符号或者数字

标识符中的字符也可以是扩展的ASCII或Unicode字母字符，但我们不推荐那样做

> 我们的标识符最好采用驼峰式大小写格式，也就是第一个字母小写，剩下的每个单词的首字母大写，例如`firstScend`,`myCar`,`doSomethingImportant`

### 注释

ECMAScript 使用C风格的注释，包括单行注释和块级注释。
- 单行注释以两个斜杠开头
`//单行注释`
- 块级注释以一个斜杠和一个星号开头
`/* hahaha`

### 严格模式
ECMAScript5引入`“use strict”`

### 语句

以一个分号结尾；如果省略分号，则由解析器确定语句的结尾

## 保留字和关键字
- 关键字：具有特殊用途
- 保留字：有可能在将来被用作关键字

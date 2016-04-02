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

#

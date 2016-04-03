> 这是什么?
  最近想恶补一下关于javascript的基础知识
  权当一个记录笔记
  反正也不会有人看..

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

## 变量
ECMAScript 的变量是松散类型的，所谓的松散类型就是可以用来保存任何类型的数据。定义变量时要用`var`操作符，后跟一个变量名。支持变量初始化。

    var name = "huybery";

## 数据类型
ECMAScript有5种简单数据类型

- Undefined
- Null
- Boolean
- Number
- String

还有1种复杂数据类型

- Object(本质上由一组无序的名值对组成)

### `typeof`操作符
一种手段来检测给定变量的数据类型，可返回的值如下

- `"undefined"` 这个值未定义
- `"Boolean"` 如果这个值是布尔值
- `"string"` 如果这个值是字符串
- `"number"` 如果这个值是数值
- `"object"` 如果这个值是对象或者null
- `"function"` 如果这个值是函数

> 特殊值`null`会被认为是一个空的对象，所以调用`typeof`操作符的时候会返回`object`

### Undefined 类型
未初始化的变量默认为`undefined`

    var message;
    alert(message == undefined); //true

奇怪的东东：
- 对于尚未声明的变量只能执行一项操作：使用`typeof`操作符检测其数据类型。
- 对于未声明的变量返回的值也是`undefined`

### Null 类型

null表示一个空对象指针，所以`typeof`返回的也是一个对象`object`.

undefined 值是派生自`null`的值，因此规定对他们的相等性测试要返回`true`。

### Boolean 类型
这个类型只有两个字面值`true`和`false`

可以对任何类型的值掉用`Boolean()`，而且总返回一个Boolean值，对于返回的是`true`还是`false`，要取决于转换值的数据类型及其实际值

### Number 类型
可以使用10，8，16 进制，在进行算数运算的时候，所有的8，16都将会转换为10进制。

- 浮点数值
 - 不失时机的转换为整数
 - 对于极大极小的数值，可以用e表示法，等于e前面的数值乘以10的指数此幂
 - 浮点数计算会有误差
- 数值范围
 - `Number.MAX_VALUE`
 - `Number.MIN_VALUE`
 - `Infinity`
- NaN：这个数值表示一个本来要返回数值的操作数未返回数值的情况
 - 任何设计NaN的操作都将返回NaN
 - NaN与任何值都不相等（包括NaN）
 - 针对这两个特点 定义了`isNaN()`函数，在接受到一个值后，会尝试将这个值转换为数值，而任何不能被转换为数值的值都会导致这个函数返回true.
- 数值转换
 - Number()
 - parseInt()
 - parseFloat()

### String 类型
用于表示由0或多个16位Unicode字符组成的字符序列

- 字符变量：包含一些特殊的字符字面量 也叫转义序列。任何字符串的长度都可以通过访问其`length`属性取得。
- 字符串的特点：ECMAScript的字符串是不可变的
- 转换为字符串：
  - `num.toString()` ; 可以添加一个参数为输出数值的基数，例如`num.toString(8)`
  - `String(num)`;如果不知道要转换的值是不是null或undefined的情况下，如果有`toString()`方法则调用，否则返回其本身
- 要把某个值转换为字符串，可以使用加法操作符与字符串`""`加在一起

### Object类型
对象其实就是一组数据和功能的集合，两种创建方式：

- `var o = new Object()`
- `new o = new Object`

## 操作符
包括算数操作符，位操作符，关系操作符和相等操作符

### 一元操作符
只能操作一个值的操作符叫做一元操作符

- 递增和递减操作符
- 一元加和减操作符


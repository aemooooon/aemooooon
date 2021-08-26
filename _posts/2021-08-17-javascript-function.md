---
layout: post
subtitle: 函数
categories: [JavaScript]
header:
  image: header.jpg
  align:
  text: light
---

今天去欣辰教育咨询公司面试，去了前台小姐姐就给了一张面试题（共四页，每页 3 道题），让我 30 分钟做完，还有一张非常详细的个人信息表需要填写。在做的过程中有熟悉的，也有不会的，所以特地回忆一下，做个记录，毕竟 **ES2015** 我确实基础薄弱。

## `let & var`

第一道题写了 2 个 `for` loop，其实就是考察 `var` 和 `let` 作用域的问题，这个之前一个 Google 的前端小姐姐已经在面试题里分享过了。

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 3000);
}

for (let i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 3000);
}
```

## `Function`

第二道题用到了函数的 prototype、apply、call、arguments 等实例方法和属性，这个确实是我不太了解的。虽然题目可能答对了，但也是蒙的。行了，看看 MDN 吧！

### `arguments` properties

> arguments 就是一个对象，函数的参数。

```javascript
function f1(a, b, c) {
  console.log(arguments[0]);
  console.log(arguments[1]);
  console.log(arguments[2]);

  console.log(typeof arguments); // object

  console.log("LENGTH properties", arguments.length);

  // 3 ways that cast object to array
  console.log(Array.prototype.slice.call(arguments));
  console.log(Array.from(arguments));
  console.log([...arguments]);
}

f1("d", "3", "f");

// d
// 3
// f
// LENGTH properties 3
// (3) ["d", "3", "f"]
// (3) ["d", "3", "f"]
// (3) ["d", "3", "f"]
```

### `Function.prototype.bind()` 实例方法

> bind() 方法创建一个新的函数，在 bind() 被调用时，这个新函数的 this 被指定为 bind() 的第一个参数，而其余参数将作为新函数的参数，供调用时使用。

```javascript
const a = {
  x: 100,
  printX: function () {
    return this.x;
  },
};

// 直接把函数委托给变量将无法访问 a 内的 this
const b = a.printX;
console.log(b()); // undefined

// bind 之后
const c = b.bind(a);
console.log(c()); // 100
```

bind() 函数会创建一个新的绑定函数（bound function，BF）。绑定函数是一个 exotic function object（怪异函数对象，ECMAScript 2015 中的术语），它包装了原函数对象。调用绑定函数通常会导致执行包装函数。

```javascript
function foo() {
    console.log( this.name);
}

var obj = {
    name: 'hua'
};

foo.call(obj); // => hua
foo.apply(obj); // => hua

var tmp = foo.bind(obj)
tmp() // => hua



<button id='btn1' onclick="clickHandler()">click me! btn1</button>
<button id='btn2' onclick="clickHandler()">click me! btn2</button>
<script>
function clickHandler() {
	console.log(this, this.id)
}
</script>

<button id='btn1' onclick="clickHandler.bind(this)()">click me! btn1</button>
<button id='btn1' onclick="clickHandler.call(this)">click me! btn1</button>
<button id='btn1' onclick="clickHandler.apply(this)">click me! btn1</button>

// ref：https://juejin.cn/post/6983503349182119966

```

## 面试问题

- CSS 的优先级问题
- CSS 伪类选择器
- CSS3 有什么新的特性
- ES6 的新特性有哪些
- get 和 post 的区别
- vue 的路由有几种
- vue 的生命周期
- vue 的组件之间如何通信
- 谈谈事件捕获和冒泡
- 谈谈 js 的事件循环机制
- 谈谈 js 的原型链
- 谈谈 js 中的继承机制
- 谈谈你对 react fiber 的了解
- 谈谈 redux
- 用手写一个防抖函数
- 给一个数组，在不改变原数组的情况下，返回不重复的值
- 给一个字符串，写一个算法找出出现最多的那个字母，并统计出现的次数
- 手写 HTML5 的视频和音频标签
- 描述一下 apply call 和 bind
- 哪些 CSS 属性不受盒子模型的影响
- 描述一下 px em rem 的区别


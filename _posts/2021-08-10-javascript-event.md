---
layout: post
subtitle: flow capture bubble
categories: [JavaScript]
header:
  image: header.jpg
  align:
  text: light
---

I've took a job interview this morning with Yunxi co.,ltd. The interviewer asked a couple of front end question, and the most impressive one is about that what is JavaScript DOM event flow and how does event capture/bubble works? I did not really answer correctly, so here it is, dig it further to record that scenaria.

> 事件流是指事件从 DOM 树的顶端 Window 向目标元素传播，然后再从目标元素传播至顶端的过程。
> 从顶而下特指事件的捕获、反之则叫事件的冒泡。默认情况下事件是在冒泡时触发。反之则是捕获阶段（addEventListener 方法第三个参数为 True 时）

## Event Capture/Bubble

- 不能冒泡的事件

`blur、focus、load、unload、onmouseenter、onmouseleave。`

- 判断一个元素的触发事件是否能冒泡

```javascript
element.onclick = function (event) {
  event = event || window.event;
  console.log(event.bubbles); //打印结果：true。说明 onclick 事件是可以冒泡的
};
```

- 如何阻止冒泡

```javascript
 element.onclick = function (event) {
        event = event || window.event;
​
        if (event && event.stopPropagation) {
            event.stopPropagation();
        } else {
            event.cancelBubble = true; // for <= IE 10
        }
    }
```

## Event Delegate

Scenaria：

```html
<ul class="myul">
  <li class="li-link">风急天高猿啸哀，</li>
  <li class="li-link">渚清沙白鸟飞回。</li>
  <li class="li-link">无边落木萧萧下，</li>
  <li class="li-link">不尽长江滚滚来。</li>
  <button class="btn-read">Read</button>
  <button class="btn-write">Write</button>
</ul>
```

这里有 2 种方法都可以拿到每一个子元素的事件，但是需要用到 `loop` ，如果子元素太多，性能肯定会受影响。

```javascript
let myul = document.querySelector(".myul");
let liLinks = document.querySelectorAll(".li-link");
liLinks.forEach((e) => {
  e.addEventListener("click", (el) => {
    console.log("forEach", el.target);
  });
});

let subLink = myul.getElementsByClassName("li-link");
for (let i = 0; i < subLink.length; i++) {
  subLink[i].onclick = (e) => {
    console.log("forLoop", e.target);
  };
}
```

此时我们可以利用冒泡机制，把 `click` 事件绑定到父元素上，当父元素捕获到事件之后，通过 `event.target` 拿到被点击的子元素，从而可以执行业务逻辑。

```javascript
myul.addEventListener(
  "click",
  (event) => {
    event = event || window.event;

    if (event.target && event.target.className === "li-link") {
      console.log("父元素事件： ", event.target);
    }
  },
  false
);
```

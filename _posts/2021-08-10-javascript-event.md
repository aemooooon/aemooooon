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

* 不能冒泡的事件

``
blur、focus、load、unload、onmouseenter、onmouseleave。
``

* 判断一个元素的触发事件是否能冒泡

```javascript
element.onclick = function (event) {
        event = event || window.event;
        console.log(event.bubbles); //打印结果：true。说明 onclick 事件是可以冒泡的
    }
```

* 阻止冒泡

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
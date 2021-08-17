---
layout: post
subtitle: 函数
categories: [JavaScript]
header:
  image: header.jpg
  align:
  text: light
---

今天去黄欣辰教育咨询公司面试，去了前台小姐姐就给了一张面试题（共四页，每页 3 道题），让我 30 分钟做完，还有一张非常详细的个人信息表需要填写。在做的过程中有熟悉的，也有不会的，所以特地回忆一下，做个记录，毕竟 **ES2015** 我确实基础薄弱。

## let 7 var

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

## Function

第二道题用到了函数的 prototype、apply、call 等实例方法，这个确实是我不太了解的。虽然题目可能答对了，但也是蒙的。行了，看看 MDN 吧！

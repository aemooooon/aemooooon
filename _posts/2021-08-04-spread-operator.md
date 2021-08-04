---
layout: post
subtitle: spread ...
categories: [JavaScript]
header:
    image: header.jpg
    align:
    text: light
---

JavaScript 接收多个参数的形式是依次用逗号隔开，如果传入的是数组`[a, b]`形式的参数，就必须使用 `apply` 来分解。ES6 的spread操作符更加简化了`apply`的作用。

* 扩展运算符将字符串转为真正的数组

```
console.log([...'聘聘袅袅十三余']) 
// ["聘", "聘", "袅", "袅", "十", "三", "余"]
```

* 比如 `Math.max` 函数

```
Math.max(14, 3, 77); // default
Math.max.apply(null, [14, 3, 77]) // 传数组使用apply
Math.max(...[14, 3, 77]) // 传数组 ES6 写法
```

```
function add(x, y) {
  return x + y;
}
 
var numbers = [4, 38];
add(...numbers)// 42


//通过push函数，将一个数组添加到另一个数组的尾部
// ES5的 写法
var arr1 = [0, 1, 2];
var arr2 = [3, 4, 5];
Array.prototype.push.apply(arr1, arr2);
 
// ES6 的写法
var arr1 = [0, 1, 2];
var arr2 = [3, 4, 5];
arr1.push(...arr2);


//合并数组
// ES5
[1, 2].concat(more)
// ES6
[1, 2, ...more]
 
var arr1 = ['a','b'];
var arr2 = ['c'];
var arr3 = ['d','e'];
 
// ES5的合并数组
arr1.concat(arr2, arr3);
// [ 'a', 'b', 'c', 'd', 'e' ]
 
// ES6的合并数组
[...arr1, ...arr2, ...arr3]
// [ 'a', 'b', 'c', 'd', 'e' ]
```

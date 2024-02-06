---
layout: post
subtitle: 防抖 & 节流
categories: [JavaScript]
header:
  image: header.jpg
  align:
  text: light
---

当在页面上操作滚动条无限加载或者表单验证的时候，`scroll` 类似事件会频繁的响应。如果每次触发事件都去 Fetch 数据的话，性能肯定会被拖累。防抖和节流就是一种减少触发事件调用函数频率的方法。

> Debounc 如果持续触发事件，则最终只会在停止触发后的 `timeout` 后调用一次。scenaria 表单验证
> Throttle 如果持续触发事件，将在设定的 `timeout` 时间段内以其频率持续调用。scenaria 无限加载

Debounce example in JavaScript

```javascript
// debounce
function debounce(callback_fn, wait_time) {
  let timeout = null;
  return function () {
    if (timeout !== null) {
      clearTimeout(timeout);
    }
    timeout = setTimeout(callback_fn, wait_time);
  };
}

function handle_scroll() {
  console.log("doing something", Math.random());
}

window.addEventListener("scroll", debounce(handle_scroll, 1000));
```

Debounce example in React

```jsx
import debounce from "lodash.debounce";

class Searchbox extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.emitChangeDebounced = debounce(this.emitChange, 250);
  }

  componentWillUnmount() {
    this.emitChangeDebounced.cancel();
  }

  render() {
    return (
      <input
        type="text"
        onChange={this.handleChange}
        placeholder="Search..."
        defaultValue={this.props.value}
      />
    );
  }

  handleChange(e) {
    this.emitChangeDebounced(e.target.value);
  }

  emitChange(value) {
    this.props.onChange(value);
  }
}
```

Throttle example in JavaScipt

```javascript
var throttle = function (func, delay) {
  var timer = null;
  var startTime = Date.now(); //设置开始时间
  return function () {
    var curTime = Date.now();
    var remaining = delay - (curTime - startTime); //剩余时间
    var context = this;
    var args = arguments;
    clearTimeout(timer);
    if (remaining <= 0) {
      // 第一次触发立即执行
      func.apply(context, args);
      startTime = Date.now();
    } else {
      timer = setTimeout(func, remaining); //取消当前计数器并计算新的remaining
    }
  };
};
function handle() {
  console.log(Math.random());
}
window.addEventListener("scroll", throttle(handle, 2000));
```

Throttle example in JavaScipt

```jsx
import throttle from "lodash.throttle";

class LoadMoreButton extends React.Component {
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
    this.handleClickThrottled = throttle(this.handleClick, 1000);
  }

  componentWillUnmount() {
    this.handleClickThrottled.cancel();
  }

  render() {
    return <button onClick={this.handleClickThrottled}>Load More</button>;
  }

  handleClick() {
    this.props.loadMore();
  }
}
```

使用 `requestAnimationFrame` 节流

```jsx
import rafSchedule from 'raf-schd';

class ScrollListener extends React.Component {
  constructor(props) {
    super(props);

    this.handleScroll = this.handleScroll.bind(this);

    // Create a new function to schedule updates.
    this.scheduleUpdate = rafSchedule(
      point => this.props.onScroll(point)
    );
  }

  handleScroll(e) {
    // When we receive a scroll event, schedule an update.
    // If we receive many updates within a frame, we'll only publish the latest value.
    this.scheduleUpdate({ x: e.clientX, y: e.clientY });
  }

  componentWillUnmount() {
    // Cancel any pending updates since we're unmounting.
    this.scheduleUpdate.cancel();
  }

  render() {
    return (
      <div
        style={{ overflow: 'scroll' }}
        onScroll={this.handleScroll}
      >
        <img src="/my-huge-image.jpg" />
      </div>
    );
  }
}

```

ref: https://zh-hans.reactjs.org/docs/faq-functions.html
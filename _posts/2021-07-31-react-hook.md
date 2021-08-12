---
layout: post
subtitle: 钩子函数
categories: [React]
header:
  image: header.jpg
  align:
  text: light
---

最近面试前端，很多问题是关于 `React` 的，之前在项目里用的 `Hook` 主要是 `useState` 和 `useEffect` 这 2 个。这次借复习就好好完整的学习一下，做个记录，不仅为了面试，也是为了可以系统性的了解这个机制。

> Hook 是 React 16.8 的新增特性。它可以让你在不编写 class 的情况下使用 state 以及其他的 React 特性。Hook 使你在无需修改组件结构的情况下复用状态逻辑。Hook 将组件中相互关联的部分拆分成更小的函数（比如设置订阅或请求数据)。 Hook 使你在非 class 的情况下可以使用更多的 React 特性。

## Hook 规则

- 只在函数的最顶层以及任何 return 之前调用他们。
  - 在 React 的函数组件中调用 Hook
  - 在自定义 Hook 中调用其他 Hook
  - 不要在普通的 JavaScript 函数中调用 Hook
- 自定义 Hook 必须以 “use” 开头

## useState

***useState and Render***

- The setter function from a useState hook will cause the component to re-render.
- The exception is when you update a State Hook to the same value as the current state.
- Same value after the initial render? The component will not re-render.
- Same value after re-renders? React will render that specific component one more time and then bails out from any subsequent renders.

```javascript
import React, { useState } from "react";

function mTimes() {
  console.log("我会每次都渲染");
  return 4;
}

const UseState = () => {
  // 关于初始化
  // 1. 如果直接设置一个固定的默认值，每次更新都会渲染
  // 2. 所以可以写成一个函数，这样就只会渲染第一次
  // 3. 写成函数也有一个例外，就是如果把函数定义到主函数之外的话，也会每次都重新渲染
  // const [count, setCount] = useState(4);
  // const [count, setCount] = useState(mTimes);
  const [count, setCount] = useState(() => {
    console.log("我只会在刚开始渲染一次");
    return 4;
  });

  const [state, setState] = useState({ count: 4, theme: "blue" });

  function xxx() {
    setState((prevValue) => {
      // 如果初始化的是一个对象，则不能像这样修改
      // return { count: prevValue.count + 1}
      // 正确方法
      return { ...prevValue, count: prevValue + 1 };
    });
  }

  function increment() {
    // 这里虽然调用了2次，但是每次只改变一次的值
    setCount(count + 1);
    setCount(count + 1);
  }

  function decrement() {
    // 应该采用这种方法更新其值
    setCount((prevCount) => prevCount - 1);
    setCount((prevCount) => prevCount - 1);
  }

  return (
    <div>
      <button onClick={increment}>+</button>
      <span>{count}</span>
      <button onClick={decrement}>-</button>
    </div>
  );
};

export default UseState;
```

## useEffect

使用 `useEffect` 主要是注意 `依赖项` 的使用以及什么情况需要及时销毁

```javascript
import React, { useState, useEffect } from "react";

const UseEffect = () => {
  const [resourceType, setResourceType] = useState("posts");
  const [result, setResult] = useState([]);

  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

  const handleResize = () => {
    setWindowWidth(window.innerWidth);
  };

  console.log("render");

  useEffect(() => {
    console.log("useEffect");

    let ignore = false;

    function fetchContent() {
      fetch(`https://jsonplaceholder.typicode.com/${resourceType}`)
        .then((response) => response.json())
        .then((json) => {
          if (!ignore) {
            setResult(json);
          }
        });
    }

    fetchContent();

    window.addEventListener("resize", handleResize);

    return () => {
      ignore = true;
      window.removeEventListener("resize", handleResize);
      console.log("clean up");
    };
  }, [resourceType]);

  return (
    <React.Fragment>
      <div>
        <button onClick={() => setResourceType("posts")}>Posts</button>
        <button onClick={() => setResourceType("comments")}>comments</button>
        <button onClick={() => setResourceType("users")}>users</button>
      </div>
      <h1>
        {resourceType} {windowWidth}
      </h1>
      <div>
        {result.map((item) => {
          return <pre key={item.id}>{JSON.stringify(item)}</pre>;
        })}
      </div>
    </React.Fragment>
  );
};

export default UseEffect;
```

one more good example: https://codesandbox.io/s/jvvkoo8pq3

https://www.robinwieruch.de/react-hooks-fetch-data

## useReducer

An example of Counter by using useState

```javascript
import React, { useState } from "react";

const UseReducer = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount((prevValue) => prevValue + 1);
  };

  const decrement = () => {
    setCount((prevValue) => prevValue - 1);
  };

  return (
    <div>
      <button onClick={increment}>increment</button>
      <div>{count}</div>
      <button onClick={decrement}>decrement</button>
    </div>
  );
};

export default UseReducer;
```

Same example by using reducer

```javascript
import React, { useReducer } from "react";

const ACTIONS = {
  INCREMENT: "increment",
  DECREMENT: "decrement",
};

function reducer(state, action) {
  switch (action.type) {
    case ACTIONS.INCREMENT:
      return { count: state.count + 1 };
    case ACTIONS.DECREMENT:
      return { count: state.count - 1 };
    default:
      return state;
  }
}

const UseReducer = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  const increment = () => {
    dispatch({ type: ACTIONS.INCREMENT });
  };

  const decrement = () => {
    dispatch({ type: ACTIONS.DECREMENT });
  };

  return (
    <div>
      <button onClick={increment}>increment</button>
      <div>{state.count}</div>
      <button onClick={decrement}>decrement</button>
    </div>
  );
};

export default UseReducer;
```

Using useReducer fetch data

```javascript
import React, { useEffect, useReducer } from "react";
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com",
});

const ACTIONS = {
  FETCH_SUCCESS: "FETCH_SUCCESS",
  FETCH_ERROR: "FETCH_ERROR",
};

const initialState = {
  loading: true,
  error: "",
  post: {},
};

const reducer = (state, action) => {
  switch (action.type) {
    case ACTIONS.FETCH_SUCCESS:
      return {
        loading: false,
        post: action.payload,
        error: "",
      };
    case ACTIONS.FETCH_ERROR:
      return {
        loading: false,
        post: {},
        error: "Something went wrong",
      };
    default:
      return state;
  }
};

function DataFetching() {
  const [state, dispatch] = useReducer(reducer, initialState);

  useEffect(() => {
    axiosInstance
      .get("/posts/1")
      .then((res) => {
        dispatch({ type: ACTIONS.FETCH_SUCCESS, payload: res.data });
      })
      .catch((err) => {
        dispatch({ type: ACTIONS.FETCH_ERROR });
      });
  }, []);

  return (
    <div>
      {state.loading ? "loading" : state.post.title}
      {state.error ? state.error : null}
    </div>
  );
}

export default DataFetching;
```

Combination of usereducer and useContent

- app.js

```jsx
import React, { useReducer } from "react";
import "./sass/app.scss";
import ComponentA from "./component/ComponentA";
import ComponentB from "./component/ComponentB";
import ComponentC from "./component/ComponentC";

export const CountContext = React.createContext();

const initialState = 0;
const reducer = (state, action) => {
  switch (action) {
    case "increment":
      return state + 1;
    case "decrement":
      return state - 1;
    case "reset":
      return initialState;
    default:
      return state;
  }
};

function App() {
  const [count, dispatch] = useReducer(reducer, initialState);

  return (
    <CountContext.Provider
      value={{ countState: count, countDispatch: dispatch }}
    >
      <div>
        <p style={{ textAlign: "center", height: "100px", paddingTop: "50px" }}>
          Count: {count}
        </p>
        <ComponentA />
        <ComponentB />
        <ComponentC />
      </div>
    </CountContext.Provider>
  );
}

export default App;
```

- Child component likes below 不管子组件有多少层，直接调用

```jsx
import React, { useContext } from "react";
import { CountContext } from "../App";

function ComponentA() {
  const countContext = useContext(CountContext);

  return (
    <div style={{ backgroundColor: "red", padding: "2rem" }}>
      <h1>A: {countContext.countState}</h1>
      <button onClick={() => countContext.countDispatch("increment")}>
        Increment
      </button>
      <button onClick={() => countContext.countDispatch("decrement")}>
        Decrement
      </button>
      <button onClick={() => countContext.countDispatch("reset")}>Reset</button>
    </div>
  );
}

export default ComponentA;
```

## useContext

### Basic usage

e.g. 通过 toggle 按钮改变全站主题颜色

// app.js

```java
import React, {useState} from "react";
import FunctionContextComponent from './component/FunctionContextComponent';
import ClassContextComponent from './component/ClassContextComponent';

export const ThemeContext = React.createContext();

function App() {

  const [darkTheme, setDarkTheme] = useState(true)

  function toggleTheme(){
    setDarkTheme(prevDarkTheme => ! prevDarkTheme)
  }

  return (
    <div>
      <ThemeContext.Provider value={darkTheme}>
        <button onClick={toggleTheme}>Toggle Theme</button>
        <FunctionContextComponent />
        <ClassContextComponent />
      </ThemeContext.Provider>
    </div>
  );
}

export default App;
```

// ClassContextComponent.js 类组件调用

```java
import React, { Component } from 'react';
import { ThemeContext } from '../App'

class ClassContextComponent extends Component {
    themeStyles(dark){
        return {
            backgroundColor: dark ? '#333' : '#ccc',
            color: dark ? '#ccc' : '#333',
            padding: '2rem',
            margin: '2rem'
        }
    }

    render() {
        return (
            <ThemeContext.Consumer>
                {
                    darkTheme => {
                        return <div style={this.themeStyles(darkTheme)}>Class Theme</div>
                    }
                }
            </ThemeContext.Consumer>
        );
    }
}

export default ClassContextComponent;

```

// FunctionContextComponent.js 函数组件调用

```java
import React, {useContext} from 'react'
import { ThemeContext } from '../App'

const FunctionContextComponent = () => {
    const darkTheme = useContext(ThemeContext)
    const themeStyles ={
        backgroundColor: darkTheme ? '#333' : '#ccc',
        color: darkTheme ? '#ccc' : '#333',
        padding: '2rem',
        margin: '2rem'
    }
    return (
        <div style={themeStyles}>
            Function Theme
        </div>
    )
}

export default FunctionContextComponent

```

### usage with custome hook

- Create a file `ThemeContext.js` under the `src`.

```javascript
import React, { useContext, useState } from "react";

const ThemeContext = React.createContext();
const ThemeUpdateContext = React.createContext();

export function useTheme() {
  return useContext(ThemeContext);
}

export function useThemeUpdate() {
  return useContext(ThemeUpdateContext);
}

export function ThemeProvider({ children }) {
  const [darkTheme, setDarkTheme] = useState(true);

  function toggleTheme() {
    setDarkTheme((prevDarkTheme) => !prevDarkTheme);
  }

  return (
    <ThemeContext.Provider value={darkTheme}>
      <ThemeUpdateContext.Provider value={toggleTheme}>
        {children}
      </ThemeUpdateContext.Provider>
    </ThemeContext.Provider>
  );
}
```

- `App.js`

```javascript
import { ThemeProvider } from "./ThemeContext";

return (
  <div>
    <ThemeProvider>
      <FunctionContextComponent />
    </ThemeProvider>
  </div>
);
```

- Child which is functional component calling

```javascript
import React from "react";
import { useTheme, useThemeUpdate } from "../ThemeContext";

const FunctionContextComponent = () => {
  const darkTheme = useTheme();
  const toggleTheme = useThemeUpdate();
  const themeStyles = {
    backgroundColor: darkTheme ? "#333" : "#ccc",
    color: darkTheme ? "#ccc" : "#333",
    padding: "2rem",
    margin: "2rem",
  };
  return (
    <>
      <button onClick={toggleTheme}>Toggle Theme</button>
      <div style={themeStyles}>Function Theme</div>
    </>
  );
};

export default FunctionContextComponent;
```

## 自定义 Hook

> Scenaria 当多个函数组件需要共享业务逻辑的时候，e.g. 表单处理、动画、订阅声明、计时器

例子 1：模仿一个用法/语法跟 `useState` 一模一样的自定义 `Hook`，把表单输入值实时存入到 `LocalStorage` 里面。

// useLocalStorage.js

```javascript
import { useState, useEffect } from "react";

function getSavedValue(key, initialValue) {
  const savedValue = JSON.parse(localStorage.getItem(key));
  if (savedValue) return savedValue;

  // 模仿一下 React 内置的 useState 既可以接收值作为参数，也可以接收 函数 作为参数
  if (initialValue instanceof Function) return initialValue();
  return initialValue;
}

export default function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    return getSavedValue(key, initialValue);
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [value]);

  return [value, setValue];
}

// 使用/调用
const [name, setName] = useLocalStorage("name", "");

return (
  <div>
    <input value={name} onChange={(e) => setName(e.target.value)} type="text" />
  </div>
);
```

例子 2： 不需要返回值/回调的操作

// useUpdateLogger.js

```javascript
import { useEffect } from "react";

export default function useUpdateLogger(initialValue) {
  useEffect(() => {
    // 单纯的在控制台输出值（如果值改变的话）
    console.log(initialValue);
  }, [initialValue]);
}

// 使用/调用
useUpdateLogger(name); // name 就是我们在调用页面需要观察的值（变量）
```

例子 3： 需要返回值/回调的操作
// useWinSize.js

```javascript
import { useState, useEffect, useCallback } from 'react'

export default function useWinSize() {

    const [size, setSize] = useState({
        width: document.documentElement.clientWidth,
        height: document.documentElement.clientHeight
    })

    const onResize = useCallback(() => {
        setSize({
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight
        })
    }, [])

    useEffect(() => {
        window.addEventListener('resize', onResize)
        return () => {
            window.removeEventListener('resize', onResize)
        }
    }, [])

    return size;

}


// app.js to call
import useWinSize from "./hook/useWinSize";

const size = useWinSize()

<div>The size of Window: width: {size.width}, height: {size.height}</div>

```

## useMemo

```js
import React, { useState, useMemo, useEffect } from "react";

// 使用场景
// 1. 当某个函数计算量非常大，十分耗费资源，需要考虑是否使用 useMemo 避免每次渲染都执行
// 2.

const UseMem = () => {
  const [number, setNumber] = useState(0);
  const [dark, setDark] = useState(false);

  // 如果直接调用 slowFunction ，则每次渲染都会执行大计算量的 slowFunction
  // const doubleNumber = slowFunction(number);
  // 使用 useMemo 如果依赖变量不发生变化，则不会执行 useMemo 里面的大计算量函数
  const doubleNumber = useMemo(() => {
    return slowFunction(number);
  }, [number]);

  // 由于 themeStyles 对象（数组，对象）是引用类型，所以如果作为 useEffect 的依赖，每次会因为变量引用的不一样，而每次都渲染
  // ESLINT 提示： The 'themeStyles' object makes the dependencies of useEffect Hook (at line 27) change on every render. To fix this, wrap the initialization of 'themeStyles' in its own useMemo() Hook.

  // const themeStyles = {
  //     backgroundColor: dark ? 'black' : 'white',
  //     color: dark ? 'white' : 'black'
  // }
  // useEffect(
  //     () => {
  //         console.log('Theme Changed')
  //     }, [themeStyles]
  // )

  const themeStyles = useMemo(() => {
    return {
      backgroundColor: dark ? "black" : "white",
      color: dark ? "white" : "black",
    };
  }, [dark]); // 这样就只会在 dark 改变的情况下，在 useEffect 里重新渲染

  useEffect(() => {
    console.log("Theme Changed");
  }, [themeStyles]);

  return (
    <div>
      <input
        type="number"
        value={number}
        onChange={(e) => setNumber(parseInt(e.target.value))}
      />
      <button onClick={() => setDark((prevDark) => !prevDark)}>
        Change Theme
      </button>
      <div style={themeStyles}>{doubleNumber}</div>
    </div>
  );

  function slowFunction(num) {
    console.log("Calling Slow Function");
    for (let i = 0; i < 1000000000; i++) {}
    return num * 2;
  }
};

export default UseMem;
```

## useCallback

> The one big difference between useMemo and useCallback is that
> useMemo it takes a function and it's going to return to you the return value of that function, but
> useCallback it takes a function but that is actually what the useCallback returns.

```javascript
import React, { useState, useEffect, useCallback } from "react";

const List = ({ getItems }) => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    setItems(getItems(5));
    console.log("Updating Items");
  }, [getItems]);

  return items.map((item) => <div key={item}>{item}</div>);
};

const UseCallback = () => {
  const [number, setNumber] = useState(1);
  const [dark, setDark] = useState(false);

  const getItems = useCallback(
    (incrementor) => {
      return [
        number + incrementor,
        number + 1 + incrementor,
        number + 2 + incrementor,
      ];
    },
    [number]
  );

  const theme = {
    backgroundColor: dark ? "#333" : "#fff",
    color: dark ? "#fff" : "#333",
  };

  return (
    <div style={theme}>
      <input
        type="number"
        value={number}
        onChange={(e) => setNumber(parseInt(e.target.value))}
      />
      <button onClick={() => setDark((prevDark) => !prevDark)}>
        Toggle theme
      </button>
      <List getItems={getItems}></List>
    </div>
  );
};

export default UseCallback;
```

## useRef

- 用来操作引用的 dom 而不用重新渲染

```javascript
const inputRef = useRef();

function focus(){
    inputRef.current.focus();
    inputRef.current.style="border:1px solid red";
}

<input ref={inputRef}>
<button onClick={focus}>Focus</button>

```

## Using Bootstrap5+ in React

- Install bootstrap: `npm install bootstrap`

- import it in index.js: `import 'bootstrap/dist/css/bootstrap.min.css';`

## Using sass in React

- Install sass: `npm install --save-dev sass`

- create resources

```bash
.
├── App.js
├── css
│   └── app.css
├── index.js
└── sass
    └── app.scss
```

- Import in App.js: `import './sass/app.scss'`

- Append in `package.json` after scripts: `"sass" : "sass src/Sass:src/Css --watch --no-source-map"`

- Run with terminal: `npm run sass`

> Hook part ref from: https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw

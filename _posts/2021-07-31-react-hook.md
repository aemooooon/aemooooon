---
layout: post
subtitle: collections
categories: [React]
header:
    image: header.jpg
    align:
    text: light
---

Hook 是 React 16.8 的新增特性。它可以让你在不编写 class 的情况下使用 state 以及其他的 React 特性。本文主要记录一下 Hook 的一些坑以及运行机制和使用技巧。

# Using Bootstrap5+ in React

* Install bootstrap: `npm install bootstrap`

* import it in index.js: `import 'bootstrap/dist/css/bootstrap.min.css';`

# Using sass in React

* Install sass: `npm install --save-dev sass`

* create resources
```sh
.
├── App.js
├── css
│   └── app.css
├── index.js
└── sass
    └── app.scss
```

* Import in App.js: `import './sass/app.scss'`

* Append in `package.json` after `scripts`: `"sass" : "sass src/Sass:src/Css --watch --no-source-map"`

* Run with terminal: `npm run sass`

# useState
```javascript
import React, { useState } from 'react'

function mTimes() {
    console.log('我会每次都渲染');
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
        console.log('我只会在刚开始渲染一次');
        return 4;
    })

    const [state, setState] = useState({ count: 4, theme: 'blue' })

    function xxx() {
        setState(prevValue => {
            // 如果初始化的是一个对象，则不能像这样修改
            // return { count: prevValue.count + 1}
            // 正确方法
            return { ...prevValue, count: prevValue + 1 }
        })
    }

    function increment() {
        // 这里虽然调用了2次，但是每次只改变一次的值
        setCount(count + 1);
        setCount(count + 1);
    }

    function decrement() {
        // 应该采用这种方法更新其值
        setCount(prevCount => prevCount - 1);
        setCount(prevCount => prevCount - 1);
    }


    return (
        <div>
            <button onClick={increment}>+</button>
            <span>{count}</span>
            <button onClick={decrement}>-</button>
        </div>
    )
}

export default UseState

```

# useEffect
```javascript
import React, { useState, useEffect } from 'react'

const UseEffect = () => {
    const [resourceType, setResourceType] = useState('posts');
    const [result, setResult] = useState([]);

    const [windowWidth, setWindowWidth] = useState(window.innerWidth);

    const handleResize = () => {
        setWindowWidth(window.innerWidth);
    }

    console.log('render')

    useEffect(
        () => {
            console.log('useEffect');

            let ignore = false;

            function fetchContent(){
                fetch(`https://jsonplaceholder.typicode.com/${resourceType}`)
                .then(response => response.json())
                .then(json => {
                    if (!ignore) {
                        setResult(json)
                    }
                });
            }

            fetchContent();

            window.addEventListener('resize', handleResize)

            return () => {
                ignore = true;
                window.removeEventListener('resize', handleResize);
                console.log('clean up')
            }

        }, [resourceType]
    )

    return (
        <React.Fragment>
            <div>
                <button onClick={() => setResourceType('posts')}>Posts</button>
                <button onClick={() => setResourceType('comments')}>comments</button>
                <button onClick={() => setResourceType('users')}>users</button>
            </div>
            <h1>{resourceType} {windowWidth}</h1>
            <div>
                {result.map(item => {
                    return (<pre key={item.id}>{JSON.stringify(item)}</pre>)
                })}
            </div>
        </React.Fragment>
    )
}

export default UseEffect

```

one more good example: https://codesandbox.io/s/jvvkoo8pq3

https://www.robinwieruch.de/react-hooks-fetch-data


# useContext

## Basic usage

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

## usage with custome hook

* Create a file `ThemeContext.js` under the `src`.

```python
import React, { useContext, useState } from "react";

const ThemeContext = React.createContext()
const ThemeUpdateContext = React.createContext()

export function useTheme() {
    return useContext(ThemeContext)
}

export function useThemeUpdate() {
    return useContext(ThemeUpdateContext)
}

export function ThemeProvider({ children }) {
    const [darkTheme, setDarkTheme] = useState(true)

    function toggleTheme() {
        setDarkTheme(prevDarkTheme => !prevDarkTheme)
    }

    return (
        <ThemeContext.Provider value={darkTheme}>
            <ThemeUpdateContext.Provider value={toggleTheme}>
                {children}
            </ThemeUpdateContext.Provider>
        </ThemeContext.Provider>
    )
}
```

* `App.js`

```
import { ThemeProvider } from './ThemeContext'

  return (
    <div>
      <ThemeProvider>
        <FunctionContextComponent />
      </ThemeProvider>
    </div>
  );

```

* Child which is functional component calling

```javascript
import React from 'react'
import { useTheme, useThemeUpdate } from '../ThemeContext'

const FunctionContextComponent = () => {
    const darkTheme = useTheme()
    const toggleTheme = useThemeUpdate()
    const themeStyles = {
        backgroundColor: darkTheme ? '#333' : '#ccc',
        color: darkTheme ? '#ccc' : '#333',
        padding: '2rem',
        margin: '2rem'
    }
    return (
        <>
            <button onClick={toggleTheme}>Toggle Theme</button>
            <div style={themeStyles}>
                Function Theme
            </div>
        </>

    )
}

export default FunctionContextComponent

```

# useMemo

```js
import React, { useState, useMemo, useEffect } from 'react'

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
            backgroundColor: dark ? 'black' : 'white',
            color: dark ? 'white' : 'black'
        }
    }, [dark]) // 这样就只会在 dark 改变的情况下，在 useEffect 里重新渲染

    useEffect(
        () => {
            console.log('Theme Changed')
        }, [themeStyles]
    )

    return (
        <div>
            <input type="number" value={number} onChange={e => setNumber(parseInt(e.target.value))} />
            <button onClick={() => setDark(prevDark => !prevDark)}>Change Theme</button>
            <div style={themeStyles}>{doubleNumber}</div>
        </div>
    )

    function slowFunction(num) {
        console.log('Calling Slow Function');
        for (let i = 0; i < 1000000000; i++) {

        }
        return num * 2;
    }
}

export default UseMem

```

# useRef

* 用来操作引用的 dom 而不用重新渲染

```javascript
const inputRef = useRef();

function focus(){
    inputRef.current.focus();
    inputRef.current.style="border:1px solid red";
}

<input ref={inputRef}>
<button onClick={focus}>Focus</button>

```
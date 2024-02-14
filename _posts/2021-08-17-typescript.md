---
layout: post
subtitle: TypeScript
categories: [TypeScript]
header:
  image: header.jpg
  align:
  text: light
---

# TypeScript crash experience.

- 初始化 ts 配置文件 `tsc --init`
- 编译文件 `tsc filename`

```typescript
// Basic Types
let id: number = 5;
let name: string = "Hua";
let isPublished: boolean = true;
let x: any = "Hello";

// Array
let ids: mumber[] = [1, 2, 3, 4, 5];
let arry: any[] = [1, true, "hi"];

// Tuple
let person: [number, string, boolean] = [1, "aemon", false];

// Tuple Array
let person: [number, string][];
person = [
  [1, "a"],
  [2, "b"],
  [3, "c"],
];

// Union
let xid: string | number;
xid = "22";

// Enum
enum Direction {
  Up,
  Down,
  Left,
  Right,
}
conole.log(Direction.Up); // 0

// Objects
type User = {
  id: number;
  name: string;
};

const user: User = {
  id: 1,
  name: "John",
};

// Type Assertion
let cid: any = 1;
let customerId = <number>cid;
// or
let customerId = cid as number;

// Functions
function addNum(x: number, y: number): number {
  return x + y;
}

// Void
function log(message: string | number): void{
  console.log(message)
}

// Interfaces objects
interface Teacher {
  id: number;
  name: string;
  age?: number;
}

const teacher: Teacher = {
  id: 1,
  name: "John",
};

console.log(teacher);

// Interfaces Function
interface MathFunc {
  (x: number, y: number): number;
}

const add: MathFunc = (x: number, y: number): number => x + y;
const sub: MathFunc = (x: number, y: number): number => x - y;
const timer: MathFunc = (x: number, y: number): number => x * y;
const div: MathFunc = (x: number, y: number): number => x / y;

console.log(add(3,4))

// Interface connot using in primitive type with unions
type point= number | string 
let p: point = 1

// The code below are not allowed 
interface point1= number | string 
let p1: point1 = 1

// Classes
interface PersonInterface {
  id: number;
  name: string;
  register(): string;
}

// class Person 实现了上面的接口
// class field can be use modifier
// such as private public and protected
class Person implements PersonInterface {
  id: number;
  name: string;
  private _id: number = 0

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }

  register() {
    return `${this.name} is now registered.`;
  }
}

const mike = new Person(1, "Mike");
const hua = new Person(2, "hua");
console.log(mike, hua);
console.log(hua.register());

// sub class
class Employee extends Person {
  position: string;

  constructor(id: number, name: string, position: string) {
    super(id, name);
    this.position = position;
  }
}

const emp = new Employee(3, 'La', 'Developer')
console.log(emp.register())
console.log(emp.position)


// Generics
// scenario
function getArray(items: any[]): any[]{
    return new Array().concat(items)
}

let numArray = getArray([1,2,3])
let strArray = getArray(['a','b','c'])

numArray.push(1)
strArray.push('s')

console.log(numArray)
console.log(strArray)

// Generics way
function getArrayWithG<T>(items: T[]): T[]{
    return new Array().concat(items)
}

let numArrayG = getArrayWithG<number>([1,2,3])
let strArrayG = getArrayWithG<string>(['a','b','c'])

numArrayG.push(1)
strArrayG.push('s')

console.log(numArrayG)
console.log(strArrayG)

// React function component exampe
export interface Props{
  title: string
  color?: string
}

const Header = (props: Props) => {
  return (
    <header>
      <h1 style={{color: props.color ? props.color : "blue" }}>{props.title}<h1>
    </header>
  )
}

export default Header


```

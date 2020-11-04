let dog
let variableName

// 배열 - 배열은 복수형 이름을 사용
const cats = []

// 정규표현식 - 정규표현식은 'r'로 시작
// const rDesc = /[가-힣]/
// console.log('regex를 사용하면?', rDesc.test('안녕하세요'))
// console.log('regex를 사용하면?', rDesc.test('hello'))

// 함수
function getPropertyName () {}

// 이벤트 핸들러 - 이벤트 핸들러는 'on'으로 시작
function onClick () {}
function onKeyDown () {}

// 불린 반환 함수 - 반환 값이 불린인 함수는 'is'로 시작
let isAvailable = false

class User {
  constructor(options) {
    this.name = options.name
  }
}

const good = new User({
  name: '홍길동',
})

const API_KEY = 'SOMEKEY'
const PI = Math.PI

// let
// 재 할당 가능
// let x = 1
// x = 3

// 재 선언 불가
// let x = 1
// let x = 3  // Uncaught SyntaxError: Identifier 'x' has already been declared

// 블록 스코프
// let x = 1

// if (x === 1) {
//   let x = 2
//   console.log(x)  // 2
// }

// console.log(x)    // 1

// const
// 선언 시 반드시 할당
// const myFav = 7
// const myFav  // Uncaught SyntaxError: Missing initializer in const declaration

// 재 할당 불가
// const myFav = 7
// myFav = 20        // Uncaught TypeError: Assignment to constant variable.

// 재 선언 불가
// const myFav = 7
// const myFav = 10  // Uncaught SyntaxError: Identifier 'myFav' has already been declared
// var myFav = 10    // Uncaught SyntaxError: Identifier 'myFav' has already been declared
// let myFav = 10    // Uncaught SyntaxError: Identifier 'myFav' has already been declared

// 블록스코프
// const myFav = 7

// if (myFav === 7) {
//   const myFav = 20
//   console.log(myFav) // 20
// }

// console.log(myFav)   // 7

// var
// var num = 1
// var num = 2
// num  // 2

// 함수 스코프
// var a = 1
// let b = 2

// if (a === 1) {
//   var a = 11      // 전역변수 a 덮어쓰기
//   let b = 22      // if 내 지역변수

//   console.log(a)  // 11
//   console.log(b)  // 22
// } 

// console.log(a)    // 11
// console.log(b)    // 2


// hoisting
// console.log(name)  // undefined => 선언 이전에 참조

// var name = '홍길동'  // 선언 부


// let 이라면?
// console.log(name)  // Uncaught ReferenceError: Cannot access 'name' before initialization

// let name = '홍길동'
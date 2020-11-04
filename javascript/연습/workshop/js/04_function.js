// 선언식
function add (num1, num2) {
	return num1 + num2
}

console.log(add(2, 7)) // 9

// 표현식
// const sub = function (num1, num2) {
// 	return num1 - num2
// }

// sub(7, 2) // 5

// // 표현식에서 기명함수 사용
const mySub = function namedSub (num1, num2) {
	namedSub(1, 2)
	return num1 - num2
}

console.log(namedSub(1, 2))

// // 기본값
// const greeting = function (name = 'noName') {
// 	console.log(`hi ${name}`)
// }

// // type
// console.log(typeof add) // function
// console.log(typeof sub) // function

// 호이스팅
// addHoisting(2, 7) // 9

// function addHoisting (num1, num2) {
// 	return num1 + num2
// }

// subHoisting(7, 2) // Uncaught ReferenceError: Cannot access 'sub' before initialization

// const subHoisting = function (num1, num2) { // var라면 다를까?
// 	return num1 - num2
// }

// arrow function
// const arrow = function (name) {
//   return `hello! ${name}`
// }

// // 1. function 키워드 삭제
// const arrow = (name) => { return `hello! ${name}` }


// // 2. () 생략 (함수 매개변수가 하나일 경우만)
// const arrow = name => { return `hello! ${name}` }


// // 3. {} & return 생략 (바디가 표현식 1개인 경우만)
// const arrow = name => `hello! ${name}`
// console.log(arrow('num'))
const a = 13 
const b = -5 
const c = 3.14      
const d = 2.998e8   // 2.998 * 10^8 = 299, 800, 000
const e = Infinity 
const f = -Infinity
const g = NaN       // Not a Number

console.log(a, b, c, d, e, f, g)

// string
// const sentence1 = 'Hello SSAFY' // single quote
// const sentence2 = "Hello SSAFY" // double quote

// console.log(sentence1)
// console.log(sentence2)

// string addition
// const firstName = 'Tony'
// const lastName = 'Stark'
// const fullName = firstName + lastName

// console.log(fullName)

// 줄바꿈
// const word1 = "안녕 \n하세요"
// console.log(word1)

// const word = "안녕
// 하세요" // Uncaught SyntaxError: Invalid or unexpected token

// Template Literal
// const word2 = `안녕
// 들 하세요`
// console.log(word2)

// const age = 10 
// const message = `홍길동은 ${age}세입니다.`
// console.log(message)

// boolean
// const charm = true
// const geojit = false

// empty value
// let firstName  // 선언만 하고 할당하지 않음
// console.log(firstName)  // undefined

// let lastName = null
// console.log(lastName)  // null - 의도적으로 값이 없음을 표현함

// console.log(typeof null)          // "object"
// console.log(typeof(undefined))     // "undefined"

// 할당 연산자
// let c = 0

// c += 10 
// console.log(c) // 10 - c에 10을 더한다

// c -= 3 
// console.log(c) // 7 - c에 3을 뺀다

// c *= 10 
// console.log(c) // 70 - c에 10을 곱한다

// c++
// console.log(c) // 71 - c에 1을 더한다(증감식)

// c--
// console.log(c) // 70 - c에 1을 뺀다.(증감식)

// 비교 연산자
// 3 > 2    // true
// 3 < 2    // false

// 'A' < 'B'    // true
// 'Z' < 'a'    // true
// '가' < '나'   // true

// 동등 연산자
// const a = 1
// const b = '1'

// console.log(a == b)          // true
// console.log(a == Number(b))  // true - Number를 통해 숫자로 형변환

// // 자동 형변환 예시
// console.log(8 * null)    // 0, null은 0
// console.log('5' - 1)     // 4
// console.log('5' + 1)     // '51'
// console.log('five' * 2)  // NaN

// 일치 연산자
// const a = 1
// const b = '1'

// console.log(a === b)  // false 
// console.log(a === Number(b))  // true

// 논리 연산자
// true && false   // false
// true && true    // true

// 1 && 0 // 0 
// 0 && 1 // 0 
// 4 && 7 // 7

// false || true    // true
// false || false   // false

// 1 || 0 // 1
// 0 || 1 // 1
// 4 || 7 // 4

// !true  // false

// 삼항 연산자
// true ? 1 : 2    // 1
// false ? 1 : 2   // 2
// const result = Math.PI > 4 ? 'Yep' : 'Nope'
// console.log(result) // Nope
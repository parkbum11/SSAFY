// 배열
const numbers = [1, 2, 3, 4]

// numbers[0]      // 1
// numbers[-1]     // undefined => 정확한 양의 정수 index 만 가능
// numbers.length  // 4

// // reverse
// numbers.reverse()  // [4,3,2,1]
// numbers  // [4,3,2,1]
// numbers.reverse()  // [1,2,3,4]
// numbers  // [1,2,3,4]

// // push & pop
// numbers.push('a')  // 5, 새로운 배열의 길이
// numbers  // [1,2,3,4,'a']

// numbers.pop()  // 'a', 가장 마지막 요소
// numbers  // [1,2,3,4]

// // shift & unshift
// numbers.unshift('a')  // 5, 새로운 배열의 길이
// numbers  // ['a',1,2,3,4]
 
// numbers.shift()  // 'a', 가장 처음 요소
// numbers  // [1,2,3,4]

// // includes
// numbers.includes(1)  // true
// numbers.includes(0)  // false

// indexOf
numbers.push('a', 'a')
numbers  // [1,2,3,4,'a','a']
numbers.indexOf('a')  // 4
numbers.indexOf('b')  // -1
console.log("numbers.indexOf('b')", numbers.indexOf('b'))

// join
numbers.join()    // '1,2,3,4,a,a'
numbers.join('')  // '1234aa'
numbers.join('-') // '1-2-3-4-a-a'


// Object
const me = {
	name: '홍길동',  // key가 한 단어일 때
	'phone number': '01012345678',  // key가 여러 단어일 때
  appleProducts: {
		ipad: '2018pro',
		iphone: '7+',
		macbook: '2019pro',
	},
}

// 접근
me.name     // 홍길동
me['name']  // 홍길동
me['phone number']     // '01012345678'
me.appleProducts       // { ipad: '2018pro', ... }
me.appleProducts.ipad  // '2018pro'

// 축약 문법 (ES6+)
// let books = ['Learning JS', 'Eloquent JS']

// let comics = { 
//   DC: ['Aquaman', 'SHAZAM'], 
//   Marvel: ['Captain Marvel', 'Avengers'],
// }

// let magazines = null

// const bookShop = {
// 	books,
// 	comics,
// 	magazines,
// }

// console.log(bookShop) 
// console.log(typeof bookShop)  // object
// console.log(bookShop.books[0])

// 메소드 축약
// // ~ES5
// var obj = {
//   name: 'ssafy',
//   sayHi: function () {
//     console.log('Hi! ' + this.name);
//   }
// };

// obj.sayHi(); // Hi! ssafy

// // ES6+
// const obj2 = {
//   name: 'ssafy',
//   // 메소드 축약 표현
//   sayHi () {
//     console.log('Hi! ' + this.name);
//   }
// };

// obj2.sayHi() // Hi! ssafy


// JSON
// to JSON
const jsonData = JSON.stringify({
	coffee: 'Americano',
	iceCream: 'Cookie and cream',
})

console.log(jsonData)         //  "{"coffee":"Americano","iceCream":"Cookie and cream"}"
console.log(typeof jsonData)  // string

// to Object
const parsedData = JSON.parse(jsonData)

console.log(parsedData)         // {coffee: "Americano", iceCream: "Cookie and cream"}
console.log(typeof parsedData)  // object
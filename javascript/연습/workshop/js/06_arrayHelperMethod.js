// forEach
// const colors = ['red', 'blue', 'green']

// colors.forEach(function (color) {
//     console.log(color)
// })

// colors.forEach(color=>console.log(color))

// refactoring

// 리턴이 있는가?
// const result = colors.forEach(color => console.log(color))
// console.log(result) // undefined

// 실습 문제, images 배열안에 있는 정보를 통해 넓이를 구해서 areas에 저장하세요
// const images = [
//   { height: 10, width: 30 },
//   { height: 20, width: 90 },
//   { height: 54, width: 32 }
// ]
// const areas = []
// images.forEach( function (image) {
//   areas.push(image.height * image.width)
// })
// console.log(areas)

// map
// const numbers = [1, 2, 3]

// const doubleNumbers = numbers.map(function (number) {
//   return number * 2
// })
// console.log(doubleNumbers) // [ 2, 4, 6 ]

// // refactoring

// 실습 - 각 요소를 제곱한 결과를 담는 배열 squared를 map을 통해 만드세요
// const newNumbers = [4, 9, 16]

// const squaredNewNumbers = newNumbers.map(number=> { return number**2})

// // filter
// const products = [
//   { name: 'cucumber', type: 'vegetable' },
//   { name: 'banana', type: 'fruit' },
//   { name: 'carrot', type: 'vegetable' },
//   { name: 'apple', type: 'fruit' },
// ]

// const fruits = products.filter(function (product) {
//   return product.name === 'banana'
// })
// console.log("const fruits", fruits)

// // // refactoring

// // 실습 - numbers 중 50보다 큰 값만 모은 배열 filteredNumbers를 만드세요
// const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]
// const filteredNumbers = numbers.filter( number => number > 50 )
// console.log("filteredNumbers", filteredNumbers)

// // reduce
// const tests = [90, 90, 80, 77]

// const sum = tests.reduce(function (total, x) {
//   return total + x
// }, 0)  // 여기서 0 생략 가능

// // refactoring


// // 평균
// const sum = tests.reduce((total, x) => total + x, 0) / tests.length

// const plus = tests.reduce(function (total, x) {
//   if ((x%2) === 0) {
//     return total + x
//   }
//   else {
//     return 0 + total
//   }
// }, 0)
// console.log("plus", plus)


// 실습 - 주어진 baseUrl 문자열 뒤에 필수 요청 변수인 api 의 
// key — value 값을 key=value 의 형태로 더하여 요청 url을 만드세요. 
// URL에서 요청 변수는 & 문자로 구분합니다.
// object의 key를 배열로 만들어 주는 기능이 js에 있습니다. 찾아보세요!

// const baseUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'

// const api = {
//   'key': 'API_KEY',
//   'targetDt': '20200115'
// }

// const li = []
// for (const key in api) {
//   li.push(key + '=' + api[key])
// }
// console.log("li", li)

// const url = li.reduce(function (orUrl, i) {
//   return '&' + orUrl + i
// }, baseUrl)
// console.log("url", url)

// find 조건에 맞는 하나만 출력 filter랑 다른점이 이것!
const avengers = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
]

const avenger = avengers.find(function (avenger) {
  return avenger.name === 'Tony Stark'
})

// // refactoring
// const avenger = avengers.find(avenger => avenger.name === 'Tony Stark')

// // some
// const arr = [1, 2, 3, 4, 5]

// const result = arr.some(elem => elem % 2 === 0)  // true

// // every
// const arr = [1, 2, 3, 4, 5]

// const result2 = arr.every(elem => elem % 2 === 0)  // false
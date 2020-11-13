<template>
  <div>
    <h2>로또번호 추천</h2>
    <button @click="getLuckyNums">Pick My Lotto Numbers</button>
    <p>오늘의 추천 로또 번호</p>
    <ul>
      <li v-for="(num, idx) in selectedLuckyNums" :key="idx">{{ num }}</li>
    </ul>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      selectedLuckyNums: [],
    }
  },
  methods: {
    getLuckyNums: function () {
      const numbers = _.range(1, 46)
      this.sampleNums = _.sampleSize(numbers, 6)
      // console.log(this.sampleNums)

      this.selectedLuckyNums = _.sortBy(this.sampleNums)
      // this.selectedLuckyNums.sort(function (num1, num2) {
      //   return num1 - num2
      // })
    },
  }
}
</script>

<style>

</style>

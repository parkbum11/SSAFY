<template>
  <div>
    <h2>점심메뉴 추천</h2>
    <button @click="pickOneInLunchMenu">Pick My Lunch Menu!</button>
    <p>오늘의 점심 메뉴: {{ selectedLunchMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['국밥', '짜장면', '햄버거'],
      selectedLunchMenu: '',
    }
  },
  methods: {
    pickOneInLunchMenu: function () {
      const randomIndex = _.random(this.lunch.length - 1)
      // console.log(randomIndex)
      this.selectedLunchMenu = this.lunch[randomIndex]
    }
  }
}
</script>

<style>

</style>

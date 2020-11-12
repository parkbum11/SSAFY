<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
// 컴포넌트 불러오기
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  // 컴포넌트 등록
  components: {
    HelloWorld
  },
}
</script>

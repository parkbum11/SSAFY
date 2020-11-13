<template>
  <div>
    <Todo 
      v-for="(todo, idx) in todos" 
      :key="idx"
      :todo="todo"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'

import Todo from './Todo'

export default {
  name: 'TodoList',
  components: {
    Todo,
  },
  computed: {
    // todos: function () {
    //   return this.$store.state.todos
    // }

    //1. index.js의 todos를 todos라는 이름으로 TodoList 컴포넌트에서 쓰자
    // ...mapState({
    //   'todos': 'todos'
    // })

    //2. 
    ...mapState([
      'todos',
    ])
  }
}
</script>

<style>

</style>

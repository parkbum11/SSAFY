<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" :checked="todo.completed">
        <span>{{ todo.content }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todos: [],
    }
  },
  created() {
    // todos를 api를 찔러서 가져와서
    // data의 todos에 할당해준다
    // 가져오는 척을 할겁니다
    const receivedTodos = [
      {
        id:1,
        content: '할일 1',
        completed: true,
      },
      {
        id:2,
        content: '할일 2',
        completed: false,
      },
    ]
    this.todos = receivedTodos
  },
}
</script>

<style>

</style>
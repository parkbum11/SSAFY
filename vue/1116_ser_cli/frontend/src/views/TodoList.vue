<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" :checked="todo.completed" @change="updateTodo(todo)">
        <span>{{ todo.content }}</span>
        <button @click="deleteTodo(todo.id)">x</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      todos: [],
    }
  },
  methods: {
    deleteTodo(todoid) {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/todos/${todoid}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then(() => {
        this.todos = this.todos.filter((todo) => todo.id !== todoid)
      }).catch((err) => {
        console.log(err)
      })
    },
    updateTodo(todo) {
      axios({
        method: 'PUT',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
        data: {
          ...todo,
          completed: !todo.completed,
        }
      }).then((res) => {
        todo.completed = res.data.completed
      }).catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    axios ({
      method: 'GET',
      url: 'http://127.0.0.1:8000/todos/',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then(res => {
      this.todos = res.data
    })
  },
}
</script>

<style>

</style>
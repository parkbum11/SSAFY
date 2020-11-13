<template>
  <div>
    <div>
      <span :class="{ completed: todo.completed }" @click="updateTodoStatus">{{ todo.title }}</span>
    </div>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'Todo',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo: function () {
      this.$store.dispatch('deleteTodo', this.todo)
    },
    updateTodoStatus: function () {
      this.$store.dispatch('updateTodoStatus', this.todo)
    }
  }
}
</script>

<style scoped>
  .completed {
    text-decoration: line-through;
  }
</style>

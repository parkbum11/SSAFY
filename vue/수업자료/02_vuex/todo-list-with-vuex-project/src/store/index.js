import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [],
  },
  getters: {
    allTodosCount: function (state) {
      return state.todos.length
    },
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    },
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      // console.log(state)
      // console.log(todoItem)
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      //1. todos 배열을 반복하며
      state.todos = state.todos.map((todo) => {
        //2. 꺼내지는 todo 요소가 넘어온 todoItem과 동일한 경우
        if (todo === todoItem) {
          //3. 그 요소의 completed를 반대로 바꿔서 return
          return {
            // title: todoItem.title,
            ...todo,
            completed: !todo.completed
          }
        }
        //4. 같지 않은 경우는 todo를 그대로 return
        return todo
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      // console.log('createTodo from actions called!!')
      // console.log(context)
      // context.commit('CREATE_TODO', todoItem)

      // destructuring을 활용
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      // console.log(context)
      // console.log(todoItem)
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function ({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },
  plugins: [
    createPersistedState(),
  ]
})

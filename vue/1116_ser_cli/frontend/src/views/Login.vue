<template>
  <form @submit="login">
    <div>
      <label for="username">username : </label>
      <input type="text" id='username' v-model='username'>
    </div>
    <div>
      <label for="password">password : </label>
      <input type="text" id='password' v-model='password'>
    </div>
    <button>Log In</button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    login(event) {
      event.preventDefault()
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: {
            username: this.username,
            password: this.password,
          },
      }).then((res) => {
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
      }).catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>
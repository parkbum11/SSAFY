<template>
  <form @submit="signup">
    <div>
      <label for="username">username : </label>
      <input type="text" id='username' v-model='username'>
    </div>
    <div>
      <label for="password">password : </label>
      <input type="text" id='password' v-model='password'>
    </div>
    <div>
      <label for="passwordConfirmation">password check : </label>
      <input type="text" id='passwordConfirmation' v-model='passwordConfirmation'>
    </div>
    <button>Sign up</button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      username: '',
      password: '',
      passwordConfirmation: '',
    }
  },
  methods: {
    signup(event) {
      event.preventDefault()
      if (this.password !== this.passwordConfirmation) {
        alert('비밀번호 낫 일치 맨')
      }
      else {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1:8000/accounts/signup/',
          data: {
            username: this.username,
            password: this.password,
          }
        }).then((res) => {
          console.log(res.data)
          this.$router.push('/login')
        }).catch((err) => {
          console.log(err)
        })
      }
    },
  }
}
</script>

<style>

</style>
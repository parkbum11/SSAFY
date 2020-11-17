<template>
  <div id="app">
    <div id="nav">
      <span v-if='login'>
        <router-link to="/">TodoList</router-link> | 
        <router-link to="/create">AddTodo</router-link> | 
        <router-link to="#" @click.native="logout">Logout</router-link>

      </span>
      <span v-else>
        <router-link to="/signup">Signup</router-link> | 
        <router-link to="/login">Login</router-link>
      </span>
    </div>
    <router-view @login='setLogin'/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      login: false,
    }
  },
  methods:{
    setLogin() {
      this.login = true
      this.$router.push('/')
    },
    logout() {
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push('/login')
    },
  },
  created() {
    if (localStorage.getItem('jwt')) {
      this.login = true
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

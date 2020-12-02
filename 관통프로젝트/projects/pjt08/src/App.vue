<template>
  <div id="app">
    <div id="nav">
        <router-link :to="{ name: 'Home' }">Home</router-link> | 
        <router-link :to="{ name: 'Random' }">Random</router-link> |
        <router-link :to="{ name: 'MyMovieList' }">MyMovieList</router-link> |
    </div>
    <router-view />
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&display=swap');
#app {
  font-family: 'Nanum Myeongjo', serif;
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

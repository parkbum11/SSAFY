<template>
  <div>
    <div class="mainimage">
      <RecoMoviesWeather />
    </div>
    <div class="appstyling">
      <RecoMovies0 />
      <RecoMovies1 />
      <RecoMovies2 />
      <RecoMovies3 />
      <RecoMovies4 />
      <RecoMovies5 />
      <RecoMovies6 />
      <RecoMovies7 />
    </div>
    
  </div>
</template>

<script>
import RecoMoviesWeather from '../components/RecoMoviesWeather.vue'
import RecoMovies0 from '../components/RecoMovies0.vue'
import RecoMovies1 from '../components/RecoMovies1.vue'
import RecoMovies2 from '../components/RecoMovies2.vue'
import RecoMovies3 from '../components/RecoMovies3.vue'
import RecoMovies4 from '../components/RecoMovies4.vue'
import RecoMovies5 from '../components/RecoMovies5.vue'
import RecoMovies6 from '../components/RecoMovies6.vue'
import RecoMovies7 from '../components/RecoMovies7.vue'
import jwt_decode from 'jwt-decode'
// import axios from 'axios'
export default {
  name: 'Main',
  components: {
    RecoMoviesWeather, 
    RecoMovies0, 
    RecoMovies1, 
    RecoMovies2, 
    RecoMovies3, 
    RecoMovies4, 
    RecoMovies5, 
    RecoMovies6, 
    RecoMovies7, 
  },
  data() {
    return {
      userid: null,
      username: '',
    }
  },
  created() {
    const token = localStorage.getItem('jwt')
    this.userid = jwt_decode(token).user_id
    this.username = jwt_decode(token).username
    this.$store.commit('USER_INFO', this.userid)
    console.log(this.username)
    if (this.username == '') {
      this.$router.push('/login')
    }
  }
}
</script>

<style>
.mainimage{
  align-items:center;
  display:flex;
  background-image:url('https://nobutlisten.files.wordpress.com/2018/01/ironman_poster2.jpg');
  background-size: cover;
  height: 90vh;
}

.appstyling {
  background-color: black;
  margin-top: 0;
}
</style>
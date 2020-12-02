<template>
  <div class="bg">
    <div class="h2 mr-3" style="float: left;">내가 찜한 영화</div>
    <div style="float: left;" class="mt-1">
        <b-form-checkbox v-model="CommentOrNot" name="check-button" switch>리뷰 안한 영화 보기</b-form-checkbox>
      </div>
    <br><br>
    <v-row v-if="CommentOrNot">
      <v-col xs="12" sm="6" md="4" lg="3" xl="2" v-for="movie in myCommentMovies" :key="movie.pk" >
        <img @click="goMovieDetail(movie)" width="100%" height="100%" :src="movie.poster_path" :alt="movie.title">
      </v-col>
    </v-row>

    <v-row v-else>
      <v-col xs="12" sm="6" md="4" lg="3" xl="2" v-for="movie in movies" :key="movie.pk" >
        <img @click="goMovieDetail(movie)" width="100%" height="100%" :src="movie.poster_path" :alt="movie.title">
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

export default {
  name: 'MyLikedMovies',
  data() {
    return {
      movies: [],
      userid: null,
      username: '',
      CommentOrNot: false,
    }
  },
  methods: {
    goMovieDetail(movie) {
      this.$store.dispatch('goMovieDetail', movie)
      this.$router.push('/movieDetail')
    },
  },
  computed:{
    myCommentMovies(){
      return this.movies.filter((movie)=>{
        for (let index = 0; index < movie.comments.length; index++) {
          if (movie.comments[index].username===this.username){
            return false
          }
        }
        return true
      })
    }
  },
  created() {
    this.CommentOrNot = false
    const token = localStorage.getItem('jwt')
    this.userid = jwt_decode(token).user_id
    this.username=jwt_decode(token).username
    axios ({
      method: 'GET',
      url: `http://127.0.0.1:8000/accounts/profile/${this.username}`,
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res) => {
      this.movies = res.data.likeMovies
      console.log(res)
    }).catch((err) => {
      console.log(err)
    })
  },
    
}
</script>

<style>
.bg {
  background-color: #141414;
  color: white;
  margin-top: 120px;
  margin-bottom: 50px;
  margin-left: 100px;
  margin-right: 98px;
  height: 100%;
}
</style>
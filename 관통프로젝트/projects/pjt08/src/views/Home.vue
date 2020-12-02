<template>
  <b-container >
    <h1>Movies</h1>
    <b-row>
        <MovieCard
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
        />
    </b-row>
  </b-container>
</template>

<script>
import MovieCard from '../components/MovieCard'
import axios from 'axios'
export default {
  components: {
    MovieCard,
  },
  data: function () {
    return {
      movies:[],
    }
  },
  created(){
    const MOVIE_URL='https://gist.githubusercontent.com/eduChange-hphk/756c987fe4ecf20ef27fd1d29f90764e/raw/f5a6acfed6bbe837d7f2f173a5b84221ee54c3b2/movies.json'
    axios({
      url:MOVIE_URL,
      method:'GET',
    })
    .then((res)=>{
      this.movies=res.data
      console.log(this.movies)
    })
    .catch((err)=>{
      console.error(err)
    })
  }
  
}
</script>

<style>

</style>
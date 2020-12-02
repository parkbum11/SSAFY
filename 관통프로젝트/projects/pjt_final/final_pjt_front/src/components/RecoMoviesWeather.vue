<template>
  <div class="container">
    <div class="mb-3">
      <h1 class="text-center text-white">오늘의 날씨는 어떤가요?</h1>
    </div>
    <div class="container text-center mb-3">
      <i @click="getMoviesSun" class="title fas fa-sun fa-4x mx-3 text-white"></i>
      <i @click="getMoviesCloud" class="title fas fa-cloud fa-4x mx-3 text-white"></i>
      <i @click="getMoviesRain" class="title fas fa-umbrella fa-4x mx-3 text-white"></i>
      <i @click="getMoviesSnow" class="title fas fa-snowflake fa-4x mx-3 text-white"></i>
    </div>
    <div v-if="isShow" class="mb-3">
      <h3 class="text-center text-white">그렇다면 이런 영화는 어떤가요?</h3>
      <vueper-slides
        class="no-shadow"
        :visible-slides="6"
        :slide-ratio="1 / 4"
        :gap="1"
        :bullets='false'
        :slideMultiple='true'
        :autoplay='true'
        :dragging-distance="70">
        <vueper-slide
          v-for="(movie, i) in movies" 
          :key="i" 
          :image="movie.poster_path" 
          @click.native="goMovieDetail(movie)"
        />
      </vueper-slides>
    </div>
    <h3 v-if="isShow" @click="noRecomment" class="title text-right text-white"><i class="fas fa-sad-cry fa-3x text-white"></i>&nbsp; 추천 안받을래요.</h3>
  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
import axios from 'axios'

export default {
  name: 'RecoMoviesWeather',
  components: { VueperSlides, VueperSlide },
  data() {
    return {
      isShow:false,
      movies: []
    }
  },
  created(){
    this.isShow=false
  },
  methods: {
    noRecomment(){
      this.isShow=false
    },
    goMovieDetail(movie) {
      this.$store.dispatch('goMovieDetail', movie)
      this.$router.push('/movieDetail')
    },
    getMoviesSun(){
      // this.isShow=true
      axios ({
        method: 'GET',
        url: 'http://127.0.0.1:8000/movies/sun/',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
      .then((res) => {
          this.movies = res.data
          this.isShow=true
          // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMoviesCloud(){
      axios ({
        method: 'GET',
        url: 'http://127.0.0.1:8000/movies/cloud/',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
      .then((res) => {
          this.movies = res.data
          this.isShow=true
          // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMoviesRain(){
      axios ({
        method: 'GET',
        url: 'http://127.0.0.1:8000/movies/rain/',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
      .then((res) => {
          this.movies = res.data
          this.isShow=true
          // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMoviesSnow(){
      axios ({
        method: 'GET',
        url: 'http://127.0.0.1:8000/movies/snow/',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
      .then((res) => {
          this.movies = res.data
          this.isShow=true
          // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style>
.change-size-hover{
  transition: all 1.5s;
}
.change-size-hover:hover{
  width: 600px;
  height: 400px;
  background-color: black;
}
</style>
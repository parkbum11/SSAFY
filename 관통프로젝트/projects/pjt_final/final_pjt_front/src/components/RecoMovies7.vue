<template>
  <div class="container my-5">
    <div class="mb-3">
      <span class='h4 text-monoscope text-white'>국가 영화</span>
    </div>
    <vueper-slides
      class="no-shadow"
      :touchable="false"
      :visible-slides="6"
      :slide-ratio="1 / 4"
      :gap="1"
      :bullets='false'
      :slideMultiple='true'
      :autoplay='true'
      :dragging-distance="70">
      <vueper-slide @click.native="goMovieDetail(movie)" v-for="(movie, i) in movies" :key="i" :image="movie.poster_path" />
    </vueper-slides>
  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
import axios from 'axios'

export default {
  name: 'RecoMovies7',
  components: { VueperSlides, VueperSlide },
  data() {
    return {
      movies: []
    }
  },
  methods: {
    goMovieDetail(movie) {
      this.$store.dispatch('goMovieDetail', movie)
      this.$router.push('/movieDetail')
    },
  },
  created() {
    axios ({
      method: 'GET',
      url: 'http://127.0.0.1:8000/movies/nation/',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
      }).then((res) => {
        this.movies = res.data
        console.log(res)
      }).catch((err) => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>
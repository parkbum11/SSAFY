<template>
  <b-col cols="4">
    <b-card
      :title="movie.title"
      :img-src="movie.poster_path"
      :img-alt="movie.title"
    >
      <b-card-text>{{movie.overview}}</b-card-text>
    </b-card>  
  </b-col>
</template>

<script>
export default {
  name:"MovieCard",
  props:{
    movie:Object,
  }
}
</script>

<style>

</style>
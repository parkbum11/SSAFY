<template>
  <div>
    <div v-if="movieList.seenMovie === true">
      <li><del>{{ movieList.title }}</del></li>  
      <b-button variant="outline-primary" @click="deleteMovieList">check</b-button>
      <b-button variant="outline-secondary" @click="deleteMovie">delete</b-button>
    </div>
    <div v-else>
      <li>{{ movieList.title }}</li>  
      <b-button variant="outline-primary" @click="deleteMovieList">check</b-button>
    </div>

  </div>
</template>

<script>
export default {
  name: 'MyList',
  props: {
    movieList: Object,
  },
  methods: {
    deleteMovieList() {
      this.$emit('deleteMovieList', this.movieList)
    },
    deleteMovie() {
      this.$emit('ondeleteMovie', this.movieList)
    }
  }
}
</script>

<style>

</style>
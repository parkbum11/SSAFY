<template>
  <b-form>
    <b-form-input class="form-control" type="text" placeholder="Enter Movie Title" @keyup.enter="onMovieDataChange" v-model="movieInput"></b-form-input>
    <b-button inline variant="success" @click="onMovieDataChange">add</b-button>
  </b-form>
</template>

<script>
export default {
  data() {
    return {
      movieInput: '',
    }
  },
  methods: {
    onMovieDataChange() {
      this.$emit('onMovieDataChange', this.movieInput)
      this.movieInput = ''
    }
  }
}
</script>

<style>
.input {
  width: 5px;
}
</style>
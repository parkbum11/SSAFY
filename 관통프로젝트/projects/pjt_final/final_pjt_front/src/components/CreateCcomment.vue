<template>
  <div class="container">
    <br>
    <b-input-group>
    <b-form-input @keyup.enter="createCcomment" type="text"></b-form-input>

    <b-input-group-append>
      <b-button @click="onChangeCcommentStatus" type="button" variant="secondary">취소</b-button>
    </b-input-group-append>
  </b-input-group>

  </div>
</template>

<script>
// import axios from 'axios'
export default {
  name: 'CreateCcomment',
  methods: {
    createCcomment(event) {
      this.$emit('onCreateCcomment', event.target.value)
    },
    onChangeCcommentStatus() {
      this.$emit('onChangeCcommentStatus')
    }
  }
}
</script>

<style>

</style>
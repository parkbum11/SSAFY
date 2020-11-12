<template>
  <div v-if="this.selectVideo.id">
    <iframe :src="videoSrc" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  props: {
    selectVideo:Object
  },
  computed: {
    videoSrc() {
      return `https://www.youtube.com/embed/${this.selectVideo.id.videoId}`
    } 
  }
}
</script>

<style>

</style>
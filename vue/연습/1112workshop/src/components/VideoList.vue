<template>
  <div>
    <ul>
      <VideoItem
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
        @getVideo="getVideo"
      />
    </ul>
    
  </div>
</template>

<script>
import VideoItem from '@/components/VideoItem.vue'
export default {
  components:{
    VideoItem,
  },
  props:{
    videos:Array
  },
  methods: {
    getVideo(selectVideo) {
      this.$emit('getVideo', selectVideo)
    }
  }
}
</script>

<style>

</style>
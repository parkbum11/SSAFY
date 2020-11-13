<template>
  <div v-if="video">
    <iframe :src="videoURI" frameborder="0"></iframe>
    <h2>{{ video.snippet.title | stringUnescape }}</h2>
    <p>{{ video.snippet.description | stringUnescape }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail', 
  // (17). 부모 컴포넌트로부터 내려온 video 데이터를 받아서 해당 컴포넌트 안에서 활용한다.
  props: {
    video: [Object, String],
  },
  computed: {
    videoURI: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

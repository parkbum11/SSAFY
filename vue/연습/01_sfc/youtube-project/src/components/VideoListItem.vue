<template>
<!-- (10). li 태그(아이템)을 클릭하면 -->
  <li @click="selectVideo">
    <img :src="youtubeImageSrc" alt="">
    <!-- <span v-html="video.snippet.title"></span> -->
    {{ video.snippet.title | stringUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem', 
  // (9). 부모 컴포넌트(VideoList)로부터 내려온 데이터를 받아서 활용한다.
  props: {
    video: Object,
  },
  methods: {
    // (11). select-video라는 이벤트와 함께 해당 video 데이터를 부모 컴포넌트로 올려준다.
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  },
  // 특정 data를 조작(변경)하지 않고 필터링 하거나 어떤 값(ex. 이미지)만 뽑아서 사용하고 싶은 경우에 활용한다.
  // return 된 값을 사용하며 직접 호출(괄호를 열고 닫는 행위)하지 않는다. 
  // 값이 같으면 캐싱된 값을 사용한다.
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      console.log(rawText)
      return _.unescape(rawText)
    }
  }
}
</script>

<template>
  <div>
    <ul>
      <!-- 3. 보여준다. -->
      <!-- (8). 부모 컴포넌트(App)로부터 내려온 데이터를 반복을 돌며 다시 자식 컴포넌트로 내려준다. -->
      <!-- (12). 자식 컴포넌트(VideoListItem)로부터 올라온 이벤트를 듣고 있다가 onVideoSelect 메서드를 실행한다. -->
      <VideoListItem 
        v-for="(video, idx) in videos" 
        :key="idx"
        :video="video"
        @select-video="onVideoSelect"
      />
    </ul>
  </div>
</template>

<script>
// @ -> src/
//1. 불러온다.
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList', 
  components: {
    //2. 등록한다.
    VideoListItem,
  },
  props: {
    // props는 내려오는 데이터의 타입을 지정할 수 있다.(일종의 validation -> 다르면 콘솔 창에 에러 메시지가 나온다.)
    videos: Array,
  },
  methods: {
    // (13). 메서드가 실행되면 올라온 데이터와 함께 select-video라는 이벤트를 다시 부모 컴포넌트(App)로 올려준다.
    onVideoSelect: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

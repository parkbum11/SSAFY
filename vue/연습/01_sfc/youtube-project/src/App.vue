<template>
  <div class="container">
    <h1>My First Youtube Project</h1>
    <!-- 3.보여준다. -->
    <SearchBar @input-change="onInputChange" />
    <!-- (16). selectedVideo 데이터를 video라는 이름으로 자식 컴포넌트(videoDetail)로 내려준다. -->
    <VideoDetail :video="selectedVideo" />
    <!-- (7). :videos="videos" 응답 받은 배열(비디오 목록)을 VideoList 컴포넌트로 내려준다. -->
    <!-- (14). 자식 컴포넌트로부터 select-video 이벤트가 올라오면 onVideoSelect 메서드를 실행한다. -->
    <VideoList :videos="videos" @select-video="onVideoSelect"/>
  </div>
</template>

<script>
import axios from 'axios'

//1. 불러온다.
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'


export default {
  name: 'App',
  components: {
    // ES6 Object 축약 문법
    // SearchBar: SearchBar, 
    //2. 등록한다.
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      inputValue: '',
      selectedVideo: '',
      videos: [],
    }
  },
  methods: {
    onInputChange: function (inputText) {
      // console.log('데이터가 SearchBar로부터 올라왔다!!!!')
      // console.log(inputText)

      //(3). 자식 컴포넌트(SearchBar.vue)로부터 올라온 데이터 inputValue라는 App.vue 컴포넌트 데이터에 넣는다.
      this.inputValue = inputText

      //(4). Youtube API로 요청을 위한 준비를 한다.
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      //(5). Youtube로 axios를 활용해 요청을 보낸다.
      // Axios는 Promise 객체를 return
      axios.get(API_URL, {
        // params: params, ES6 Object 축약 문법
        params,
      })
      .then((res) => {
        console.log(res)
        console.log(res.data.items)
      
        //(6). Youtube로부터 응답 받은 영상 목록(배열)을 배열에 넣는다.
        this.videos = res.data.items
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // (15). 메서드가 실행되면 자식 컴포넌트로부터 올라온 video 데이터를 App 컴포넌트의 selectedVideo 데이터에 넣는다.
    onVideoSelect: function (video) {
      this.selectedVideo = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

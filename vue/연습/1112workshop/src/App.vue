<template>
  <div id="app">
    <SearchBar 
      :userInput="userInput"
      @changeUserInput="onChangeUserInput"
    />
    <VideoList :videos="videos" @getVideo="getVideo"/>
    <VideoDetail :selectVideo="selectVideo"/>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'
import axios from 'axios'
export default {
  name: 'App',
  components: {
    SearchBar,
    VideoDetail,
    VideoList
  },
  data(){
    return {
      userInput:'',
      videos: [],
      videoIndex: 0,
      selectVideo: {},
    }
  },
  methods:{
    onChangeUserInput(input){
      this.userInput=input
      //유튜브 영상 검색하는 API 사용
      const API_URI='https://www.googleapis.com/youtube/v3/search'
      const API_KEY='AIzaSyC7Fd8ss-vFCa7x3vv4Wagdo9x0upKNjQ8'
      if(this.userInput==='') return
      axios({
        url:API_URI,
        method:'GET',
        params:{
          key:API_KEY,
          part:'snippet',
          type:'video',
          q:this.userInput,
        }
      }).then(res=>{
        this.videos=res.data.items
      }).catch(err=>{
        console.log(err)
      })
    },
    getVideo: function(selectVideo) {
      this.selectVideo = selectVideo
    },
  },
  watch:{
    userInput(value){
      console.log(value)
      if(value === 'bad'){
        this.userInput=''
        alert('말조심!')
      }
    }
  }
}
</script>

<style>
</style>
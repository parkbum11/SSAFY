<template>
<div class="contain">
  <div class="stylingbg container">
    <p class='h1 text-monospace text-center'>Review</p><br><br>

    <p class="h4">별점을 선택해주세요</p><br>
    <div class="score">
      <b-form-rating variant="danger" v-model="movieScore" inline size="lg"></b-form-rating>
      <p class="mt-1 ml-3 h2 text-danger">  {{ movieScore*2 }}</p>
    </div><br><br>

    <p class="h4">제목</p><br>
    <b-input type="text" size="lg" v-model="title" placeholder="최대 50자"></b-input><br><br>

    <p class="h4">내용</p><br>
    <b-textarea v-model="content" rows="8" placeholder="최대 300자"></b-textarea>
    <br>

    <div>
      <b-button @click="createComment" variant="success">만들기</b-button>   
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name: 'CreateComment',
  data() {
    return {
      movieScore: 0,
      title: '',
      content: '',
    }
  },
  computed: {
    ...mapState(['movieId']),
  },
  methods: {
    createComment() {
      this.movieScore = this.movieScore*2
      axios ({
        method: 'POST',
        url: `http://127.0.0.1:8000/comments/${this.movieId}/`,
        data: { title: this.title, content: this.content, score: this.movieScore },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then((res) => {
        this.$store.commit('CTEATE_COMMENT_STATUS', res.data)
        this.$router.push('/movieDetail')
        console.log(res.data)
      }).catch((err) => {
        console.log(err)
      })
    } 
  },
}
</script>

<style>
.contain {
  background-image: 
    linear-gradient( 
    rgba(0, 0, 0, 0.55), 
    rgba(0, 0, 0, 0.55) ), 
      url('https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80');
  opacity: 0.9;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  background-attachment: fixed;
} 
.stylingbg {
  background-color: #141414;
  color: white;
  margin-top: 100px;
  margin-bottom: 50px;
  margin-left: 200px;
  margin-right: 200px;
}
.score {
  display: flex;
}
</style>
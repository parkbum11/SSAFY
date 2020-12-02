<template>
  <div>
    <br>
    <div class="mb-5">
      <div class="mb-2">
        <div class="d-flex bd-highlight mb-2 text-light">
          <span class="h4 p-2 bd-highlight"> {{ comment.title }} </span>
          <span class="text-secondary title my-auto p-2 bd-highlight"> {{ comment.username }} </span> 
          <span class="text-secondary my-auto"> | </span>
          <span class="text-secondary my-auto">{{ comment.created_at.slice(0,10) }} {{ comment.created_at.slice(11,19) }} |  </span>
          <span class="text-secondary mr-auto my-auto"></span>
          <span class="p-2 bd-highligh h5">{{ comment.score }}</span>
          <div v-if="comment.score === 10" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
          </div>
          <div v-else-if="comment.score === 8" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="comment.score === 6" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="comment.score === 4" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="comment.score === 2" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="comment.score === 0" class='p-2 bd-highligh h5'>            
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
        </div>
        <div class='text-monospace text-secondary m-1 text-light' v-if="comment.content.length >= 30">
          {{ comment.content.slice(0,100) }}...
        </div>
        <div  class='text-monospace text-secondary m-2 text-light' v-else>
          {{ comment.content }}
        </div>

        <div class='p-2 bd-highligh h5'>
          <span class="text-primary mr-3">{{ comment.like_users.length }}</span>
          <button @click="ChangeCommentLike(id)" v-if="userid in comment.like_users">
            <span class="mr-4"><i class="fas fa-thumbs-up" style="color: Dodgerblue"></i></span>
          </button>
          <button @click="ChangeCommentLike(id)" v-else>
            <span class="mr-4"><i class="far fa-thumbs-up" style="color: Dodgerblue"></i></span>
          </button>
          <span class="text-danger mr-3">{{ comment.hate_users.length }}</span>
          <button @click="ChangeCommentHate(id)" v-if="userid in comment.hate_users">
            <span class="mr-4"><i class="fas fa-thumbs-down" style="color: red"></i></span>
          </button>
          <button @click="ChangeCommentHate(id)" v-else>
            <span class="mr-4"><i class="far fa-thumbs-down" style="color: red"></i></span>
          </button>
          <span class="mr-3" @click="createCcommentStatus">댓글</span>

          <b-button style="float: right;" v-if="username === comment.username" @click="commentDelete" variant="danger" class="ml-2">삭제</b-button>
          <b-button style="float: right;" v-if="username === comment.username" @click="commentUpdate" variant="secondary" class="text-right ml-2">수정</b-button>
          <br>

          <CreateCcomment 
            v-if="ccommentCreateStatus" 
            @onCreateCcomment="createCcomment"
            @onChangeCcommentStatus="createCcommentStatus"
          />
          <br>

          <div v-if="ccommentStatus" @click="lookCcomments">
            <div v-if="comment.co_comment.length" class="title"><i class="fas fa-angle-up"></i> 댓글 {{ comment.co_comment.length }}개 숨기기</div>
            <div v-else class="title"><i class="fas fa-angle-up"></i> 댓글 숨기기</div>
            <div v-for="(ccomment, id) in comment.co_comment" :key="id">
              <br>
              <span class="p bd-highlight"> {{ ccomment.username }} 님의 댓글 </span> 
              <span class="text-secondary">{{ ccomment.created_at.slice(0,10) }} {{ ccomment.created_at.slice(11,19) }} |  </span>
              <b-button v-if="username === ccomment.username" @click="ccommentDelete(ccomment.id)" style="float: right;" variant="danger" class="ml-2">삭제</b-button>
              <div  class='text-monospace text-secondary m-2 text-light'>
                {{ ccomment.content }}
              </div>
            </div>
          </div>
          <div v-else @click="lookCcomments">
            <div v-if="comment.co_comment.length" class="title"><i class="fas fa-angle-down"></i> 댓글 {{ comment.co_comment.length }}개 보기</div>
            <div v-else class="title"><i class="fas fa-angle-down"></i> 댓글 보기</div>
          </div>
        </div>

        <hr id="hr1">
      </div>
    </div> 
  </div>
</template>

<script>
import CreateCcomment from '../components/CreateCcomment.vue'
import { mapState, mapActions } from 'vuex'
import jwt_decode from 'jwt-decode'
import axios from 'axios'

export default {
  name: 'ReviewList',
  components: { CreateCcomment },
  props: {
    comment: Object,
    id: Number
  },
  data() {
    return {
      userid: '',
      username: '',
      ccommentStatus: false,
      ccommentCreateStatus: false,
      ccommentContent: '',
    }
  },
  computed: {
    ...mapState(['movieDetail', 'movieId'])
  },
  methods: {
    ...mapActions(['ChangeCommentLike', 'ChangeCommentHate']),
    lookCcomments() {
      this.ccommentStatus = !this.ccommentStatus
    },
    createCcommentStatus() {
      this.ccommentCreateStatus = !this.ccommentCreateStatus
    },
    createCcomment(ccomment) {
      this.ccommentContent = ccomment
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/comments/${this.movieId}/${this.comment.id}/comment/`,
        data: { content: this.ccommentContent },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then((res) => {
        this.$store.commit('CTEATE_COMMENT', res.data)
        this.ccommentCreateStatus = false
        this.ccommentStatus = true
      }).catch((err) => {
        console.log(err)
      })
    },
    commentDelete() {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/comments/${this.movieId}/${this.comment.id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then((res) => {
        this.$store.commit('COMMENT_DELETE', res.data)
      }).catch((err) => {
        console.log(err)
      })
    },
    commentUpdate() {
      this.$store.commit('COMMENT_UPDATE', this.comment.id)
      this.$router.push('/updatecomment')
    },
    ccommentDelete(ccomment_id) {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/comments/${this.movieId}/${this.comment.id}/comment/${ccomment_id}`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then((res) => {
        this.$store.commit('CCOMMENT_DELETE', res.data)
        this.ccommentStatus = true
      }).catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    const token = localStorage.getItem('jwt')
    this.userid = jwt_decode(token).user_id
    this.username=jwt_decode(token).username
  }
}
</script>

<style>
.title:hover {
  cursor: pointer;
  color: red;
}
hr#hr1 {
  border-top: 1px dashed #8c8b8b;
  border-bottom: 1px dashed #fff;
}
.right-box {
  float: right;
}
</style>
<template>
<div class="contain">
  <div class="stylingbg">
    <div class="container mt-4">
      <div v-if="videoStatus">
        <span class="h2 mr-2">{{ movieDetail.title }}  </span>
        <button v-if="movieDetail.video_path" movieDetail.video_path style="float:;" type="button" class="btn" @click="videoOn">
          <i class="fas fa-pause fa-2x" style="color:red"></i>
        </button>
        <span class="mr-auto text-right">예고편 닫기</span>
        <br>
        <iframe :src="movieDetail.video_path" frameBorder="0" style="display:block; width:100%; height: 75vh"></iframe>
      </div>
      <div v-else>
        <span class="h2 mr-2">{{ movieDetail.title }}  </span>
        <span v-if="movieDetail.video_path">
          <button movieDetail.video_path style="float:;" type="button" class="btn" @click="videoOn">
            <i class="fas fa-play fa-2x" style="color:red"></i>
          </button>
          <span class="mr-auto text-right">예고편 보기</span>
        </span>
      </div>
      <br>

      <br><br>

      <div class="d-flex justify-content-between bd-highlight mb-3 p-0 m-0">
        <div class="mr-auto p-2 bd-highlight">
          <span class="h4 mr-2">The Movie 평점</span>

          <span v-if="9 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
          </span>
          <span v-else-if="8 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star-half-alt" style="color:red"></i>
          </span>
          <span v-else-if="7 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else-if="6 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star-half-alt" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else-if="5 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else-if="4 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star-half-alt" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else-if="3 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else-if="2 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star-half-alt" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else-if="1 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else-if="0 < movieDetail.comment_score_average" class='h5 mr-2'>
            <i class="fas fa-star-half-alt" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else class='h5 mr-2'>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>

          <p class="badge badge-success"> {{ movieDetail.comment_score_average }}</p>
          <br>

          <span class="h5 mr-3">개요</span>
          <span class="text-monospace text-white">{{ nations[movieDetail.nation] }}</span>
          <span class="text-white-50"> | </span>
          <span class="text-monospace text-white">{{ movieDetail.release_date }} 개봉</span>
          <br>

          <span class="h5 mr-3">평점</span>
          <span class="text-monospace text-white">{{ movieDetail.vote_average }}</span>
          <br>

          <span class="h5 mr-3">장르</span>
          <span 
            v-for="(genres, id) in movieDetail.genres" 
            :key="id"
            class="text-monospace text-white"
            >
            {{ genres.name }}
            <span class="text-white-50"> | </span>
            </span>
          <br>
          <div class="my-4 h5">줄거리</div>
          <p class="text-monospace">{{ movieDetail.overview }}</p>

          <div class="text-center">
            <p class="h5 mt-5 mb-3">스트리밍</p>
            <a href="https://www.youtube.com/feed/storefront?bp=ogUCKAI%3D" class='mr-4'><img src="https://image.flaticon.com/icons/svg/1384/1384060.svg" alt="" style="height: 40px"></a>
            <a href="https://www.netflix.com/kr/" class="mr-4"><img src="https://www.flaticon.com/premium-icon/icons/svg/2504/2504929.svg" alt="" style="height: 40px"></a>
            <a href="https://serieson.naver.com/movie/home.nhn"><img src="https://www.naver.com/favicon.ico" alt="" style="height: 40px"></a>
          </div>

          <div v-if="likedStatus" class="text-right mt-4 mr-4 heart">
            <button @click="heartStatusChange">
              <i class="fas fa-heart mt-1 fa-2x" style="color:red"></i>
            </button>
            <span class="ml-2 h4">{{ movieDetail.like_users.length }}</span>
            <span class="ml-2 h4">찜하기</span>
          </div>
          <div v-else class="text-right mt-4 mr-4 heart" >
            <button @click="heartStatusChange">
              <i class="far fa-heart mt-1 fa-2x" style="color:red"></i>
            </button>
            <span class="ml-2 h4">{{ movieDetail.like_users.length }}</span>
            <span class="ml-2 h4">찜하기</span>
          </div>
          
        </div>
        <img :src="movieDetail.poster_path" alt="No Poster" class="w-50 bd-highlight">
      </div>
      <br>

      <!-- 등장인물 -->
      <div>
        <div class="mb-3">
          <span class='h4 text-monoscope text-white'>등장인물</span>
        </div>
        <vueper-slides
          class="no-shadow"
          :touchable="false"
          :visible-slides="6"
          :slide-ratio="1 / 4"
          :gap="1"
          :bullets='true'
          :slideMultiple='true'
          :dragging-distance="70">
          <vueper-slide v-for="(actor, i) in movieDetail.actors" :key="i" :image="actor.profile_path"/>
        </vueper-slides>
      </div>
      <!-- 등장인물 엔드 -->

      <hr style="border:solid 1px white;">
      <div class="text-right text-white">
        <button style="float: right;" @click="$router.push('/createcomment')" class="btn btn-secondary">리뷰 작성하기</button>
      </div>
      <div style="float: left;" class="h3 mr-3">The Movie 리뷰</div>
      <div style="float: left;" class="mt-1">
        <b-form-checkbox v-model="onlyMyComment" name="check-button" switch>내 리뷰 보기</b-form-checkbox>
      </div>
      <br><br>
      <div v-if="onlyMyComment">
        <ReviewList 
          v-for="(comment, id) in MyComment"
          :key="id"
          :comment="comment"
          :id="id"
        />
      </div>
      <div v-else>
        <ReviewList 
          v-for="(comment, id) in movieDetail.comments"
          :key="id"
          :comment="comment"
          :id="id"
        />
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import ReviewList from '../components/ReviewList.vue'
import { mapState, mapActions } from 'vuex'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
// import axios from 'axios'
import jwt_decode from 'jwt-decode'

export default {
  name: 'MovieDetail',
  components: { ReviewList, VueperSlides, VueperSlide },
  data() {
    return {
      userid: '',
      username: '',
      onlyMyComment: false,
      videoStatus: false,
      nations: {
        'pl': '폴란드',
        'de': '독일',
        'sv': '스웨덴',
        'ko': '한국',
        'es': '스페인',
        'it': '이탈리아',
        'no': '노르웨이',
        'zh': '중국',
        'fr': '프랑스',
        'ru': '러시아',
        'en': '미국/영국',
        'ja': '일본',
        'hi': '인도',
      }
    }
  },
  methods: {
    ...mapActions(['heartStatusChange']),
    videoOn() {
      this.videoStatus = !this.videoStatus
    }
  },

  computed: {
    ...mapState(['movieDetail', 'likedStatus', 'star']),
    MyComment(){
      return this.$store.state.movieDetail.comments.filter((comment)=>{
        return comment.username===this.username
      })
    },
  },
  created() {
    const token = localStorage.getItem('jwt')
    this.userid = jwt_decode(token).user_id
    this.username=jwt_decode(token).username
  }
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
  background-color: transparent !important;
  color: white;
  margin-top: 100px;
  margin-bottom: 50px;
  margin-left: 200px;
  margin-right: 200px;
}


</style>
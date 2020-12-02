<template>
  <div class="out contain" id="styling">
    <form @submit="signup">
      <vueper-slides class="in" :touchable="false" :bullets="false" :arrows="false" ref="first" style="width: 1500px; display: inline-block">
        <vueper-slide :key="1">
          <template v-slot:content>
            <div style="width: 25%; margin:auto">
              <h1>Sign Up</h1><br>

              <div class="form-group">
                <label>Name</label>
                <input v-model="username" placeholder="2자 이상" type="text" style="margin:auto;" class="form-control form-control-lg" />
              </div>

              <div class="form-group">
                <label>Email Address</label>
                <input v-model="email" placeholder="example@gmail.com" style="margin:auto;" type="email" class="form-control form-control-lg" />
              </div>
              
              <div class="form-group">
                <label>Password</label>
                <input v-model="password"  @keyup.enter="$refs.first.next()" min="1" placeholder="6자 이상" type="password" style="margin:auto;" class="form-control form-control-lg" />
              </div>

              <button type="button" @click="$refs.first.next()" class="btn btn-primary btn-lg btn-block" style="margin-top:10px">Next</button>
            </div>
          </template>
        </vueper-slide>
        <vueper-slide :key="2">
          <template v-slot:content>
            <div style="width: 25%; margin:auto">
              <h1>Sign Up</h1><br>

              <div class="form-group">
                <label>Nation</label>
                <b-form-select v-model="nation" :options="options" class="form-control form-control-lg"></b-form-select>
              </div>

              <div class="form-group">
                <label>Age</label>
                <input v-model="age" style="margin:auto;" type="number" class="form-control form-control-lg" />
              </div>

              <div class="form-group">
                <label>Gender</label>
                <br>
                <b-button-group>
                  <b-button @click="changeToMale" variant="success">Male</b-button>
                  <b-button @click="changeToFemale" variant="success">Female</b-button>
                </b-button-group>
              </div>

              <button type="button" @click="$refs.first.next()" @keypress.enter="$refs.first.next()" class="btn btn-primary btn-lg btn-block" style="margin-top:10px">Next</button>
              <button type="button" @click="$refs.first.previous()" class="btn btn-dark btn-lg btn-block" style="margin-top:10px">Back</button>
            </div>
          </template>
        </vueper-slide>
        <vueper-slide :key="3">
          <template v-slot:content>
            <div style="width: 40%; margin:auto">
              <h1>Sign Up</h1><br>

              <label>좋아 하는 장르</label>
              <div>
                <div v-if="isLikedHorror" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedHorror">공포</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedHorror">공포</b-button>
                </div>

                <div v-if="isLikedThriller" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedThriller">스릴러</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedThriller">스릴러</b-button>
                </div>

                <div v-if="isLikedCriminal" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedCriminal">범죄</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedCriminal">범죄</b-button>
                </div>

                <div v-if="isLikedMistery" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedMistery">미스터리</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedMistery">미스터리</b-button>
                </div>
              </div>
              
              <div>
                <div v-if="isLikedComedy" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedComedy">코미디</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedComedy">코미디</b-button>
                </div>

                <div v-if="isLikedRomance" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedRomance">로맨스</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedRomance">로맨스</b-button>
                </div>

                <div v-if="isLikedDrama" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedDrama">드라마</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedDrama">드라마</b-button>
                </div>

                <div v-if="isLikedMusic" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedMusic">음악</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedMusic">음악</b-button>
                </div>
              </div>

              <div>
                <div v-if="isLikedWar" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedWar">전쟁</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedWar">전쟁</b-button>
                </div>

                <div v-if="isLikedSf" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedSf">SF</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedSf">SF</b-button>
                </div>

                <div v-if="isLikedAdventure" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedAdventure">모험</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedAdventure">모험</b-button>
                </div>

                <div v-if="isLikedAction" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedAction">액션</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedAction">액션</b-button>
                </div>
              </div>

              <div>
                <div v-if="isLikedFantasy" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedFantasy">판타지</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedFantasy">판타지</b-button>
                </div>

                <div v-if="isLikedHistory" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedHistory">역사</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedHistory">역사</b-button>
                </div>

                <div v-if="isLikedDocumentary" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedDocumentary">다큐</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedDocumentary">다큐</b-button>
                </div>

                <div v-if="isLikedAnimation" style="float: left; width: 25%;" class="container">
                  <b-button variant="dark" block @click="changeLikedAnimation">애니매이션</b-button>
                </div>
                <div v-else style="float: left; width: 25%;" class="container">
                  <b-button variant="light" block @click="changeLikedAnimation">애니매이션</b-button>
                </div>
              </div>
              <div class="contanier">
              <button type="submit" class="btn btn-primary btn-lg btn-block" style="margin-top:10px">Sign Up</button>
              <button type="button" @click="$refs.first.previous()" class="btn btn-dark btn-lg btn-block" style="margin-top:10px">Back</button>
              </div>
            </div>
          </template>
        </vueper-slide>
      </vueper-slides>
    </form>
  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
import axios from 'axios'
import Swal from 'sweetalert2'

export default {
  components: { VueperSlides, VueperSlide },
  data() {
    return { 
      options: [
        { value: 'pl', text: '폴란드' },
        { value: 'de', text: '독일' },
        { value: 'sv', text: '스웨덴' },
        { value: 'ko', text: '한국' },
        { value: 'es', text: '스페인' },
        { value: 'it', text: '이탈리아' },
        { value: 'no', text: '노르웨이' },
        { value: 'zh', text: '중국' },
        { value: 'fr', text: '프랑스' },
        { value: 'ru', text: '러시아' },
        { value: 'en', text: '미국/영국' },
        { value: 'ja', text: '일본' },
        { value: 'hi', text: '인도' },
      ],
      username: '', 
      email: '', 
      password: '', 
      age: 0, 
      nation: '', 
      gender: '',
      isLikedAnimation: false,
      isLikedComedy: false,
      isLikedRomance: false,
      isLikedMusic: false,
      isLikedDrama: false,
      isLikedHorror: false,
      isLikedThriller: false,
      isLikedCriminal: false,
      isLikedMistery: false,
      isLikedSf: false,      
      isLikedWar: false,      
      isLikedAdventure: false,      
      isLikedFantasy: false,      
      isLikedAction: false,      
      isLikedHistory: false,      
      isLikedDocumentary: false,    
    }
  },
  methods: {
    signup(event) {
      event.preventDefault()
      axios({
        url: 'http://127.0.0.1:8000/accounts/signup/',
        method: 'POST',
        data: {
          username: this.username,
          email: this.email,
          password: this.password,
          age: this.age,
          nation: this.nation,
          gender: this.gender,
          isLikedAnimation: this.isLikedAnimation,
          isLikedComedy: this.isLikedComedy,
          isLikedRomance: this.isLikedRomance,
          isLikedMusic: this.isLikedMusic,
          isLikedDrama: this.isLikedDrama,
          isLikedHorror: this.isLikedHorror,
          isLikedThriller: this.isLikedThriller,
          isLikedCriminal: this.isLikedCriminal,
          isLikedMistery: this.isLikedMistery,
          isLikedSf: this.isLikedSf,
          isLikedWar: this.isLikedWar,
          isLikedAdventure: this.isLikedAdventure,
          isLikedFantasy: this.isLikedFantasy,
          isLikedAction: this.isLikedAction,
          isLikedHistory: this.isLikedHistory,
          isLikedDocumentary: this.isLikedDocumentary,
        },
      }).then(()=>{
        Swal.fire({
          title: `The Movie의 회원이 되신걸 \n 축하 드립니다!`,
          text: '',
          icon: 'success',
          confirmButtonText: '확인'
        })
        this.$router.push('/login')
      }).catch(()=>{
        if (this.username == '') {
          Swal.fire({
            title: 'Error',
            text: '아이디를 입력해주세요',
            icon: 'error',
            confirmButtonText: '취소'
          })
        } else if (this.email == '') {
          Swal.fire({
            title: 'Error',
            text: '이메일을 입력해주세요',
            icon: 'error',
            confirmButtonText: '취소'
          })
        } else if (this.password == '') {
          Swal.fire({
            title: 'Error',
            text: '비밀번호를 입력해주세요',
            icon: 'error',
            confirmButtonText: '취소'
          })
        } else if (this.age == 0) {
          Swal.fire({
            title: 'Error',
            text: '나이를 입력해주세요',
            icon: 'error',
            confirmButtonText: '취소'
          })
        } else if (this.nation == '') {
          Swal.fire({
            title: 'Error',
            text: '국적을 선택해주세요',
            icon: 'error',
            confirmButtonText: '취소'
          })
        } else if (this.gender == '') {
          Swal.fire({
            title: 'Error',
            text: '성별을 선택해주세요',
            icon: 'error',
            confirmButtonText: '취소'
          })
        }
      })
    },
    changeToMale() { this.gender = 'male' },
    changeToFemale() { this.gender = 'female' },
    changeLikedHorror() { this.isLikedHorror = !this.isLikedHorror },
    changeLikedThriller() { this.isLikedThriller = !this.isLikedThriller },
    changeLikedCriminal() { this.isLikedCriminal = !this.isLikedCriminal },
    changeLikedMistery() { this.isLikedMistery = !this.isLikedMistery },
    changeLikedComedy() { this.isLikedComedy = !this.isLikedComedy },
    changeLikedRomance() { this.isLikedRomance = !this.isLikedRomance },
    changeLikedDrama() { this.isLikedDrama = !this.isLikedDrama },
    changeLikedMusic() { this.isLikedMusic = !this.isLikedMusic },
    changeLikedWar() { this.isLikedWar = !this.isLikedWar },
    changeLikedSf() { this.isLikedSf = !this.isLikedSf },
    changeLikedAdventure() { this.isLikedAdventure = !this.isLikedAdventure },
    changeLikedAction() { this.isLikedAction = !this.isLikedAction },
    changeLikedFantasy() { this.isLikedFantasy = !this.isLikedFantasy },
    changeLikedHistory() { this.isLikedHistory = !this.isLikedHistory },
    changeLikedDocumentary() { this.isLikedDocumentary = !this.isLikedDocumentary },
    changeLikedAnimation() { this.isLikedAnimation = !this.isLikedAnimation },
  }
}
</script>

<style>
#styling {
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
}

form {
  color: white;
}

.contain {
  background-image: 
    linear-gradient( 
    rgba(0, 0, 0, 0.55), 
    rgba(0, 0, 0, 0.55) ), 
      url('https://images.unsplash.com/photo-1524712245354-2c4e5e7121c0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80');
      /* '../assets/logo.png' */
  opacity: 0.9;
  background-size: cover;
}

</style>
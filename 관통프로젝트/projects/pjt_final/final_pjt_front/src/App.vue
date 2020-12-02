<template>
  <div class="appbg">
    <b-navbar toggleable="lg" type="dark" variant="" class="navbar fixed-top" >
      <b-navbar-brand href="/">
        <img src="./assets/movielogo.png" width="120" height="40">
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/"><span class="text-white">홈</span></b-nav-item>
          <b-nav-item href="/mylikedmovies"><span class="text-white">내가 찜한 영화</span></b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto mt-2" >
          <div class="" data-app="true">
            <v-autocomplete
              class="white--text"
              :items="items"
              :search-input.sync="search"
              v-model="select"
              cache-items
              flat
              dense
              rounded
              filled
              hide-no-data
              solo
              label="영화를 검색하세요."
              @keyup.enter="goMovieDetailBySearch"
            >
            <!-- <template v-slot:no-data>
              <v-list-item>
                <v-list-item-title>
                  는 존재하지 않는 영화입니다.
                </v-list-item-title>
              </v-list-item>
            </template> -->
            </v-autocomplete>
          </div>
          <!-- <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">ES</b-dropdown-item>
            <b-dropdown-item href="#">RU</b-dropdown-item>
            <b-dropdown-item href="#">FA</b-dropdown-item>
          </b-nav-item-dropdown> -->
          <b-nav-item v-if="username===''" href="/login" right class="">
            <span class="text-white"><i class="fas fa-door-open fa-fw"></i>&nbsp; 로그인</span>
          </b-nav-item>
          <b-nav-item v-else @click="logout" right class="">
            <span class="text-white"><i class="fas fa-door-closed fa-fw"></i>&nbsp; 로그아웃</span>
          </b-nav-item>
          <b-nav-item  v-if="username===''" href="/signup" right class="">
            <span class="text-white"><i class="fas fa-address-card fa-fw"></i>&nbsp; 회원가입</span>
          </b-nav-item>
          <b-nav-item  v-else href="/mylikedmovies" right class="">
            <span class="text-white"><i class="fas fa-user-circle"></i>&nbsp; {{username}}</span>
          </b-nav-item>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!-- 임시1 -->
    <!-- <div class="appstyling"><router-view></router-view></div> -->
    <router-view></router-view>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import title from '@/assets/title.json'
export default {
  data: function () {
    return {
      items: [],
      search: null,
      select: null,
      searchInfo: title,
    }
  },
  watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val);
    },
  },
  computed: {
    ...mapState(['username']),
  },
  methods: {
    querySelections(v) {
      setTimeout(() => {
        this.items = this.searchInfo.title.filter(e => {
          return (e || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1;
        });
      }, 500);
    },
    
    logout() {
      localStorage.removeItem('jwt')
      this.$store.commit('DELETE_USERNAME')
      this.$router.push('/login')
    },
    goMovieDetailBySearch(){
      for (let index = 0; index < this.searchInfo.title.length; index++) {
        if(this.select==this.searchInfo.title[index]){
          axios ({
            method: 'GET',
            url: `http://127.0.0.1:8000/movies/detail/${this.searchInfo.m_id[index]}/`,
            headers: {
              Authorization: `JWT ${localStorage.getItem('jwt')}`
            },
          })
          .then((res) => {
              const searchMovie = res.data
              console.log(searchMovie)
              this.$store.dispatch('goMovieDetail', searchMovie)
              this.$router.push('/movieDetail')
              // console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
        }
      }
    }
  },
}
</script>
  
<style>
/* 임시2 */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&display=swap');
.appstyling {
  background-color: black;
  margin-top: 5px;
}
.appbg {
  font-family: 'Noto Sans KR', sans-serif;
  height: 100vh;
  width: 100vw;
  overflow-y: scroll;
  background-color: #141414;
}
</style>

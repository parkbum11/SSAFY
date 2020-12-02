import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'
// import { for } from 'core-js/fn/symbol'
// import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movieDetail: {},
    // star:null,
    likedStatus: false,
    movieId: 0,
    commentId: null,
    username: '',
    userid: null,
  },
  mutations: {
    GO_MOVIE_DETAIL: function (state, movie) {
      state.movieDetail = movie
      // state.star=movie.comment_score_average/2
      state.likedStatus = false
      state.movieId = movie.m_id
      state.commentId = null
      for (let i = 0; i < movie.like_users.length; i++) {
        if (movie.like_users[i] == state.userid) {
          state.likedStatus = true
        }
      }
      console.log(state.movieDetail)
    },
    HEART_STATUS_CHANGE: function(state, movie) {
      state.movieDetail = movie
      state.likedStatus = !state.likedStatus
    },
    CHANGE_COMMENT_LIKE: function(state, movie) {
      state.movieDetail = movie
    },
    CHANGE_COMMENT_HATE: function(state, movie) {
      state.movieDetail = movie
    },
    CTEATE_COMMENT_STATUS: function(state, movie){
      state.movieDetail = movie
    },
    CTEATE_COMMENT: function(state, movie){
      state.movieDetail = movie
      // state.star=movie.comment_score_average/2
    },
    COMMENT_DELETE: function(state, movie){
      state.movieDetail = movie
      // state.star=movie.comment_score_average/2
    },
    COMMENT_UPDATE: function(state, comId){
      state.commentId = comId
    },
    CCOMMENT_DELETE: function(state, movie){
      state.movieDetail = movie
    },
    USER_NAME: function(state, userName) {
      state.username = userName
    },
    DELETE_USERNAME: function(state) {
      state.username = ''
    },
    USER_INFO: function(state, userid) {
      state.userid = userid
    }
  },
  actions: {
    goMovieDetail: function ({ commit }, movie) {
      commit('GO_MOVIE_DETAIL', movie)
    },
    heartStatusChange(context){
      axios ({
        method: 'POST',
        url: `http://127.0.0.1:8000/movies/detail/${context.state.movieDetail.m_id}/like/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then((res) => {
        console.log(res.data)
        context.commit('HEART_STATUS_CHANGE', res.data)
      }).catch((err) => {
        console.log(err)
      })
    },
    ChangeCommentLike(context, like_id){
      axios ({
        method: 'POST',
        url: `http://127.0.0.1:8000/comments/${context.state.movieDetail.m_id}/like/${context.state.movieDetail.comments[like_id].id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then((res) => {
        console.log(res.data)
        context.commit('CHANGE_COMMENT_LIKE', res.data)
      }).catch((err) => {
        console.log(err)
      })
    },
    ChangeCommentHate(context, hate_id){
      axios ({
        method: 'POST',
        url: `http://127.0.0.1:8000/comments/${context.state.movieDetail.m_id}/hate/${context.state.movieDetail.comments[hate_id].id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then((res) => {
        console.log(res.data)
        context.commit('CHANGE_COMMENT_HATE', res.data)
      }).catch((err) => {
        console.log(err)
      })
    },
  },
})

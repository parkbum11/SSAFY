import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import MovieDetail from '../views/MovieDetail.vue'
import MyLikedMovies from '../views/MyLikedMovies.vue'
import CreateComment from '../views/CreateComment.vue'
import UpdateComment from '../views/UpdateComment.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', name: 'Main', component: Main },
  { path: '/login', name: 'Login', component: Login },
  { path: '/signup', name: 'Signup', component: Signup },
  { path: '/movieDetail', name: 'MovieDetail', component: MovieDetail },
  { path: '/mylikedmovies', name: 'MyLikedMovies', component: MyLikedMovies },
  { path: '/createcomment', name: 'CreateComment', component: CreateComment },
  { path: '/updatecomment', name: 'UpdateComment', component: UpdateComment },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

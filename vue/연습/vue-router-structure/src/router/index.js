import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/', // 여기가 url
    name: 'Home', // 여기가 name
    component: Home // 여기가 어떤 컴포넌트를 렌더링할 때
  },
  {
    path: '/about',
    name: 'About',
    // 이거는 신경쓰지 마세요! 그냥 위에 Home 쓰는 것처럼 하면 됨!
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

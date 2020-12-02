<template>
  <div>
    <b-jumbotron header="Random Movie">
      <b-button squared variant="outline-secondary" @click="onClick">Pick</b-button>
      <hr>
      <h3>{{this.movie}}</h3>
    </b-jumbotron>
  </div>

</template>

<script>
import _ from 'lodash'
export default {
  name:'Random',
  data(){
    return{
      datas:['대부','해리포터','어벤져스','어바웃타임'],
      movie:'',
    }
  },
  methods:{
    onClick() {
      const movie_idx=_.random(this.datas.length-1)
      this.movie=this.datas[movie_idx]
    }
  }
}
</script>

<style>

</style>
<template>
  <div>
    <h1>App</h1>
    <input type="text" v-model="appData" >
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <Parent 
      :appData="appData" 
      :parentData="parentData"
      :childData="childData"
      @onParentDataChange="onParentDataChange" />
    <Child
      :appData="appData" 
      :parentData="parentData"
      :childData="childData" 
      @onChildDataChange="onChildDataChange" />
  </div>
</template>

<script>
import Parent from './components/Parent.vue'
import Child from './components/Child.vue'

export default {
  name:'App',
  components:{
    Parent,
    Child,
  },
  data: function (){
    return {
      appData:'',
      parentData: '',
      childData: '',
    }
  },
  methods:{
    // onParentDataChange 이벤트 발생시 해야될 일
    // 이벤트 발생 시 인자 전달 받는 것 가능
    onParentDataChange: function(parentData){
      this.parentData = parentData
    },
    onChildDataChange: function(childData){
      this.childData = childData
    },
  },
}
</script>

<style>

</style>
<template>
  <div>
    <h1>Parent</h1>
    <input type="text" @keyup.enter="onChange">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
</template>

<script>
export default {
  // props: ['appData',], 이렇게도 가능!
  props:['appData', 'parentData', 'childData',],
  methods: {
    onChange: function(event){
      // 부모가 달아둔 onParentDataChange라는 이벤트 발생시킴
      // 발생시키면서 인자 전달
      this.$emit('onParentDataChange', event.target.value)
    }
  }
}
</script>

<style>

</style>
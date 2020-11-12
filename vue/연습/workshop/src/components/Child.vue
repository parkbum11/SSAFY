<template>
  <div>
    <h1>Child</h1>
    <input type="text" @keyup.enter="onChange">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
</template>

<script>
export default {
  props:['appData', 'parentData', 'childData',],
  methods: {
    onChange: function(event){
      this.$emit('onChildDataChange', event.target.value)
    }
  }
}
</script>

<style>

</style>
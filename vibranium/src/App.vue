<template>
  <div id="app">
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons">
    <PeriodicTable />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue"
import PeriodicTable from "./components/PeriodicTable.vue"
import 'vue-material/dist/vue-material.min.css'

export default {
  name: "app",
  components: {
    PeriodicTable
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

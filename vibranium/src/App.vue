<template>
  <div id="app">
    <PeriodicTable />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue"
import PeriodicTable from "./components/PeriodicTable.vue"
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

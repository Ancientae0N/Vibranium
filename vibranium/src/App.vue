<template>
<div>

    <TopPart></TopPart>
<v-app>
    <router-view></router-view>
  <navigation></navigation>
</v-app>
</div>
</template>

<script>
import isotope from 'vueisotope';
import navigation from './Navigation.vue';
import leftnav from './LeftNavigation.vue';
import TopPart from './TopPart.vue';
export default {
  name: 'App',
  components: {
    isotope,
    navigation,
    leftnav,
      TopPart
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

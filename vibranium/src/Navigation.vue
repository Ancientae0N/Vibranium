<template>
<v-card height="200px" flat>
  <v-bottom-nav :absolute='true' :active.sync="bottomNav" :value="true" absolute color="transparent">
    <router-link :to="'/'">
      <v-btn color="teal" flat value="recent">
        <v-icon>Periodic Table</v-icon>
      </v-btn>
    </router-link>
    <router-link :to="'/equation'">
      <v-btn color="teal" flat value="favorites">
        <v-icon>Equation</v-icon>
      </v-btn>
    </router-link>
    <router-link :to='"/about"'>
      <v-btn color="teal" flat value="nearby">
        <v-icon>About</v-icon>
      </v-btn>
    </router-link>
  </v-bottom-nav>
</v-card>
</template>

<script>
export default {
  data() {
    return {
      bottomNav: 'recent'
    }
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

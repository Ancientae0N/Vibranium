<template>
<div class="md-layout col">
  <div class="md-layout-item">
    <md-content>
      <isotope :list="elements" :options="options" @filter="filterOption=arguments[0]" @sort="sortOption=arguments[0]">
        <div v-for="element in elements" :key="element.symbol">
          <router-link to="/element/He">
            <md-card class="card" style="width:150px">
              <md-card-header>
                {{element.symbol}}
              </md-card-header>
              <md-card-content>
                {{element.name}}
              </md-card-content>
              <md-card-actions>
              </md-card-actions>
            </md-card>
          </router-link>
        </div>
      </isotope>
    </md-content>
  </div>
</div>
</template>

<script>
import data from "./periodic_table.js";
import $ from 'jquery';
import isotope from 'vueisotope'
export default {
  name: "PeriodicTable",
  data() {
    return {
      elements: data,
      options: {}
    }
  },
  components: {isotope}
}
</script>

<style>
.col: {
  width: 80%
}
.md-card: {
  width: 40px
}
</style>

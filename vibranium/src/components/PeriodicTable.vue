<template>
<div class="md-layout col">
  <div class="md-layout-item">
    <md-content>
      <flex-row tag="section">
        <flex-col v-for="element in elements">
          <router-link to="/element/He">
            <md-card>
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
        </flex-col>
      </flex-row>
    </md-content>
  </div>
</div>
</template>

<script>
import data from "./periodic_table.js";
import $ from 'jquery';
export default {
  name: "PeriodicTable",
  data() {
    return {
      elements: data
    }
  }
}
</script>

<style>
.col: {width:80%}
</style>

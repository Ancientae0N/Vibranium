<template>
<flex-row tag="section">
  <flex-col v-for="element in elements">
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
  </flex-col>
</flex-row>
</template>

<script>
import data from "./periodic_table.js";
import {
  Waterfall,
  WaterfallItem
} from 'vue2-waterfall';
export default {
  name: "PeriodicTable",
  data() {
    return {
      elements: data
    }
  }
}
</script>

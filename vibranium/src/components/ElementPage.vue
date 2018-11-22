<template>
<div class="container">

  <md-content>
    {{$route.params.symbol}}
  </md-content>
</div>
</template>

<script>
import data from "./periodic_table.js";
import $ from 'jquery';

export default {
  name: "ElementPage",
  data() {
    return {
      elements: data
    }
  }
}
</script>

<style>
.container: {
  width: 80%;
}
</style>

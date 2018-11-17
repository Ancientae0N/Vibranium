<template>
<div>
  askjdlkasjdlkasjd
  <div v-for="element in elements">
    {{element.symbol}}
  </div>
</div>
</template>

<script>
import data from "./periodic_table.js"
export default {
  name: "PeriodicTable",
  data() {
    return {
      elements: data
    }
  }
}
</script>

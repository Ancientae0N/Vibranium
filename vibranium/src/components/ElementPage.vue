<template>
  <iframe :src="'http://localhost:5000/'+$route.params.symbol" style="width:100%;height:100%">
  </iframe>
</template>

<script>

export default {
  name: "ElementPage",
}

</script>

<style>
.container: {
  width: 80%;
}
</style>

<template>
<div id="app">
  <h1>Equation Solver</h1>
  <v-app id="inspire">
    <v-form>
      <v-container>
        <v-layout row wrap>
          <v-flex xs12 sm6 md3 offset-sm2>
            <v-text-field label="Left side" outline id="lhs" v-model='lhs'></v-text-field>
          </v-flex>
          <v-flex xs12 sm6 md3 offset-sm2>
            <v-text-field label="Right side" outline id="rhs" v-model='rhs'></v-text-field>
          </v-flex>



        </v-layout>
        <v-app id="inspire">
          <div class='output'>
            {{result}}
          </div>
        </v-app>
      </v-container>
    </v-form>
  </v-app>
</div>
</template>
<style>
h1 {
  padding: 10px
}
</style>
<script>

function fetchData() {
  console.log('recompute');
  var _this = this;
  var equation = this.lhs + "->" + this.rhs;
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://127.0.0.1:5000/balance/"+equation, true);
  xhr.send()
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
      _this.result = xhr.response;
    }
  }
}

export default {
  data: function() {
    return {
      lhs: '',
      rhs: '',
      result: ''
    }
  },
  watch: {
    lhs: fetchData,
    rhs: fetchData
  }
}
</script>

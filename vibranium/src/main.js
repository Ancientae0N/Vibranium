import Vue from "vue"
Vue.config.devtools=true;
//import App from "./App.vue"
import 'vue-material/dist/vue-material.min.css'
import VueFlex from "vue-flex";
// Already autoprefixed for vendor prefixes.
// Also namespaced to avoid collisions.
import "vue-flex/dist/vue-flex.css";
//import VueMaterial from 'vue-material'
import Vuetify from 'vuetify'


import App from './App'
import router from './router'
import VueRouter from 'vue-router'
import isotope from 'vueisotope'
import 'vuetify/dist/vuetify.min.css'

Vue.config.productionTip = false

Vue.use(isotope);
Vue.use(VueFlex);
Vue.config.productionTip = false;
//Vue.use(VueMaterial);
Vue.use(VueRouter);
Vue.use(Vuetify);


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {isotope},
  render: h => h(App)
})

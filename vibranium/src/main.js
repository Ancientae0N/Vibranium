import Vue from "vue"
import App from "./App.vue"
import 'vue-material/dist/vue-material.min.css'
import VueFlex from "vue-flex";
// Already autoprefixed for vendor prefixes.
// Also namespaced to avoid collisions.
import "vue-flex/dist/vue-flex.css";

Vue.use(VueFlex);
Vue.config.productionTip = false;
Vue.use(VueMaterial);
import VueMaterial from 'vue-material'

new Vue({
  render: h => h(App),
}).$mount("#app");

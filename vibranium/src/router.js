import VueRouter from 'vue-router'
import ElementPage from "./components/ElementPage.vue"
import PeriodicTable from "./components/PeriodicTable.vue"

var router = new VueRouter({
  routes: [{
    path: "/",
    component: PeriodicTable
  },
  {
    path: "/element/:symbol",
    component: ElementPage
  }]
})

export default router;

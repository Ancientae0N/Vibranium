import VueRouter from 'vue-router'
import ElementPage from "./components/ElementPage.vue"
import PeriodicTable from "./components/PeriodicTable.vue"
import Equations from "./components/Equations.vue"

var router = new VueRouter({
  routes: [{
    path: "/",
    component: PeriodicTable
  },
  {
    path: "/element/:symbol",
    component: ElementPage
  },
      {
        path: "/equation",
          component: Equations
      }]
})

export default router;

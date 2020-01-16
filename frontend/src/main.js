import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueRouter from 'vue-router'
import createjob from './components/createjob.vue'
import dbselect from './components/dbselect.vue'
import tbview from './components/tbview.vue'
import convert from './components/convert.vue'
import tbcheck from './components/tbcheck.vue'
import testdjango from './components/testdjango.vue'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'tailwindcss/dist/tailwind.css'
import './assets/css/tailwind.css'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import 'vue-ads-table-tree/dist/vue-ads-table-tree.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Grid from 'simple-xgrid'
import  'simple-xgrid/dist/simple-grid.css'
import feather from 'vue-icon'

Vue.use(feather, 'v-icon')

Vue.use(Grid);

library.add(faUserSecret)
import '@fortawesome/fontawesome-free/css/all.css';
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueRouter)

const routes = [
  {path: '/', component: createjob},
  {path: '/createjob', component: createjob},
  {path: '/dbselect', component: dbselect},
  {path: '/tbview', component: tbview},
  {path: '/convert', component: convert},
  {path: '/tbcheck', component: tbcheck},
  {path: '/testdjango', component: testdjango},
]

const router = new VueRouter({
    mode:'history',
    routes // short for `routes: routes`
})


new Vue({
  el: '#app',
  beforeCreate(){
    Vue.prototype.$http=axios
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    axios.defaults.xsrfCookieName = 'csrftoken'
  },
  router,
  render: h => h(App)
})

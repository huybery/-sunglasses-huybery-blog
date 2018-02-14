import Vue from 'vue'
import App from './App'
import store from './store'
import router from './router'
import axios from './http'

import iView from 'iview'
// import 'iview/dist/styles/iview.css'
import '../my-theme/index.less'

Vue.config.productionTip = false

Vue.use(iView)
Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})

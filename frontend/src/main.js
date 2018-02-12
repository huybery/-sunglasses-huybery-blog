import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview'
// import 'iview/dist/styles/iview.css'
import '../my-theme/index.less'

import axios from 'axios'

Vue.config.productionTip = false
Vue.use(iView)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.defaults.auth = {
  username: '',
  password: ''
}

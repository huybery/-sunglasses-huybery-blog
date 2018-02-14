import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

import iView from 'iview'
// import 'iview/dist/styles/iview.css'
import '../my-theme/index.less'

import axios from 'axios'

Vue.config.productionTip = false
Vue.use(iView)

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (localStorage.token) {
      store.commit('set_token', localStorage.token)
      let token = store.getters.token
      console.log(token)
      axios.defaults.auth = {
        username: token,
        password: 'unused'
      }
      next()
    } else {
      next({
        path: '/login'
      })
    }
  } else {
    iView.LoadingBar.start()
    next()
  }
})

router.afterEach((to, from, next) => {
  iView.LoadingBar.finish()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})

axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.defaults.auth = {
  username: '',
  password: ''
}
Vue.prototype.$axios = axios

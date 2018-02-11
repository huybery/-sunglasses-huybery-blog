import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview'
// import 'iview/dist/styles/iview.css'
import '../my-theme/index.less'

Vue.config.productionTip = false
Vue.use(iView)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

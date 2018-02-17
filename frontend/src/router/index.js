import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
import iView from 'iview'
import axios from '../http'

import {routes} from './router'
import {LOGIN} from '../store/mutation-types'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

// console.log(routes)
// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//   ]
// })

const router = new Router({
  routes,
  mode: 'history'
})

// 刷新页面时重新赋值 token
if (localStorage.getItem('token')) {
  store.commit(LOGIN, localStorage.token)
}

// 路由钩子方法
router.beforeEach((to, from, next) => {
  // console.log('now token: ' + localStorage.token)
  if (to.meta.requireAuth) {
    if (localStorage.token) {
      store.commit(LOGIN, localStorage.token)
      let token = store.state.token
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

export default router

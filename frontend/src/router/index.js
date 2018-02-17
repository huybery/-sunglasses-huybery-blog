import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
import iView from 'iview'
import axios from '../http'
import {LOGIN} from '../store/mutation-types'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

const routerOptions = [{
  path: '/',
  component: 'Home'
},
{
  path: '/post',
  component: 'Post'
},
{
  path: '/categories',
  component: 'Categories'
},
{
  path: '/about',
  component: 'About'
},
{
  path: '/login',
  component: 'Login'
},
{
  path: '/register',
  component: 'Register'
},
{
  path: '/admin',
  component: 'Admin',
  meta: {
    requireAuth: true
  }
},
{
  path: '*',
  component: 'NotFound'
}]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => (
      import(`@/components/${route.component}`))
  }
})

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
  // console.log('token commit from localStorage')
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

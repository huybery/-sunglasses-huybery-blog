import Vue from 'vue'
import Router from 'vue-router'
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

export default new Router({
  routes,
  mode: 'history'
})

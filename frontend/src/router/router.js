// 常规 router
const appRouterOptions = [{
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
  path: '*',
  component: 'NotFound'
}]

const appRoutes = appRouterOptions.map(route => {
  return {
    ...route,
    component: () => (
        import(`@/components/${route.component}`))
  }
})

// dashBoard 子路由相关
const dashboardChild = [{
  path: '/post',
  component: 'Post'
},
{
  path: '/user',
  component: 'User'
},
{
  path: '/statis',
  component: 'Statis'
}]

const dashboardChildRoutes = dashboardChild.map(route => {
  return {
    ...route,
    component: () => (
        import(`@/components/dashboard/${route.component}`)
    )
  }
})

// dashboard 相关 router
const dashboardRouterOptions = [{
  path: '/admin',
  component: 'Admin',
  meta: {
    requireAuth: true
  },
  children: dashboardChildRoutes
}]

const dashboardRoutes = dashboardRouterOptions.map(route => {
  return {
    ...route,
    component: () => (
        import(`@/components/dashboard/${route.component}`)
    )
  }
})

// 合并路由数组
export const routes = [
  ...appRoutes,
  ...dashboardRoutes
]

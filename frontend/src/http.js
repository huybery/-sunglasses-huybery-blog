// axios 基本配置

import axios from 'axios'
import store from './store'
import router from './router'
import * as types from './store/mutation-types'

axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.defaults.auth = {
  username: '',
  password: ''
}

// http request 拦截器
axios.interceptors.request.use(
  config => {
    if (store.getters.token) {
      config.headers.Authorization = `token ${store.getters.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

// http resposne 拦截器
axios.interceptors.response.use(
  response => {
    return response
  },
  err => {
    if (err.response) {
      switch (err.response.status) {
        case 401:
          store.commit(types.LOGOUT)
          router.replace({
            path: '/login'
          })
      }
    }
    return Promise.reject(err.response.data)
  }
)
export default axios

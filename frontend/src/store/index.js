import Vue from 'vue'
import Vuex from 'vuex'
import * as types from './mutation-types'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: '',
    loginUser: ''
  },
  mutations: {
    [types.LOGIN] (state, payload) {
      state.token = payload.token
      state.loginUser = payload.loginUser
      localStorage.token = payload.token
      localStorage.loginUser = payload.loginUser
    },
    [types.LOGOUT] (state) {
      state.token = null
      state.loginUser = null
      localStorage.removeItem('token')
      localStorage.removeItem('loginUser')
    }
  }
})

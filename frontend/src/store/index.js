import Vue from 'vue'
import Vuex from 'vuex'
import * as types from './mutation-types'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: ''
  },
  mutations: {
    [types.LOGIN] (state, token) {
      state.token = token
      localStorage.token = token
    },
    [types.LOGOUT] (state) {
      state.token = null
      localStorage.removeItem('token')
    }
  },
  getters: {
    token: state => {
      return state.token
    }
  }
})

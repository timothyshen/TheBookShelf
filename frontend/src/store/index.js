import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      isLoading: false,
      isAuthenticated: false,
      token: {
          access_token: '',
          refresh_token: ''
      },
      user: null
  },
  mutations: {
      LOGIN_SUCCESS(state, response) {
          state.token.access_token = response.data.access_token
          state.token.refresh_token = response.data.refresh_token
          state.isAuthenticated = true
      },
      setIsLoading(state, status) {
          state.isLoading = status
      },
      removeToken(state) {
          state.token.access_token = ''
          state.token.refresh_token = ''
          state.isAuthenticated = false
      },
      setUser(state, user) {
          state.user = user
      },
  },
  actions: {},
  modules: {
  }
})

<template>
  <div class="about">
    <form @submit.prevent="toggleLogin">
      <label>Username:</label>
      <input v-model="username" name="username">
      <label>Password</label>
      <input v-model="password" name="password" type="password">
      <button @click="toggleLogin">logon</button>
      <div v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
    </form>
    <login></login>
  </div>
</template>
<script>
import axios from "axios";
import Login from "@/views/components/Login/Login";
import {toLogin, getUserInfo, getUserBookcase} from "@/api/axois";
export default {
  components: {Login},
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    async toggleLogin() {

      this.$store.commit('setIsLoading', true)
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')

      const userdata = {
        username: this.username,
        password: this.password,
        grant_type: 'password',
        client_id: 'CuHSbKKrPUwL0IzeRZ5M8CnTVrGav58BW9m75M9v',
        client_secret: 'kMX4H5mGCSGBgmhDTfi8vYLfU8SRfqBWx5F4IpFgtEKIjBcvLdc6oUImZ2rLVKPAgznY4mjMf9s8k67QYK1E9fzDrsdjw2dzYVXcLPzecSW4OWOV3DCfuTWD8lWQKRPo'
      }
      // login api call - for token generation
      // then add token to the store
      await toLogin(userdata)
          .then((response) => {
            console.log(response.data)
            const access = response.data.access_token
            this.$store.commit('LOGIN_SUCCESS', response)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + access
            console.log(axios.defaults.headers.common['Authorization'])
          }).catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else if (error.message) {
              this.errors.push('Something went wrong. Please try again!')
            }
          })
      // Get user information
      // After the token added to authentication, retrieve user information from server
      await getUserInfo()
          .then((response) => {
            console.log(response.data)
            this.$store.commit('setUser', response.data.user[0])
          }).catch((error) => {
            console.log(error.data)
          })
      await getUserBookcase()
          .then((response) => {
            console.log(response.data)
          }).catch((error) => {
            console.log(error.data)
          });
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

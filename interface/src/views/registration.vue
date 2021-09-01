<template>
  <div class="container">
    <section class="hero">
      <div class="hero-body">
        <p class="title">
          Registration
        </p>
      </div>
    </section>
    <div class="columns is-centered">
      <div class="column is-half">
        <div v-if="errors.length && isError" class="notification is-danger">
          <button class="delete" @click="setClose"></button>
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>
        <form @submit.prevent="toRegister">
          <div class="field">
            <label class="label">Email</label>
            <div class="control has-icons-left has-icons-right">
              <input v-model="email_address" class="input" placeholder="Email input" type="email">
              <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
              </span>
              <span v-show="errors.length" class="icon is-small is-right">
                <i class="fas fa-exclamation-triangle"></i>
              </span>
            </div>
          </div>
          <div class="field">
            <label class="label">Password</label>
            <div class="control">
              <input v-model="password" class="input" placeholder="password" type="password">
            </div>
          </div>
          <div class="field">
            <label class="label">Confirm Password</label>
            <div class="control">
              <input v-model="password2" class="input" placeholder="password" type="password">
            </div>
          </div>
          <div class="field">
            <div class="control">
              <label class="checkbox">
                <input v-model="isTCClicked" type="checkbox">
                I agree to the <a href="#">terms and conditions</a>
              </label>
            </div>
          </div>

          <div class="field is-grouped is-grouped-centered">
            <p class="control">
              <a class="button is-primary" @click="toRegister">
                Submit
              </a>
            </p>
            <p class="control">
              <a class="button is-light" @click="backButton">
                Cancel
              </a>
            </p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from 'bulma-toast'

export default {
  name: "registration",
  data() {
    return {
      email_address: '',
      password: '',
      password2: '',
      errors: [],
      isError: true,
      isTCClicked: false
    }
  },
  methods: {
    setClose() {
      this.isError = false
    },
    backButton() {
      this.$router.back()
    },
    async toRegister() {
      if (this.email_address === '') {
        this.errors.push('The email address is missing')
      } else {
        const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        if (!mailReg.test(this.email_address)) {
          this.errors.push('Please insert correct email format')
        }
      }
      if (this.password === '') {
        this.errors.push('The password is too short')
      }

      if (this.password !== this.password2) {
        this.errors.push('The password are not matching')
      }
      if (this.isTCClicked === false) {
        this.errors.push('Please accept the terms and condition!')
      }
      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)

        const formData = {
          username: this.email_address,
          password: this.password
        }
        await axios
            .post('http://127.0.0.1:8000/api/v1/register', formData)
            .then((response) => {
              console.log(response.data)
              toast({
                message: 'Account was created, please log in',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              })
              this.$router.push('/login')
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              } else if (error.message) {
                this.errors.push('Something went wrong. Please try again!')
              }
            })
        this.$store.commit('setIsLoading', false)
      }
    }
  },
  computed: {}
}
</script>

<style lang="scss" scoped>

</style>

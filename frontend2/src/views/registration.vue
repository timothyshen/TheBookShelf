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
        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error}}</p>
        </div>
        <form @submit.prevent="toRegister">
          <div class="field">
            <label class="label">Email</label>
            <div class="control has-icons-left has-icons-right">
              <input class="input is-danger" type="email" placeholder="Email input" v-model="email_address" >
              <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
              </span>
              <span class="icon is-small is-right">
                <i class="fas fa-exclamation-triangle"></i>
              </span>
            </div>
          </div>
          <div class="field">
            <label class="label">Password</label>
            <div class="control">
              <input class="input" type="password" placeholder="password" v-model="password">
            </div>
          </div>
          <div class="field">
            <label class="label">Confirm Password</label>
            <div class="control">
              <input class="input" type="text" placeholder="password" v-model="password2">
            </div>
          </div>
          <div class="field">
            <div class="control">
              <label class="checkbox">
                <input type="checkbox">
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
              <a class="button is-light">
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
export default {
  name: "registration",
  data() {
    return {
      email_address: '',
      password:'',
      password2:'',
      errors:[]
    }
  },
  methods: {
    async toRegister() {
      if (this.email_address === '') {
        this.errors.push('The email address is missing')
      }else{
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
      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)

        const formData = {
          username: this.email_address,
          password: this.password
        }
        await axios
            .post('http://127.0.0.1:8000/api/v1/register', formData)
            .then((response)=>{
              console.log(response.data)
            })
            .catch()
      }
    }
  },
  computed: {

  }
}
</script>

<style lang="scss" scoped>

</style>

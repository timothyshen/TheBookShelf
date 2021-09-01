<template>
  <div class="container">
    <section class="hero">
      <div class="hero-body">
        <p class="title">
          - Billing address -
        </p>
      </div>
    </section>
    <div class="columns is-centered" style="padding: 20px">
      <div class="column is-three-quarters">
        <form>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Your name</label>
            </div>
            <div class="field-body">
              <div class="field">
                <p class="control is-expanded has-icons-left">
                  <input v-model="billing_address.first_name" class="input" placeholder="First name" type="text">
                  <span class="icon is-small is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </p>
              </div>
              <div class="field">
                <p class="control is-expanded has-icons-left">
                  <input v-model="billing_address.last_name" class="input" placeholder="Last name" type="text">
                  <span class="icon is-small is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </p>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-left">
              <label class="label">Phone</label>
            </div>
            <div class="field-body">
              <div class="field is-expanded">
                <div class="field has-addons">
                  <p class="control">
                    <a class="button is-static">
                      +44
                    </a>
                  </p>
                  <p class="control is-expanded">
                    <input v-model="billing_address.phone" class="input" placeholder="Your phone number" type="tel">
                  </p>
                </div>
                <p class="help is-left">Do not enter the first zero</p>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-left">
              <label class="label">Address</label>
            </div>
            <div class="field-body">
              <div class="field is-expanded">
                <div class="control">
                  <input v-model="billing_address.address" class="input" name="address" placeholder="Line of address"
                         required="" type="text">
                </div>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-left">
              <label class="label">Zip code</label>
            </div>
            <div class="field-body">
              <div class="field is-expanded">
                <div class="control">
                  <input v-model="billing_address.zipcode" class="input " name="zip_code" placeholder="Zip code"
                         required="" type="text">
                </div>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-left">
              <label class="label">Place</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <input v-model="billing_address.place" class="input " name="place" required="" type="text">
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
    <div class="columns">
      <div v-for="plan in sub_plan" v-bind:key="plan.id" class="column">
        <div class="card">
          <p>{{ plan.title }}</p>
          <p>$ {{ plan.price }}</p>
          <button class="button is-danger" @click="subscribe('plan','1 month plan', plan.price_id)">Subscribe</button>
        </div>
      </div>
      <div class="column">
        <div class="card">
          <p>30 Bookshelf coins</p>
          <p>$0.99</p>
          <button class="button is-danger" @click="topup('topup','30 BookShelf coins')">Purchase</button>
        </div>
      </div>
    </div>

  </div>

</template>

<script>

import axios from "axios";
import {loadStripe} from '@stripe/stripe-js';

export default {
  name: "plan",
  data() {
    return {
      pub_key: '',
      stripe: null,
      billing_address_list: null,
      billing_address: {
        first_name: '',
        last_name: '',
        email: this.$store.state.user.email,
        address: '',
        zipcode: '',
        place: '',
        phone: '',
        user_id: this.$store.state.user.userid
      },
      sub_plan: null,
      product_list: null
    }
  },
  async mounted() {
    await this.getPubKey()

    this.stripe = await loadStripe(this.pub_key);


  },
  methods: {
    async getPubKey() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get(`http://127.0.0.1:8000/api/v1/stripe/get_stripe_pub_key/`)
          .then(response => {
            this.pub_key = response.data.pub_key
          })
          .catch(error => {
            console.log(error)
          })

      await axios
          .get('http://127.0.0.1:8000/api/v1/subscription/')
          .then(response => {
            console.log(response.data)
            this.sub_plan = response.data
          })

      this.$store.commit('setIsLoading', false)
    },
    async subscribe(type, plan) {
      this.$store.commit('setIsLoading', true)

      const data = {
        product_type: type,
        plan: plan,
        gateway: 'stripe',
        user: 1,
        billing_address: this.billing_address
      }

      await axios
          .post('http://127.0.0.1:8000/api/v1/stripe/create_checkout_session/', data)
          .then(response => {
            console.log(response.data.sessionId)
            return this.stripe.redirectToCheckout({sessionId: response.data.sessionId})
          })
          .catch(error => {
            console.log('Error:', error)
          })

      /*await axios
          .post(`/api/v1/teams/upgrade_plan/`, data)
          .then(response => {
              console.log('Upgraded plan')

              console.log(response.data)

              this.$store.commit('setTeam', {
                  'id': response.data.id,
                  'name': response.data.name,
                  'plan': response.data.plan.name,
                  'max_leads': response.data.plan.max_leads,
                  'max_clients': response.data.plan.max_clients
              })

              toast({
                  message: 'The plan was changed!',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
              })

              this.$router.push('/dashboard/team')
          })
          .catch(error => {
              console.log(error)
          })*/

      this.$store.commit('setIsLoading', false)
    },
    async topup(type, product, id_price) {
      this.$store.commit('setIsLoading', true)

      console.log(id_price)
      const data = {
        product_type: type,
        product: product,
        gateway: 'stripe',
        user: 1,
        billing_address: this.billing_address,
        price_id: 'price_1JF4FxBaL13HgkoymjNPtsCs'
      }
      console.log(data)
      await axios
          .post('http://127.0.0.1:8000/api/v1/stripe/create_topup_session/', data)
          .then(response => {
            console.log(response.data)
            return this.stripe.redirectToCheckout({sessionId: response.data.sessionId})
          })
    }
  }
}
</script>

<style scoped>

</style>

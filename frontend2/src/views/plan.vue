<template>
  <div>
    <p>1 month plan</p>
    <button class="button is-danger" @click="subscribe('1 month plan')">Subscribe</button>
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
      stripe: null
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

      this.$store.commit('setIsLoading', false)
    },
    async subscribe(plan) {
      this.$store.commit('setIsLoading', true)

      const data = {
        plan: plan,
        gateway: 'stripe',
        user: 1
      }

      axios
          .post('http://127.0.0.1:8000/api/v1/stripe/create_checkout_session/', data)
          .then(response => {
            console.log(response.data.sessionId)
            localStorage.setItem('session_id', response.data.sessionId)
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
    }
  }
}
</script>

<style scoped>

</style>

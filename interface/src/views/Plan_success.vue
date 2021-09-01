<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Thank you</h1>
      </div>

      <div class="column is-4">
        <p class="is-center">Thank you for subscribing to a plan!</p>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
export default {
  name: "Plan_success",
  data() {
    return {}
  },
  mounted() {
    console.log(localStorage.getItem('session_id'))
    //   axios
    //       .post('http://127.0.0.1:8000/api/v1/stripe/check_session/', {
    //         'session_id': this.$route.query.session_id,
    //         'order_id': this.$route.query.order_id
    //       })
    //       .then(response => {
    //         console.log(response)
    //       })
    //       .catch(error => {
    //
    //         console.log('Error', error)
    //         })
  }
}
</script>

<style scoped>

</style>

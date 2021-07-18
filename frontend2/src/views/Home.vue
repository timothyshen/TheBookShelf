<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <router-link v-if="$store.state.isAuthenticated" to="/plan">Plan</router-link>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {}
}
</script>

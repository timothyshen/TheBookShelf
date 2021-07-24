<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <a class="button is-primary">
      <router-link v-if="$store.state.isAuthenticated" to="/plan">Plan</router-link>
    </a>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {}
}
</script>

<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
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
    </div>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
  components: {
  }
}
</script>

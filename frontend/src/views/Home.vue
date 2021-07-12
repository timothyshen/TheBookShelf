<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <plan></plan>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/views/components/HelloWorld.vue'
import plan from "@/views/components/plan";

export default {
  name: 'Home',
  components: {
    plan
  }
}
</script>

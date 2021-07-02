<template>
  <div class="about">
    <h1>This is an about page</h1>
    <login></login>
  </div>
</template>
<script>
import Login from "@/views/components/Login/Login";
export default {
  components: {Login},
  name: 'HelloWorld',
  props: {
    msg: String
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

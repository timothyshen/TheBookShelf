<template>
    <el-container>
      <div>User</div>
      <div>UserName:{{this.$store.state.user.username}}</div>
      <div>UserName:{{this.$store.state.user.role}}</div>
      <div>UserName:{{this.$store.state.user.userid}}</div>
      <div>UserName:{{this.$store.state.user.email}}</div>
    </el-container>
</template>

<script>
export default {
  name: "user_info"
}
</script>

<style scoped>

</style>

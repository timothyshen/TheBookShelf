<template>
  <nav class="navbar is-primary py-4">
    <div class="container is-fluid">
      <div class="navbar-brand">
        <a class="navbar-item" href="#">
          <img alt="" class="image" src="bulma-plain-assets/logos/plainb-logo.svg" width="96px">
        </a>
        <a aria-expanded="false" aria-label="menu" class="navbar-burger" role="button">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu">
        <div class="navbar-start"><a class="navbar-item" href="#">About</a><a class="navbar-item" href="#">Company</a><a
            class="navbar-item" href="#">Services</a><a class="navbar-item" href="#">Testimonials</a></div>
        <div class="navbar-item">
          <el-input
              class="input " placeholder="请输入内容"
              style="background-color: #00D1B2; border: none"
              type="search"
          >
            <template #append>
              <el-button icon="el-icon-search"></el-button>
            </template>
          </el-input>
        </div>
        <div class="navbar-item">
          <div class="buttons">
            <a class="button" href="#">Sign In</a>
            <a class="button is-primary" href="#">Sign Up</a>
          </div>
        </div>

      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "header_two"
}
</script>

<style scoped>

</style>

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
          <div class="field has-addons">
            <div class="control">
              <input aria-label="Search" class="input" placeholder="Search" type="search">
            </div>
            <div class="control">
              <button class="button" type="submit">
                <svg fill="none" stroke="currentColor" style="width: 24px;height: 24px" viewBox="0 0 24 24"
                     xmlns="http://www.w3.org/2000/svg">
                  <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" stroke-linecap="round" stroke-linejoin="round"
                        stroke-width="2"></path>
                </svg>
              </button>
            </div>
          </div>
          <div class="navbar-item">
            <div class="buttons">
              <a class="button" href="#">Sign In</a>
              <a class="button is-primary" href="#">Sign Up</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "header_nav"
}
</script>

<style scoped>

</style>

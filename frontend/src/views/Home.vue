<template>
  <div class="home">
    <a v-if="$store.state.isAuthenticated" class="button is-primary">
      <router-link to="/plan">Plan</router-link>
    </a>

    <section class="section is-fixed-top">
      <div class="container">
        <div class="columns is-multiline is-centered">
          <div class="column is-8 has-text-centered">
            <span class="has-text-grey-dark">New Feature</span>
            <h2 class="mt-2 mb-4 is-size-1 is-size-3-mobile has-text-weight-bold">Take quick action that increases your
              brand's regular profit.</h2>
            <p class="subtitle has-text-grey mb-5">If you have ever wondered how to develop your brand, this is the
              place for you. Take a big step forward in growing your business with this great tool.</p>
            <div class="buttons is-centered"><a class="button is-primary" href="#">Active Demo</a><a class="button"
                                                                                                     href="#">Share with
              your friends</a></div>
          </div>
        </div>
        <div class="hero-foot">
          <nav class="tabs is-boxed is-fullwidth">
            <div class="container">
              <ul>
                <li class="is-active">
                  <a>Overview</a>
                </li>
                <li><a href="#monetization">Pictures</a></li>
                <li><a href="#publishing">Music</a></li>
                <li><a href="#benefit">Videos</a></li>
                <li><a href="#we">Documents</a></li>
              </ul>
            </div>
          </nav>
        </div>
      </div>
    </section>
    <section id="monetization" :class="{ 'active show': isActive('monetization') }" class="section">
      <div class="container">
        <div class="is-vcentered columns is-multiline">
          <div class="column is-5">
            <h2 class="mb-4 is-size-1 is-size-3-mobile has-text-weight-bold">Expand your brand with this excellent
              extension tool</h2>
            <p class="subtitle has-text-grey mb-5">With this tool, you will get much better results at work and develop
              new skills. Will you take the risk of trying the latest version of our application?</p>
            <a class="button is-primary" href="#">Try Demo</a>
          </div>
          <div class="column is-6 ml-auto">
          </div>
        </div>
      </div>
    </section>
    <section id="publishing" :class="{ 'active show': isActive('publishing') }" class="section">
      <div class="container">
        <div class="is-vcentered columns is-multiline">
          <div class="column is-6">

          </div>
          <div class="column is-5 ml-auto">
            <h2 class="mb-4 is-size-1 is-size-3-mobile has-text-weight-bold">Expand your brand with this excellent
              extension tool</h2>
            <p class="subtitle has-text-grey mb-5">With this tool, you will get much better results at work and develop
              new skills. Will you take the risk of trying the latest version of our application?</p>
            <a class="button is-primary" href="#">Try Demo</a>
          </div>
        </div>
      </div>
    </section>
    <section id="benefit" :class="{ 'active show': isActive('monetization') }" class="section">
      <div class="container">
        <div class="is-vcentered columns is-multiline">
          <div class="column is-5">
            <h2 class="mb-4 is-size-1 is-size-3-mobile has-text-weight-bold">Expand your brand with this excellent
              extension tool</h2>
            <p class="subtitle has-text-grey mb-5">With this tool, you will get much better results at work and develop
              new skills. Will you take the risk of trying the latest version of our application?</p>
            <a class="button is-primary" href="#">Try Demo</a>
          </div>
          <div class="column is-6 ml-auto">

          </div>
        </div>
      </div>
    </section>
    <section id="we" :class="{ 'active show': isActive('publishing') }" class="section">
      <div class="container">
        <div class="is-vcentered columns is-multiline">
          <div class="column is-6">

          </div>
          <div class="column is-5 ml-auto">
            <h2 class="mb-4 is-size-1 is-size-3-mobile has-text-weight-bold">Expand your brand with this excellent
              extension tool</h2>
            <p class="subtitle has-text-grey mb-5">With this tool, you will get much better results at work and develop
              new skills. Will you take the risk of trying the latest version of our application?</p>
            <a class="button is-primary" href="#">Try Demo</a>
          </div>
        </div>
      </div>
    </section>

  <footer_component></footer_component>
  </div>
</template>

<script>
// @ is an alias to /src
import Footer_component from "../components/footer_component.vue";

export default {
  name: 'Home',
  components: {Footer_component},
  data() {
    return {
      activeItem: 'monetization'
    }
  },
  methods: {
    isActive(menuItem) {
      return this.activeItem === menuItem
    },
    setActive(menuItem) {
      this.activeItem = menuItem
    }
  }
}
</script>

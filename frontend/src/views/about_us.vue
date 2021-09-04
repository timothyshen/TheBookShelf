<template>
  <div>
    <section class="hero is-info is-medium">
      <div class="hero-head">
        <nav class="navbar">
          <div class="container">
            <div class="navbar-brand">
              <a class="navbar-item">
                <img alt="Logo" src="https://bulma.io/images/bulma-type-white.png">
              </a>
              <span class="navbar-burger" data-target="navbarMenuHeroB">
            <span>
              Ranking
            </span>
            <span>d</span>
            <span></span>
          </span>
            </div>
            <div id="navbarMenuHeroB" class="navbar-menu">
              <div class="navbar-end">
                <a class="navbar-item is-active">
                  Home
                </a>
                <a class="navbar-item">
                  Examples
                </a>
                <a class="navbar-item">
                  Documentation
                </a>
                <span class="navbar-item">
              <a class="button is-info is-inverted">
                <span class="icon">
                  <i class="fab fa-github"></i>
                </span>
                <span>Download</span>
              </a>
            </span>
              </div>
            </div>
          </div>
        </nav>
      </div>

      <div class="hero-body">
        <div class="container has-text-centered">
          <p class="title">
            Title
          </p>
          <p class="subtitle">
            Subtitle
          </p>
        </div>
      </div>

      <div class="hero-foot">
        <nav class="tabs is-boxed is-fullwidth">
          <div class="container">
            <ul>
              <li class="is-active">
                <a>Overview</a>
              </li>
              <li>
                <a>Monetization</a>
              </li>
              <li>
                <a>Publishing</a>
              </li>
              <li>
                <a>Advertising</a>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </section>
    <div class="container">
      <section class="articles">

      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "about_us"
}
</script>

<style scoped>
.hero-body {
  background-image: url(https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Plum_trees_Kitano_Tenmangu.jpg/1200px-Plum_trees_Kitano_Tenmangu.jpg);
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  height: 500px;
}

.articles {
  margin: 5rem 0;
  margin-top: -200px;
}

.articles .content p {
  line-height: 1.9;
  margin: 15px 0;
}

.author-image {
  position: absolute;
  top: -30px;
  left: 50%;
  width: 60px;
  height: 60px;
  margin-left: -30px;
  border: 3px solid #ccc;
  border-radius: 50%;
}

.media-center {
  display: block;
  margin-bottom: 1rem;
}

.media-content {
  margin-top: 3rem;
}

.article, .promo-block {
  margin-top: 6rem;
}

div.column.is-8:first-child {
  padding-top: 0;
  margin-top: 0;
}

.article-title {
  font-size: 2rem;
  font-weight: lighter;
  line-height: 2;
}

.article-subtitle {
  color: #909AA0;
  margin-bottom: 3rem;
}

.article-body {
  line-height: 1.4;
  margin: 0 6rem;
}

.promo-block .container {
  margin: 1rem 5rem;
}
</style>

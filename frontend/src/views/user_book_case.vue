<template>
  <div>
    <div class="dashboard is-full-height">
      <!-- left panel -->
      <div class="dashboard-panel is-one-quarter">
      </div>

      <!-- main section -->
      <div class="dashboard-main is-scrollable">
        <nav class="navbar is-fixed-top">
          <div class="navbar-brand">
        <span class="navbar-item">
          Bulma Dashbaord
        </span>
          </div>
        </nav>

        <section class="section">
          <p class="title">
            Main
          </p>
        </section>

        <!-- the footer will take up all unused space at the bottom -->
        <footer class="footer">

        </footer>
      </div>

      <!-- right panel -->
      <div class="dashboard-main is-small">
      </div>
    </div>
    <table class="table">
      <thead>
      <tr></tr>
      </thead>
      <tbody>
      <tr v-for="(book, index) in book_case" v-bind:key="index">
        <th>{{ index }}</th>
        <td>{{ book.name }}</td>
        <td>{{ book.age }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "user_book_case",
  data() {
    return {
      book_case: [
        {id: 3, name: 'Bob', age: 27},
        {id: 4, name: 'Frank', age: 32},
        {id: 5, name: 'Joe', age: 38}
      ]
    }
  }
}
</script>

<style scoped>

</style>

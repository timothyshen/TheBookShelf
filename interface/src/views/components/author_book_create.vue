<template>
  <div class="container">
    <section class="hero">
      <div class="hero-body">
        <p class="title">
          - Create Your Book -
        </p>
      </div>
    </section>
    <div class="columns is-centered" style="padding:20px">
      <div class="column is-half">
        <form>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Book name</label>
            </div>
            <div class="field-body">
              <div class="field">
                <p class="control has-icons-left">
                  <input v-model="book_detail.first_name" class="input" placeholder="First name" type="text">
                  <span class="icon is-small is-left">
                    <i class="fas fa-book"></i>
                  </span>
                </p>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Book Type</label>
            </div>
            <div class="field-body">
              <div class="select is-primary">
                <select>
                  <option>Select dropdown</option>
                  <option>With options</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Book cover</label>
            </div>
            <div class="field-body">
              <div class="file">
                <label class="file-label">
                  <input class="file-input" name="resume" type="file">
                  <span class="file-cta">
                    <span class="file-icon">
                      <i class="fas fa-upload"></i>
                    </span>
                    <span class="file-label">
                      Choose a file…
                    </span>
                  </span>
                </label>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Short description</label>
            </div>
            <div class="field-body">
              <textarea class="textarea" placeholder="e.g. Hello world"></textarea>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Detailed description</label>
            </div>
            <div class="field-body">
              <textarea class="textarea" placeholder="e.g. Hello world"></textarea>
            </div>
          </div>
          <div class="field is-grouped is-grouped-centered">
            <p class="control">
              <a class="button is-primary">
                Submit
              </a>
            </p>
            <p class="control">
              <a class="button is-light">
                Cancel
              </a>
            </p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "author_book_create",
  methods: {},
  mounted() {
  },
  data() {
    return {
      book_detail: {
        book_name: '',
        book_image: '',
        short_description: '',
      }
    }
  }
}
</script>

<style scoped>

</style>

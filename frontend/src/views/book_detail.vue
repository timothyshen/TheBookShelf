<template>
  <div class="container">
    <div class="columns is-mobile">
      <div class="column is-three-fifths is-offset-one-fifth">
        <div class="columns">
          <div class="column is-one-quarter">
            <img/>
          </div>
          <div class="column">
            <p>
              {{ book_info.book_name }}
            </p>
            <p>
              {{ book_info.added_time }}
            </p>
            <p>
              {{ book_info.book_short_description }}
            </p>
            <p>
              {{ book_info.book_description }}
            </p>
          </div>
        </div>
        <nav class="level my-4">
          <div class="level-item has-text-centered">
            <div>
              <p class="heading">Chapters</p>
              <p class="title">{{ book_info.chapter_count }}</p>
            </div>
          </div>
          <div class="level-item has-text-centered">
            <div>
              <p class="heading">Clicks</p>
              <p class="title">{{ book_info.total_click }}</p>
            </div>
          </div>
          <div class="level-item has-text-centered">
            <div>
              <p class="heading">Votes</p>
              <p class="title">{{ book_info.total_vote }}</p>
            </div>
          </div>
          <div class="level-item has-text-centered">
            <div>
              <p class="heading">Words</p>
              <p class="title">{{ book_info.total_words }}</p>
            </div>
          </div>
        </nav>
        <div class="columns my-6">
          <div class="column">
            <div class="columns is-multiline">
              <div v-for="(chapter, index) in chapters" v-bind:key="index" class="column is-half">
                {{ chapter.chaptername }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "book_detail",

  data() {
    return {
      book_info: null,
      chapters: [
        {
          bookName: 1,
          chaptername: 'ddddd'
        }, {
          bookName: 1,
          chaptername: 'ddddd'
        }, {
          bookName: 1,
          chaptername: 'ddddd'
        }, {
          bookName: 1,
          chaptername: 'ddddd'
        }, {
          bookName: 1,
          chaptername: 'ddddd'
        }, {
          bookName: 1,
          chaptername: 'ddddd'
        }, {
          bookName: 1,
          chaptername: 'ddddd'
        },
      ]
    }
  },
  beforeCreate() {
    console.log(axios.defaults.headers.common['Authorization'])
    axios
        .get('http://127.0.0.1:8000/api/v1/detail/1')
        .then((response) => {
          console.log(response.data)
          this.book_info = response.data
        })
  },
  methods: {
    method1() {
    }
  }
}
</script>

<style scoped>

</style>

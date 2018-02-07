// Home vue

<template>
  <div>
      <p>Home page</p>
      <p>New Test from flask : {{testNumber}}</p>
      <button @click="getTest">New Test</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      testNumber: 0
    }
  },
  methods: {
    getNumberFromBackend () {
      const path = 'http://localhost:5000/api/test'
      axios.get(path)
        .then(response => {
          this.testNumber = response.data.testNumber
        })
        .catch(error => {
          console.log(error)
        })
    },
    getTest () {
      this.testNumber = this.getNumberFromBackend()
    },
    created () {
      this.getTest()
    }
  }
}
</script>

// Admin page

<template>
    <div>
        <div>
            <p>{{ msg }}</p>
        </div>
        <button @click="logout" type="primary"> 注销 </button>
    </div>
</template>

<script>
export default {
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    logout () {
      this.$store.commit('del_token')
      this.$router.push('/login')
    }
  },
  created () {
    // this.$axios.defaults.auth = this.$store.commit('get_token')
    this.$axios.get('/api/admin').then(response => {
      this.msg = response.data
    }).catch(error => {
      this.$Message.error(error)
    })
  }
}
</script>

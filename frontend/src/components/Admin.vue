// Admin page

<template>
    <div>
        <div>
            <p>{{ msg }}</p>
        </div>
        <Button @click="logout" type="primary"> 注销 </Button>
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
      this.$router.push('login')
    }
  },
  created () {
    console.log(this.$axios.defaults.auth)
    this.$axios.get('/api/admin').then(response => {
      this.msg = response.data
    }).catch(error => {
      this.$Message.error(error)
    })
  }
}
</script>

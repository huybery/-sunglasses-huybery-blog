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

import {LOGOUT} from '../store/mutation-types'

export default {
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    logout () {
      this.$store.commit(LOGOUT)
      this.$router.push('login')
      this.$Message.success('退出登录')
    }
  },
  created () {
    this.$axios.get('/api/admin').then(response => {
      this.msg = response.data
    }).catch(error => {
      this.$Message.error(error)
    })
  }
}
</script>

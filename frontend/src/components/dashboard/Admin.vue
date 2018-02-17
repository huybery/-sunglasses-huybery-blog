// Admin page

<template>
  <div>
    <!-- Header -->
    <Menu ref="menu" mode="horizontal" active-name="currentPage" @on-select="selectEvent">
      <!-- 文章管理 -->
      <MenuItem name="post">
          <Icon type="ios-paper"></Icon>
          文章管理
      </MenuItem>
      <!-- 用户管理 -->
      <MenuItem name="user">
          <Icon type="ios-people"></Icon>
          用户管理
      </MenuItem>
      <!-- 统计分析 -->
      <Submenu name="statis">
          <template slot="title">
              <Icon type="stats-bars"></Icon>
              统计分析
          </template>
          <MenuGroup title="使用">
              <MenuItem name="3-1">新增和启动</MenuItem>
              <MenuItem name="3-2">活跃分析</MenuItem>
              <MenuItem name="3-3">时段分析</MenuItem>
          </MenuGroup>
          <MenuGroup title="留存">
              <MenuItem name="3-4">用户留存</MenuItem>
              <MenuItem name="3-5">流失用户</MenuItem>
          </MenuGroup>
      </Submenu>
      <!-- 用户注销 -->
      <Submenu name="user" class="admin-nav">
        <template slot="title">
            <Icon type="happy-outline"></Icon>
            {{username}}
        </template>
        <MenuItem name="logout">
          <Icon type="log-out"></Icon>
          退出登录
        </MenuItem>
      </Submenu>
    </Menu>

  </div>
</template>

<script>

import {LOGOUT} from '@/store/mutation-types'

export default {
  data () {
    return {
      username: '',
      currentPage: ''
    }
  },
  methods: {
    logout () {
      this.$store.commit(LOGOUT)
      this.$router.push('login')
      this.$Message.success('退出登录')
    },
    selectEvent (name) {
      switch (name) {
        case 'logout':
          this.logout()
          break
        case 'post':
          console.log(this.currentPage)
      }
    }
  },
  created () {
    this.$axios.get('/api/admin').then(response => {
      this.username = response.data.username
    }).catch(error => {
      this.$Message.error(error)
    })
    console.log('router detect:', this.$route)
    let path = this.$route.fullPath.match(/^\/(.*)\//)
    this.currentPage = this.$route.name
    this.openedSubmenuArr = [].concat(path)
    this.$nextTick(() => {
      this.$refs.menu.updateOpened()
      this.$refs.menu.updateActiveName()
    })
  }
}
</script>

<style lang="less" scoped>
  .admin-nav{
    float: right;
    margin: 0 auto;
    margin-right: 20px;
  }
</style>

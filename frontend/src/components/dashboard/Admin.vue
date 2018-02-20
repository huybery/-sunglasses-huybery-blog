// Admin page

<template>
  <div>
    <!-- Header -->
    <Menu ref="headMenu" mode="horizontal" :active-name="currentPage" @on-select="selectEvent">
      <!-- 统计分析 -->
      <MenuItem name="statis">
          <Icon type="stats-bars"></Icon>
          统计分析
      </MenuItem>
      <!-- 文章管理 -->
      <MenuItem name="artical">
          <Icon type="ios-paper"></Icon>
          文章管理
      </MenuItem>
      <!-- 用户管理 -->
      <MenuItem name="user">
          <Icon type="ios-people"></Icon>
          用户管理
      </MenuItem>
      <!-- <Submenu name="statis">
          <template slot="title">
              <Icon type="stats-bars"></Icon>
              统计分析
          </template>
          <MenuGroup title="流量">
              <MenuItem name="statis">网站流量</MenuItem>
              <MenuItem name="activate">活跃分析</MenuItem>
              <MenuItem name="time">时段分析</MenuItem>
          </MenuGroup>
          <MenuGroup title="其他">
              <MenuItem name="3-4">说不定有用呢</MenuItem>
              <MenuItem name="3-5">说不定有用呢</MenuItem>
          </MenuGroup>
      </Submenu> -->
      <!-- 用户注销 -->
      <Submenu name="user" class="admin-nav">
        <template slot="title">
            <Icon type="happy-outline"></Icon>
            {{loginUser}}
        </template>
        <MenuItem name="home">
          <Icon type="home"></Icon>
          返回主页
        </MenuItem>
        <MenuItem name="logout">
          <Icon type="log-out"></Icon>
          退出登录
        </MenuItem>
      </Submenu>
    </Menu>
    <transition name="fade" mode="out-in">
      <router-view>

      </router-view>
    </transition>
  </div>
</template>

<script>
import {LOGOUT} from '@/store/mutation-types'

export default {
  name: 'headMenu',
  data () {
    let currentPage = this.$router.currentRoute.path.split('/').pop()
    return {
      LoginUser: '',
      currentPage: currentPage
    }
  },
  methods: {
    logout () {
      this.$store.commit(LOGOUT)
      this.$router.push('/login')
      this.$Message.success('退出登录')
    },
    selectEvent (active) {
      if (active === 'logout') {
        this.logout()
      } else if (active === 'home') {
        this.$router.push('/')
      } else {
        this.$router.push(active)
      }
    }
  },
  created () {
    const loginUser = this.$store.state.loginUser
    if (loginUser) {
      this.loginUser = loginUser
    } else {
      this.$Message.error('登录异常，重新登录')
      this.$router.push('/login')
    }
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

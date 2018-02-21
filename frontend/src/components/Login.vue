<template>
<div id="login" >
    <Row type="flex" justify="center">
        <Col :sm="16" :md="12" :lg="8" :xs="22">
            <Card class="form">
                <p slot="title">
                  <Icon slot="prepend" type="log-in"></Icon>
                  「 登录 」
                </p>
                <Form ref="formInline" :model="formInline" :rules="ruleInline" >
                    <FormItem prop="username">
                        <Input type="text" v-model="formInline.username" placeholder="用户名" size="large" @on-enter="handleSubmit('formInline', formInline)">
                            <Icon slot="prepend" type="person"></Icon>
                        </Input>
                    </FormItem>
                    <FormItem prop="password">
                        <Input type="password" v-model="formInline.password" placeholder="密码"  size="large" @on-enter="handleSubmit('formInline', formInline)">
                            <Icon slot="prepend" type="locked"></Icon>
                        </Input>
                    </FormItem>
                    <FormItem>
                        <Button type="info" @click="handleSubmit('formInline', formInline)" long>登录</Button>
                    </FormItem>
                </Form>
            </Card>
        </Col>
    </Row>
</div>
</template>
<script>

import * as types from '../store/mutation-types'

export default {
  name: 'login',
  data () {
    return {
      formInline: {
        username: '',
        password: ''
      },
      ruleInline: {
        username: [
          { required: true, message: '请填写用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请填写密码', trigger: 'blur' },
          { type: 'string', min: 4, message: '密码长度不能小于4位', trigger: 'blur' }
        ]
      },
      bg: {
        width: `${window.innerWidth}px`,
        height: `${window.innerHeight}px`,
        position: 'absolute'
      }
    }
  },
  methods: {
    handleSubmit (name, form) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          this.$axios.defaults.auth = {
            username: form.username,
            password: form.password
          }
          const msg = this.$Message.loading({
            content: '登录中...'
          })
          this.$axios.get('/api/login')
            .then(response => {
              msg()
              this.$Message.success('登录成功')
              let data = response.data
              // data = {
              //   token: '',
              //   loginUser: ''
              // }
              let payload = data
              this.$store.commit(types.LOGIN, payload)
              this.$router.push('/admin/statis')
            })
            .catch(error => {
              msg()
              if (error === 'Unauthorized Access') {
                this.$Message.error('账户名/密码有误!')
              }
            })
        } else {
          this.$Message.error('表单验证失败!')
        }
      })
    }
  }
}
</script>

<style lang="less" scoped>
.bg {
    position: absolute;
}
.form {
    text-align: center;
    margin-top: 150px;
    // min-width: 300px;
}
</style>

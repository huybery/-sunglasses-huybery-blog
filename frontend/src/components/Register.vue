<template>
<div id="login" >
    <Row type="flex" justify="center">
        <!-- <img src="../assets/login.jpg" alt="" :style="bg"> -->
        <Col span="8">
            <Card class="form">
                <div slot="title">
                    「 注册 」
                </div>
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
                        <Button type="ghost" @click="handleSubmit('formInline', formInline)" long>注册</Button>
                    </FormItem>
                </Form>
            </Card>
        </Col>
    </Row>
</div>
</template>
<script>

// import * as types from '../store/mutation-types'

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
          let user = {
            username: form.username,
            password: form.password
          }
          this.$axios.post('/api/register', user).then(response => {
            this.$Message.success('注册成功')
            let data = response.data
            this.$Message.success(data.username + '注册成功，请登录')
            this.$router.push('login')
          }).catch(error => {
            console.log(error)
            if (error === 'User Has Exist') {
              this.$Message.error('账号已存在!')
              this.$refs[name].resetFields()
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

<style>
.bg {
    position: absolute;
}
.form {
    text-align: center;
    margin-top: 150px;
    min-width: 300px;
    /* p {
        font-size: 30px;
    } */
}
</style>

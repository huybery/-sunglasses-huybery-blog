<template>
<div id="login" >
    <Row type="flex" justify="center">
        <Col :sm="16" :md="12" :lg="8" :xs="22">
            <Card class="form">
                <p slot="title">
                    <Icon type="person-add"></Icon>
                    「 注册 」
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
                        <Button type="ghost" @click="handleSubmit('formInline', formInline)" long>注册</Button>
                    </FormItem>
                </Form>
            </Card>
        </Col>
    </Row>
</div>
</template>
<script>

export default {
  name: 'register',
  data () {
    const validateUser = (rule, value, callback) => {
      let username = value
      if (username === '') { callback(new Error('请填写用户名')) }
      this.$axios.get('/api/user/' + username).then(response => {
        if (response.data[username]) {
          callback(new Error('用户已经存在'))
        } else {
          callback()
        }
      }).catch(error => {
        this.$Message.error(error)
        this.$refs[name].resetFields()
      })
    }
    return {
      formInline: {
        username: '',
        password: ''
      },
      ruleInline: {
        username: [
          { validator: validateUser, required: true, trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请填写密码', trigger: 'blur' },
          { type: 'string', min: 4, message: '密码长度不能小于4位', trigger: 'blur' }
        ]
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

<style lang="less" scoped>
    .form {
    text-align: center;
    margin-top: 150px;
    min-width: 300px;
}
</style>

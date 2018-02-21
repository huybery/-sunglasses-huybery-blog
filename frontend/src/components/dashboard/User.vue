
<template>
    <Row type="flex" justify="center" class="user-list">
        <Col :xs="20" :sm="16" :md="12" :lg="18">
            <Card>
                <p slot="title">
                    用户列表
                </p>
                <div class="edittable-table-height-con">
                    <can-edit-table
                        v-model="editInlineData"
                        :columns-list="editInlineColumns"
                        @on-cell-change="handleCellChange"
                        @on-delete="handleDel"
                        :editIncell="true"
                    >
                    </can-edit-table>
                </div>
            </Card>
        </Col>
    </Row>
</template>

<script>
import canEditTable from './canEditTable.vue'
export default {
  components: {
    canEditTable
  },
  data () {
    return {
      editInlineData: [],
      eiditInlineColumns: []
    }
  },
  methods: {
    getData () {
      let editInlineData = []
      this.$axios.get('/api/user').then(response => {
        const data = response.data
        for (var user of data) {
          let cellData = {
            username: user.username,
            password: user.password,
            uid: user.uid
          }
          editInlineData.push(cellData)
        }
      }).catch(err => {
        this.$Message.error(err)
      })
      return editInlineData
    },
    setData () {
      const editInlineColumns = [
        {
          title: '序号',
          type: 'index',
          align: 'center'
        },
        {
          title: '用户名',
          align: 'center',
          key: 'username',
          editable: true
        },
        {
          title: '密码',
          align: 'center',
          key: 'password',
          editable: true
        },
        {
          title: '操作',
          align: 'center',
          key: 'handle',
          handle: ['delete']
        }
      ]
      this.editInlineData = this.getData()
      this.editInlineColumns = editInlineColumns
    },
    handleDel (val, index) {
      let uid = val.uid
      this.$axios.delete('/api/user/' + uid)
        .then(response => {
          let data = response.data
          this.$Message.success('成功删除用户: ' + data.username)
        })
        .catch(err => {
          this.$Message.error(err)
        })
    },
    handleCellChange (val, index, key) {
      let uid = val[index]['uid']
      let changeAttr = val[index][key]
      let changeDict = {
        [key]: changeAttr
      }
      this.$axios.put('/api/user/' + uid, changeDict)
        .then(response => {
          let data = response.data
          if (data.err_code === 0) {
            this.$Message.success('修改了第 ' + (index + 1) + ' 行列名为 ' + key + ' 的数据')
          }
          if (data.err_code === 1) {
            this.setData()
            this.$Message.error('修改失败，用户名已存在')
          }
        })
        .catch(err => {
          this.$Message.error(err)
        })
    }
  },
  created () {
    this.setData()
  }
}
</script>

<style lang="less" scoped>
    .user-list{
        margin-top: 50px;
    }
</style>

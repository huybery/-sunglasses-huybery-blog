
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
      const editInlineAndCellData = [
        {
          name: 'Aresn',
          //   sex: '男',
          work: '前端开发'
        },
        {
          name: 'Lison',
          //   sex: '男',
          work: '前端开发'
        },
        {
          name: 'lisa',
          //   sex: '女',
          work: '程序员鼓励师'
        }
      ]
      const editInlineColumns = [
        {
          title: '序号',
          type: 'index',
          align: 'center'
        },
        {
          title: '用户名',
          align: 'center',
          key: 'name',
          editable: true
        },
        {
          title: '岗位',
          align: 'center',
          key: 'work',
          editable: true
        },
        {
          title: '操作',
          align: 'center',
          key: 'handle',
          handle: ['delete']
        }
      ]
      return [editInlineAndCellData, editInlineColumns]
    },
    setData () {
      this.editInlineData = this.getData()[0]
      this.editInlineColumns = this.getData()[1]
    },
    handleDel (val, index) {
      this.$Message.success('删除了第' + (index + 1) + '行数据')
    },
    handleCellChange (val, index, key) {
      this.$Message.success('修改了第 ' + (index + 1) + ' 行列名为 ' + key + ' 的数据')
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

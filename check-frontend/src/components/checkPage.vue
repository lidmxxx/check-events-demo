<template>
  <el-container style="height: 100%; border: 1px solid #eee">
    <!-- 侧边布局 -->
    <el-aside width="300px" style="background-color: rgb(238, 241, 246)">
      <!-- 输入表单 -->
      <el-form :model="inputForm" ref="inputFormRef"  class="input_form">
        <!-- 日期选择器 -->
        <el-form-item prop="date">
        <span class="inputdate">上报时间（必填）</span>
        <el-date-picker
          v-model="inputForm.date"
          type="date"
          placeholder="选择日期"
          value-format='yyyyMMdd'
          aria-required="true"
        >
        </el-date-picker>
        </el-form-item>
        <!-- equip_id 输入框 -->
        <el-form-item prop="equip_id">
        <span class="inputequip_id">equip_id（必填）</span>
        <el-input 
        v-model="inputForm.equip_id" 
        placeholder="请输入 equip_id" 
        aria-required="true"
        clearable />
        </el-form-item>
        <!-- 按钮 -->
        <el-form-item class="btns">
            <el-button type="primary" @click="postData">提交</el-button>
            <el-button type="info" @click="resetForm">重置</el-button>
        </el-form-item> 
        <div>
            <el-button type="text" @click="dialogTableVisible = true">查看当前支持校验的埋点</el-button>
            <el-dialog title="可校验的埋点事件名称" :visible.sync="dialogTableVisible" @open='getDetails()'>
            <el-table :data="eventsData">
            <el-table-column property="event" label="埋点事件"></el-table-column>
            </el-table>
            </el-dialog>
        </div>
       </el-form>
    </el-aside>  
  
    <el-container>
      <el-header>埋点校验</el-header>
      <el-main>
        <el-table
          :data="tableData"
          border
          style="width: 100%">
          <el-table-column
            prop="event"
            label="埋点事件"
          >
          </el-table-column>
          <el-table-column
            prop="times"
            label="出现次数"
          >
          </el-table-column>
          <el-table-column
            prop="check"
            label="是否漏报">
          </el-table-column>
          
        </el-table>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>

  export default {
    data() {
      return {
        // 输入框数据绑定
        inputForm:{
          disabledDate(time) {
          return time.getTime() > Date.now()
          },
          date: '',
          equip_id: ''
        },
        tableData:[],
        eventsData:[],
        dialogTableVisible: false
      }
    },
    // 添加行为
    methods: {
      resetForm(){
        this.$refs.inputFormRef.resetFields()
      },
      async postData(){
        const { data: res } = await this.$http.post('check-is-missed', this.inputForm)
        const newData = []
        for(let i in res){
          var resMap = {}
          resMap.event = i
          resMap.times = res[i]
          if(resMap.times != 0){
            resMap.check = '未漏报'
          }
          else{
            resMap.check = '漏报'
          }
          newData.push(resMap)
        }
        this.tableData = newData
      },
      async getDetails(){
        const { data: res } = await this.$http.get('details')
        console.log(res)
        const newData = []
        for(let i in res){
          var resMap = {}
          resMap.num = i
          resMap.event = res[i]
          newData.push(resMap)
        }
        this.eventsData = newData
      }
    }
  }

</script>

<style>
   .el-header {
    background-color: #b3c0d1;
    color: var(--el-text-color-primary);
    line-height: 60px;
  }
   .el-main {
    background-color: #e9eef3;
    color: var(--el-text-color-primary);
    text-align: center;
    height: 100%;
  }
   body > .el-container {
    margin-bottom: 40px;
    height: 100%;
  }

</style>

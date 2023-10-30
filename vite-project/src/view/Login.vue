<script setup>
import { reactive, ref } from 'vue'

const labelPosition = ref('right')

const formLabelAlign = reactive({
  name: '',
  region: '',
  type: '',
})

function handleLogin(username, password) {

}
</script>

<template>
  <div class="login">
    <el-form :label-position="labelPosition" label-width="100px" :model="formLabelAlign" style="max-width: 460px">
      <el-form-item label="账号">
        <el-input v-model="formLabelAlign.region" />
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="formLabelAlign.type" />
      </el-form-item>
    </el-form>

    <div class="register">
      <a href="#">点击注册</a>
    </div>

    <el-button type="primary" @click="handleLogin">登录</el-button>

  </div>
</template>

<style scoped></style>
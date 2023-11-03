<script setup>
import { reactive, ref } from 'vue'
import { ElNotification } from 'element-plus'

let isLoginPage = ref(true)

const labelPosition = ref('right')

const formLabelAlign = reactive({
  name: '',
  region: '',
  type: '',
})

function handleLogin(username, password) {

}

function jumpRegister() {
  isLoginPage.value = false
}

function forgetPasswd() {
  ElNotification({
    title: '忘的好',
    message: '下次别忘了',
    type: 'success',
  })
}
</script>

<template>
  <div class="box">
    <div class="login">
      <!-- 标题 -->
      <h2>AI健康助手</h2>

      <!-- 输入框 -->
      <el-form :label-position="labelPosition" label-width="100px" :model="formLabelAlign" style="max-width: 460px">
        <!--      <el-form-item label="账号">-->
        <el-input v-model="formLabelAlign.region" placeholder="用户名" class="input" />
        <!--      </el-form-item>-->
        <!--      <el-form-item label="密码">-->
        <el-input v-model="formLabelAlign.type" placeholder="密码" class="input" />
        <el-input v-model="formLabelAlign.type" placeholder="确认密码" class="input" v-if="!isLoginPage"/>
        <!--      </el-form-item>-->
      </el-form>

      <!-- 登录按钮 -->
      <el-button type="primary" @click="handleLogin" class="button" v-if="isLoginPage">
        登录
      </el-button>
      <!-- 注册按钮 -->
      <el-button type="primary" @click="handleLogin" class="button" v-else>
        注册
      </el-button>
      <div class="register" v-if="isLoginPage">
        <span @click="jumpRegister">
          点击注册
        </span>
        <span @click="forgetPasswd">
          忘记密码
        </span>
      </div>
      <div v-else>
        <span @click="isLoginPage=true">
          已有密码, 点击登录
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.box {
  background-image: url("src/images/bk.jpg");
  width: 100vw;
  height: 100vh;
  background-size: cover;
  background-position: center;
}

.login {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 10px;
  box-shadow: 10 10 20px rgba(47, 46, 46, 0.2);
  text-align: center;
}

.login h2 {
  text-align: center;
  color: #a3c5a1;
  font-size: 28px;
  margin-bottom: 10px;
}

.login .register {
  text-align: center;
}

.register {
  width: 100%;
  display: flex;
  justify-content: center;
  justify-content: space-between;
}

.login .register span {
  color: rgb(147, 170, 111);
  margin: 0 40px;
}

.login .register span:hover {
  margin-right: 10px;
  color: rgb(79, 88, 66);
  transition: all;
}

.input {
  align-items: center;
  margin-bottom: 10px;
}

.button {
  margin: 10px auto;
  width: 100%;
  height: 40px;
  font-size: 16px;
}
</style>
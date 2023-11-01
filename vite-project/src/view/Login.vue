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
  <div class="box">
  <div class="login">
    <h2>AI健康助手</h2>
    <el-form :label-position="labelPosition" label-width="100px" :model="formLabelAlign" style="max-width: 460px">
<!--      <el-form-item label="账号">-->
        <el-input v-model="formLabelAlign.region" placeholder="用户名" class="input"/>
<!--      </el-form-item>-->
<!--      <el-form-item label="密码">-->
        <el-input v-model="formLabelAlign.type" placeholder="密码" class="input"/>
<!--      </el-form-item>-->
    </el-form>

     <el-button type="primary" @click="handleLogin" class="button">登录</el-button>

    <div class="register">
      <span><a href="#">点击注册</a>  <a href="#">忘记密码</a></span>
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
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
        text-align: center;
    }

    .login h2 {
        text-align: center;
        color: #333;
        font-size: 28px;
        margin-bottom: 10px;
    }

    .login .register {
        text-align: center;
        margin-bottom: 20px;
    }

    .login .register a {
        text-decoration: none;
        color: #4169E1;
        font-size: 16px;
        margin-right: 5px;
    }

    .login .register span {
        margin-right: 10px;
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
<script setup>
import { onMounted, onUnmounted, reactive, ref } from 'vue'
import { ElNotification } from 'element-plus'
import router from '../router';
import { useUserStore } from '../store/userStore'

let cnt = ref(0)

let isLoginPage = ref(true)

let username = ref('')
let password = ref('')
let email = ref('')
let loading = ref(false)

const userStore = useUserStore()

function handleLogin(username, password) {
  loading.value = true
  userStore.loginAction(username, password)
    .finally(() => loading.value = false)
}

function jumpRegister() {
  isLoginPage.value = false
}

function forgetPasswd() {
}
function handleKeyDown(e) {
  if (e.key === 'Enter') {
    handleLogin(username.value, password.value)
  }
}
onMounted(() => {
  window.addEventListener('keydown', handleKeyDown)
})
onUnmounted(() => {
  window.removeEventListener('keydown', handleKeyDown)
})
</script>

<template>
  <div class="box">
    <div class="login">
      <!-- 标题 -->
      <h2>AI健康助手</h2>

      <!-- 输入框 -->
      <form style="max-width: 460px" class="main-form">
        <!--      <el-form-item label="账号">-->
        <input v-model="username" placeholder="用户名" class="input" />
        <!--      </el-form-item>-->
        <!--      <el-form-item label="密码">-->
        <input v-model="password" placeholder="密码" class="input" />
        <input v-model="email" placeholder="邮箱" class="input" v-if="!isLoginPage" />
        <input placeholder="" class="input tmp"  v-if="isLoginPage" />
        <!--      </el-form-item>-->
      </form>

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
        <span @click="isLoginPage = true">
          已有密码, 点击登录
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-form {
  width: 100vw; /* 设置容器宽度为视口宽度 */
  display: flex;
  flex-wrap: wrap; /* 设置换行 */
  justify-content: center;
  align-items: center;
}

.main-form .input {
  height: 30px;
  width: 80%;
  margin: 10px;
}

.main-form .tmp {
  background-color: transparent;
  border-color: transparent;
}

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
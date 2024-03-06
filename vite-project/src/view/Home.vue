<script setup>
import { service } from '../axios';
import NavBar from '../components/Home/NavBar.vue';
import { ref } from 'vue'
import { useUserStore } from '../store/userStore';
import { toast } from '../composables/utils';
import { removeCookie } from '../composables/auth';

let drawer = ref(false)
let password = ref('')
let new_password = ref('')

const toggleDrawer = (params) => {
  drawer.value = params
}

let userStore = useUserStore()

const repassword = () => {
  service.put('/user/me/password', null, {
    params: {
      password: password.value,
      new_password: new_password.value,
      id: userStore.userInfo.id
    }
  }).then(() => {
    removeCookie()
    location.reload()
    toast('修改成功', 'success')
  }).catch(() => {
    toast('密码错误', 'error')
  }).finally(() => {
    drawer.value = false
  })
}

const theme = ref(true)
const handleChangeTheme = (darkTheme) => {
  theme.value = darkTheme
}
</script>

<template>
  <div class="common-layout" :data-theme="theme ? 'dark' : 'light'">
    <el-container class="">

    <el-header class="">
      <NavBar :drawer="drawer" @onChangeTheme="handleChangeTheme" @open-drawer="toggleDrawer"></NavBar>
    </el-header> 
       
      <el-main class="min-h-[90vh]">
        <router-view></router-view>
      </el-main>
      
      <el-drawer v-model="drawer" size="50%" title="修改密码" :direction="direction" :before-close="handleClose">
        <form drawer-form>
          <input v-model="password" type="password" placeholder="密码"
            class="input input-bordered m-2 input-xs w-full max-w-xs">
          <input v-model="new_password" type="password" placeholder="新密码"
            class="input input-bordered m-2 input-xs w-full max-w-xs">
        </form>
        <el-button type="primary" @click="repassword" class="m-5">确认修改</el-button>
      </el-drawer>
    </el-container>
  </div>
</template>


<style scoped>
.main-container {
  min-height: 85vh;
  background: #666;
}

.aside {
  background-color: rgb(63, 57, 69);
}
</style>
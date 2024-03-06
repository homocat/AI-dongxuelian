<script setup>
import router from '../../router';
import { useUserStore } from '../../store/userStore'
import { getCookie, removeCookie } from '../../composables/auth'
import { showModal } from '../../composables/utils';
import { ref } from 'vue';
import { ArrowDown } from '@element-plus/icons-vue'

const props = defineProps({
  drawer: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['openDrawer', 'onChangeTheme'])
const openDrawer = () => {
  emit('openDrawer', true)
}

const userStore = useUserStore()

function toLoginPage() {
  router.push('/login')
}

function logout() {
  showModal("是否退出").then(() => {
    removeCookie()
    location.reload()
  })
}

function repassword() {
  toggleDrawer()
}

function toggleDrawer() {
  drawer.value = !drawer.value
}

const darkTheme = ref(true)
const handleChangeTheme = () => {
  darkTheme.value = !darkTheme.value
  emit('onChangeTheme', darkTheme.value)
}
</script>

<template>
  <div class="navbar bg-base-100">
      <div class="navbar-start">
        <div class="dropdown">
          <label tabindex="0" class="btn btn-ghost btn-circle">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" />
            </svg>
          </label>
          <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
            <li><router-link to="/about">home</router-link></li>
            <li><router-link to="/QA">问答</router-link></li>
            <li><router-link to="/spark">健康助手</router-link></li>
          </ul>
          <input @click="handleChangeTheme"
              type="checkbox" value="synthwave" class="ml-2 toggle theme-controller bg-amber-300 border-sky-400 [--tglbg:theme(colors.sky.500)] checked:bg-blue-300 checked:border-blue-800 checked:[--tglbg:theme(colors.blue.900)] row-start-1 col-start-1 col-span-2"/>
        </div>
      </div>
      <div class="navbar-center">
        <div class="btn btn-ghost">
          <router-link to="/blog"> blog </router-link>
        </div>

        <div class="btn btn-ghost">
          <router-link to="/QA"> 问答 </router-link>
        </div>


        <div class="btn btn-ghost">
          <router-link to="/spark"> AI健康助手 </router-link>
        </div>

      </div>
      <div class="navbar-end">
        <div>
          <div class="nouser" v-if="!userStore.userInfo.id">
            <div @click="toLoginPage">未登录, 点击登录</div>
          </div>
          <div class="user" v-else>

            <!-- 用户头像 -->
            <div class="w-32 rounded">
              <div class="block">
                <router-link to="/about">
                  <img :src="userStore.avatar" alt="" class="user-avatar">
                </router-link>
              </div>
            </div>
            <!-- 用户名 -->
            <el-dropdown class="container">
              <span class="el-dropdown-link">
                <span class="userinfo">
                  {{ userStore.userInfo.username }}
                </span>
              </span>

              <el-icon class="el-icon--right">
                <arrow-down />
              </el-icon>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
                  <el-dropdown-item @click="openDrawer">修改密码</el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </div>
        </div>
      </div>

    





    <div class="h-6" />
  </div>
</template>

<style scoped>
.block {
  max-width: 100px;
  /* 设置容器的最大宽度 */
  height: 50px;
  /* 设置容器的高度为自动，以保持图片的纵横比 */
}

.user-avatar {
  border-radius: 13%;
  border: transparent;
  box-shadow: 2px 2px 12px 1px rgba(101, 93, 93, 0.5);
  max-width: 100%;
  /* 设置图片的最大宽度为100% */
  height: 100%;
  /* 设置图片的高度为自动，以保持图片的纵横比 */
  display: block;
  /* 将图片设置为块级元素，以避免默认的行内元素间隙 */
}

.index-5 {
  margin-left: auto;
}

.container {
  align-items: center;
  padding: 10px;
  font-size: large;
}

.el-icon--right {
  color: red;
}

.container:hover {
  color: rgb(34, 141, 45);
  border: transparent;
}

.user {
  display: flex;
}
</style>
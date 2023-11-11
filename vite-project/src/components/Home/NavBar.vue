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

const emit = defineEmits(['openDrawer'])
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

</script>

<template>
  <div class="navbar">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="4">
        <router-link to="/">a </router-link>
      </el-menu-item>
      <el-menu-item index="1">
        <router-link to="/about"> 个人主页 </router-link>
      </el-menu-item>
      <el-menu-item index="3">
        <router-link to="/blog"> blog </router-link>
      </el-menu-item>
      <el-menu-item index="2">
        <router-link to="/health"> 身体数据 </router-link>
      </el-menu-item>
      <el-menu-item index="12">
        <router-link to="/spark"> AI健康助手 </router-link>
      </el-menu-item>

      <el-menu-item index="5" class="index-5">
        <div class="nouser" v-if="!userStore.userInfo.id">
          <div @click="toLoginPage">未登录, 点击登录</div>
        </div>
        <div class="user" v-else>

          <!-- 用户头像 -->
          <div class="demo-basic--circle">
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
      </el-menu-item>
    </el-menu>
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
}</style>
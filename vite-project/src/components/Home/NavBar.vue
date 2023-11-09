<script setup>
import router from '../../router';
import { useUserStore } from '../../store/userStore'
import { getCookie, removeCookie } from '../../composables/auth'
import { showModal } from '../../composables/utils';

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

      <el-menu-item index="5">
        <div class="nouser" v-if="!userStore.userInfo.id">
          <div @click="toLoginPage">未登录, 点击登录</div>
        </div>
        <div class="user" v-else>

          <!-- 用户头像 -->
          <div class="demo-basic--circle">
            <div class="block">
              <el-avatar shape="square" :size="50" src="../../../public/download.jpg" />
            </div>
          </div>
          <!-- 用户名 -->
          <el-dropdown>
            <span class="el-dropdown-link">
              <span>
                {{ userStore.userInfo.username }}
              </span>
              <el-icon class="el-icon--right">
                <arrow-down />
              </el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
                <el-dropdown-item @click="">修改密码</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-menu-item>
  </el-menu>
  <div class="h-6" />

</div></template>

<style scoped>
.el-menu-demo {
  width: 100%;
  background-color: #fff;
}

.user {
  display: flex;
}
</style>
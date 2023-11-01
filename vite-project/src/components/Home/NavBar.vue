<script setup>
import router from '../../router';

defineProps({
  username: String
})

function toLoginPage() {
 router.push('/login') 
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
        <router-link to="/todolist"> 待办清单 </router-link>
      </el-menu-item>
      <el-menu-item index="2">
        <router-link to="/health"> 身体数据 </router-link>
      </el-menu-item> 
      <el-menu-item index="12">
        <router-link to="/spark"> AI健康助手 </router-link>
      </el-menu-item> 

      <el-menu-item index="5">
        <!-- 用户头像 -->
          <div class="demo-basic--circle">
            <div class="block">
              <el-avatar shape="square" :size="50" :src="squareUrl" />
            </div>
          </div>
        <!-- 用户名 -->
        <el-dropdown>
          <span class="el-dropdown-link">
            {{ username }}
            <el-icon class="el-icon--right">
              <arrow-down />
            </el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="handleLogout" >退出登录</el-dropdown-item>
              <el-dropdown-item @click="toLoginPage">登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </el-menu-item>
    </el-menu>
    <div class="h-6" />

  </div>
</template>

<style scoped>
.el-menu-demo {
  width: 100%;
  background-color: #fff;
}
</style>
<script setup>
import NavBar from '../components/Home/NavBar.vue';
</script>

<template>
  <div class="common-layout">
    <el-container>

      <el-header class="head">
        <NavBar username="asdf"></NavBar>
      </el-header>

      <el-main class="main">
        <router-view></router-view>
      </el-main>
     
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
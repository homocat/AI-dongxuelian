<script setup>
import { ref } from 'vue';
import { useUserStore } from '../../store/userStore';

const BlogList = [1, 2, 3, 3]
const userStore = useUserStore()
const currentDate = ref(new Date())
</script>

<template>
  <div class="bloglist">
    <template v-for="blog in BlogList">
      <el-card shadow="hover" class="user-card" :body-style="{ padding: '0px' }">
        <img
          :src="userStore.avatar"
          class="image"
        />
        <div style="padding: 14px">
          <span>{{ userStore.userInfo.username }}</span>
          <div class="bottom">
            <time class="time">{{ currentDate }}</time>
            <el-button text class="button">Operating</el-button>
          </div>
        </div>
      </el-card>
    </template>
  </div>
</template>

<style scoped>
.bloglist {
  display: grid;
}
.user-card {
  width: 300px;
  height: auto;
  margin: 10px;
}
</style>
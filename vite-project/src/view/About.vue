<script setup>
import { service } from '../axios';
import { useUserStore } from '../store/userStore'
import { toast } from '../composables/utils';
import { ref } from 'vue'

const userStore = useUserStore()
const id = userStore.userInfo.id

const local = `http://127.0.0.1:8000/api/user/update-avatar/${id}`
const remote = `http://101.42.31.45/api/user/update-avatar/${id}`

function handleSuccess() {
  location.reload()
}

const currentDate = ref(new Date())
</script>

<template>
  <div class="about">
    <el-row :gutter="20" class="main-container">
      <el-col :span="8" class="left">
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
        <el-upload v-if="id > 0" class="upload-demo" drag :action="local" :on-success="handleSuccess" multiple>
          <el-icon class="el-icon--upload"><upload-filled /></el-icon>
          <div class="el-upload__text">
            拖动到这里 <em>上传图片</em>
          </div>
          <template #tip>
            <div class="el-upload__tip">
              文件小于 2 MB
            </div>
          </template>
        </el-upload>


      </el-col>
      <el-col :span="16" class="right">
        <iframe src="https://xugaoyi.com/" class="h-[100%] w-[100%]">

        </iframe>
      </el-col>
    </el-row>
  </div>
</template>

<style scoped>
.user-card {
  width: 300px;
  height: auto;
}
.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}


.right {
  display: flex;
  justify-content: center;
  align-items: center;
  height: auto;
  /* 根据需要设置容器的高度 */
}

.img-container {
  max-width: 55%;
  /* 设置容器的最大宽度 */
  height: 45%;
  /* 设置容器的高度为自动，以保持图片的纵横比 */
}

.img-container img {
  margin: 15px;
  border-radius: 3%;
  border: transparent;
  /* box-shadow: 2px 2px 12px 1px rgba(101, 93, 93, 0.5); */
  max-width: 100%;
  /* 设置图片的最大宽度为100% */
  height: 100%;
  /* 设置图片的高度为自动，以保持图片的纵横比 */
  display: block;
  /* 将图片设置为块级元素，以避免默认的行内元素间隙 */
}

.upload-demo {
  margin-top: 10px;
  width: 300px;
}
</style>
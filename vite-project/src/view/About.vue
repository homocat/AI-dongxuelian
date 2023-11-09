<script setup>
import { useUserStore } from '../store/userStore'

const userStore = useUserStore()
</script>

<template>
  <div class="about">
    <h2>about组件</h2>
    <h1>昵称: {{ userStore.userInfo.username }}</h1>
  </div>
</template>

<style scoped></style>
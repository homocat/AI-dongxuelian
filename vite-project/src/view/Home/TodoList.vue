<script setup>

import { defineProps } from 'vue'

defineProps({
  todo: {
    type: {
      title: String,
      Content: String,
      isCompleted: Boolean
    },
    required: true
  }
})
</script>
<template>
  <div class="todolist">

  <el-descriptions

   title="{{}}" :column="3" border>

    <el-descriptions-item
      label="Username"
      label-align="right"
      align="center"
      label-class-name="my-label"
      class-name="my-content"
      width="150px"
      >{{}}</el-descriptions-item
    >
    <!-- <el-checkbox v-model="todo.isCompleted">Not disabled</el-checkbox> -->
    <!-- <el-descriptions-item label="Place" label-align="right" align="center" >Suzhou</el-descriptions-item > -->
  </el-descriptions>

  </div>
</template>

<style scoped></style>
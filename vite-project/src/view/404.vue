<script setup>

</script>

<template>
  <div class="not-found">
    <el-card>
      <h2>404 Not Found</h2>
      <p>Sorry, the page you are looking for does not exist.</p>
      <el-button type="primary" @click="$router.go(-1)">Go Back</el-button>
    </el-card>
  </div>
</template>

<style scoped></style>
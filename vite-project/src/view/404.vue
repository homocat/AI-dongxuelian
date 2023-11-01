<script setup>

</script>

<template>
<!--  <div class="box2">-->
  <div class="not-found">
    <el-card class="card">
      <h2 class="title">404 Not Found</h2>
      <p class="message">页面找不到了/(ㄒoㄒ)/~~</p>
<!--      <p class="message">点击按钮原路返回</p>-->
      <el-button class="button" type="primary" @click="$router.go(-1)">返回</el-button>
    </el-card>
    </div>
<!--  </div>-->
</template>

<style scoped>

   /*.box2{
      background-image: url("src/assets/111.png");
      height: 100vh;
      width: 100vw;
      background-size: cover;
      background-position: center;
    }*/
    .not-found {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-image: url("src/images/111.png");
        width: 100vw;
        background-size: cover;
        background-position: center;
}

    .card {
        max-width: 400px;
        padding: 30px;
        text-align: center;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        background-color: rgba(255, 255, 255, 0.5);
}

    .title {
        font-size: 24px;
        color: #333;
        margin-bottom: 20px;
}

    .message {
        margin-bottom: 10px;
        color: #666;
}

    .button {
        width: 100%;
}
</style>
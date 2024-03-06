<script setup>

</script>

<template>
  <div class="scroll">
    <div class="carousel carousel-center rounded-box">
      <div class="carousel-item">
        <img src="../images/" alt="Pizza" />
      </div>
      <div class="carousel-item">
        <img src="/images/stock/photo-1565098772267-60af42b81ef2.jpg" alt="Pizza" />
      </div>
      <div class="carousel-item">
        <img src="/images/stock/photo-1572635148818-ef6fd45eb394.jpg" alt="Pizza" />
      </div>
      <div class="carousel-item">
        <img src="/images/stock/photo-1494253109108-2e30c049369b.jpg" alt="Pizza" />
      </div>
      <div class="carousel-item">
        <img src="/images/stock/photo-1550258987-190a2d41a8ba.jpg" alt="Pizza" />
      </div>
      <div class="carousel-item">
        <img src="/images/stock/photo-1559181567-c3190ca9959b.jpg" alt="Pizza" />
      </div>
      <div class="carousel-item">
        <img src="/images/stock/photo-1601004890684-d8cbf643f5f2.jpg" alt="Pizza" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.demonstration {
  color: var(--el-text-color-secondary);
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
<script setup>
import { ref } from 'vue';
import { Promotion } from '@element-plus/icons-vue'

function uploadFormData() {
    var formData = new FormData();
    var alphaArray = ['A', 'B', 'C','D','E'];
    for (var i = 0; i < alphaArray.length; i++) {
        formData.append('stop', alphaArray [i]);
    }
    formData.append("prompt", "test");
    axios({
            method: 'post',
            url: '/engines/completions',
            data: formData,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
        })
        .then(response => {
            console.log(response);
        })
        .catch(error => {
            console.error(error);
        });
}

const input = ref('')
</script>

<template>
  <div class="gpt">
    <h2>AI健康助手</h2>
    <el-input v-model="input" placeholder="Please input" />
    <el-button>
      <el-icon><Promotion /></el-icon>
    </el-button>
  </div>
</template>

<style scoped></style>
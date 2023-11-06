<script setup>
import { ref } from 'vue';
import { Promotion } from '@element-plus/icons-vue';
import axios from 'axios';
import Nahida from './Nahida/Index.vue';
Nahida

let input = ref('');
let address = ref('');
let dialogs = []
let loading = ref(false)
let sended = ref(false)

async function handleSend() {
  dialogs.push({question: input, ans: ''})
  sended.value = true
  loading.value = true
  const response = await axios.post('http://101.42.31.45/v1/ai/', null, {
    params: {
      req: input.value
    },
    responseType: 'blob'
  });

  const audioBlob = new Blob([response.data], { type: 'audio/wav' });
  const audioUrl = URL.createObjectURL(audioBlob);
  address.value = audioUrl
  
  dialogs.at(-1).ans = audioUrl
  input.value = '';
  sended.value = false
  loading.value = false
}

function playAudio() {
  audioElement.value.play()
}
</script>

<template>
  <div class="gpt">
    <h2>AI健康助手</h2>

    <!-- 对话框 -->
    <div class="dialog">
      <div class="one-message" v-for="item in dialogs">
        <div class="ans">{{ item.question.value }}</div>
        <audio :src="item.ans" ref="audioElement" controls="controls" @click="playAudio"></audio>
      </div>
    </div>

    <!-- 输入框 -->
    <el-input v-model="input"></el-input>
    <!-- 发送按钮 -->
    <el-button @click="handleSend" v-if="!sended && !loading">
      <el-icon>
        <Promotion />
      </el-icon>
    </el-button>
    <div class="loading" v-else>
      正在加载...
    </div>

    <!-- nahida -->
    <Nahida />
  </div>
</template>

<style scoped>
.dialog {
  border: 1px solid salmon;
  width: 90vw;
  height: 20vh;
}

.voice-box .voice {
  width: 100px;
  height: 50px;
}
</style>
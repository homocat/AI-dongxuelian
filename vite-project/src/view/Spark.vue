<script setup>
import { ref } from 'vue';
import { Promotion } from '@element-plus/icons-vue';
import axios from 'axios';

let inputs = [];
let input = ref('');
let address = ref('');
let loading = ref(true)
let sended = ref(false)

async function handleSend() {
  sended.value = true
  inputs.push(input.value);
  const response = await axios.post('http://101.42.31.45/v1/ai/', null, {
    params: {
      req: input.value
    },
    responseType: 'blob'
  });
  loading = false

  const audioBlob = new Blob([response.data], { type: 'audio/wav' });
  const audioUrl = URL.createObjectURL(audioBlob);
  address.value = audioUrl

  input.value = '';
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
      <!-- 输入文字 -->
      <div class="you" v-for="item in inputs">
        {{ item }}
      </div>
      <!-- AI语音 -->
      <div class="display" v-if="sended">
        <div class="voice-box" v-if="loading">
          正在加载...
        </div>
        <div class="voice" v-else>
          <audio :src='address' ref="audioElement" controls="controls" class="loaded" @click="playAudio" />
        </div>
      </div>
    </div>

    <!-- 输入框 -->
    <el-input v-model="input"></el-input>
    <!-- 发送按钮 -->
    <el-button @click="handleSend">
      <el-icon>
        <Promotion />
      </el-icon>
    </el-button>
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
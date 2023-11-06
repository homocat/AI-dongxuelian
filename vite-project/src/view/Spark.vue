<script setup>
import { ElNotification } from 'element-plus'
import { onMounted, ref } from 'vue';
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
  if (input.value === '') {
    ElNotification({
      title: '请输入',
      type: 'error',
      duration: 300
    })
    return
  }
  dialogs.push({ question: input, ans: '' })
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
  console.log(audioElement.value.src);
}

onMounted(() => {
  window.addEventListener('keydown', (e) => {
    if (loading.value && e.key === 'Enter') {
      ElNotification({
        title: '请勿重复输入',
        type: 'warning',
        duration: 300
      })
      return
    }
    if (e.key === 'Enter') {
      handleSend()
    }
  })
})
</script>

<template>
  <div class="gpt">
    <h2 class="title">AI健康助手</h2>
    <el-container>
      <el-main class="hahida">
        <!-- nahida -->
        <Nahida />
      </el-main>
      <el-aside width="70vw">

        <!-- 对话框 -->
        <div class="dialog">
          <div class="one-message" v-for="item in dialogs">
            <div class="ans">{{ item.question.value }}</div>
            <audio v-if="!loading" :src="item.ans" ref="audioElement" controls="controls" @click="playAudio"
              class="voice"></audio>
            <div v-else class="voice">loading...</div>
          </div>
        </div>

        <!-- 输入框 -->
        <input v-model="input" class="input-text" placeholder="请输入..." />
        <!-- 发送按钮 -->
        <el-button @click="handleSend" v-if="!sended && !loading" class="send-btn">
          <el-icon>
            <Promotion />
          </el-icon>
        </el-button>
        <span class="loading" v-else>
          正在加载...
        </span>

      </el-aside>
    </el-container>
  </div>
</template>

<style scoped>
.gpt {
  text-align: center;
  height: 100vh;
}

.title {
  color: sandybrown;
  margin-left: 5%;
  width: 12%;
  box-shadow: 10px 0 0 orange;
  transition: width 0.3s ease;
}

.title:hover {
  width: 15%;
  /* transition: all; */
}

.dialog {
  margin-left: 10px;
  margin-right: 30px;
  margin-top: 30px;
  padding: 10px;
  padding-top: 10px;
  box-shadow: 0px 4px 10px 5px rgba(128, 0, 0, 0.13);
  border-radius: 15px;
  height: 60vh;
  display: flex;
}

.input-text {
  padding-left: 10px;
  margin-right: 10px;
  border-radius: 10px;
  margin-top: 30px;
  width: 80%;
  height: 50px;
  font-size: 18px;
  border: none;
  box-shadow: 0px 4px 10px 5px rgba(128, 0, 0, 0.13);
  border: none;
}

.send-btn {
  display: inline;
  height: 30px;
  margin-left: 10px;
}

/* .voice-box .voice {
  width: 100px;
  height: 50px;
} */
.one-message {
  margin-left: 10px;
  margin-right: 10px;
}

.one-message .ans {
  justify-content: end;
}

.one-message .voice {
  justify-content: start;
}

.nahida {
  background-color: #f40;
}</style>
<script setup>
import { ElNotification } from 'element-plus'
import { onMounted, ref } from 'vue';
import axios from 'axios';
import Nahida from './Nahida/Index.vue';
Nahida

let input = ref('');
let address = ref('');
let dialogs = []
let loading = ref(false)
let sended = ref(false)

async function handleSend() {
  if (input.value.trim() === '') {
    ElNotification({
      title: '请输入',
      type: 'error',
      duration: 300
    })
    return
  }
  dialogs.push({question: "尊嘟假嘟? o.O"})
  const tmp = input.value
  input.value = '';
  sended.value = true
  loading.value = true
  const response = await axios.post('http://101.42.31.45/v1/ai/', null, {
    params: {
      req: tmp
    },
    responseType: 'blob'
  });

  const audioBlob = new Blob([response.data], { type: 'audio/wav' });
  const audioUrl = URL.createObjectURL(audioBlob);
  address.value = audioUrl

  dialogs.pop()
  dialogs.push({ question: tmp, ans: audioUrl })
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
        title: '请稍等',
        type: 'warning',
        duration: 300
      })
      return
    }
    if (e.key === 'Enter' && e.shiftKey) {
      handleSend()
    }
  })
})
</script>

<template>
  <div class="gpt">
    <h2 class="title">AI健康助手</h2>
    <el-container>
      <el-main>
        <!-- nahida -->
        <Nahida class="nahida" />
      </el-main>
      <el-aside width="50vw">

        <!-- 对话框 -->
        <div class="dialog">
          <div class="one-message" v-for="(item, index) in dialogs">
            <el-input v-model="item.question" disabled autosize class="ans" type="textarea" placeholder="Please input" />
            <div v-if="loading && index === dialogs.length - 1" class="voice">
              <img src="../images/Spinner-1s-200px.gif" alt="">
              <span style="color: gray; font-size: 10px;"> 加载大约需要20s </span>
            </div>
            <audio v-else :src="item.ans" ref="audioElement" controls="controls" @click="playAudio" class="voice"></audio>

          </div>
        </div>

        <!-- 输入框 -->
        <el-input v-model="input" :autosize="{ minRows: 1, maxRows: 3 }" type="textarea" placeholder="Shift + Enter 发送消息"
          class="input-text" />
      </el-aside>
    </el-container>
  </div>
</template>

<style scoped>
.gpt {
  text-align: center;
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
  height: 35vh;
  overflow: hidden;
  overflow-y: scroll;
}

.input-text {
  width: 80%;
  height: 30px;
  margin-top: 30px;
}

.one-message {
  text-align: left;
}

.one-message .voice {
  margin: 10px;
}

.send-btn {
  display: inline;
  height: 30px;
  margin-left: 10px;
}

.voice img {
  width: 55px;
  height: 50px;
  background-color: red;
}

.one-message {
  margin-left: 10px;
  margin-right: 10px;
}

.one-message .ans {
  border-radius: 10px;
  background-color: rgb(103, 174, 103);
}

.one-message .voice {
  justify-content: start;
}

.nahida {
  width: 150%;
  height: 100%;
}
</style>
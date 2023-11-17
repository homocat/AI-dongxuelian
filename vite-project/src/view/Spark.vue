<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import Nahida from './Nahida/Index.vue';
import '../../public/font_m3kibal6kh/iconfont.css'
import { toast } from '../composables/utils';
import { useUserStore } from '../store/userStore'
import { service } from '../axios';
import { splitDate } from '../composables/utils'

let input = ref('');
let address = ref('');
let dialogs = []
let loading = ref(false)
let sended = ref(false)
let isPlaying = ref(false)

const userStore = useUserStore()

async function handleSend() {
  const id = userStore.userInfo.id
  if (!id) {
    toast('请先登录', 'error')
    return
  }
  if (input.value.trim() === '' || input.value.length <= 3) {
    toast('请输入有效问题', 'warning')
    return
  }
  dialogs.push({ question: "尊嘟假嘟? o.O" })
  const tmp = input.value.replace(/[\r\n]/g, "")
  input.value = '';
  sended.value = true
  loading.value = true
  const response = await service.post('/ai/', null, {
    params: {
      req: tmp,
      current_user: id
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

function playWavFile(url) {
  const audioContext = new (window.AudioContext || window.webkitAudioContext)();
  const request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.responseType = 'arraybuffer';

  request.onload = function () {
    audioContext.decodeAudioData(request.response, function (buffer) {
      const source = audioContext.createBufferSource();
      source.buffer = buffer;
      source.connect(audioContext.destination);
      source.start(0);
    });
  };

  request.send();
}

onMounted(() => {
  window.addEventListener('keydown', (e) => {
    if (loading.value && e.key === 'Enter') {
      toast('请稍等', 'warning')
      return
    }
    if (e.key === 'Enter' && e.shiftKey) {
      handleSend()
    }
  })
})
let audio_obj = ref({})
async function playHistoryAudio(index) {
  // audio_obj.value?.pause()
  isPlaying.value = true
  const response = await service.post("/ai/play", null, {
    params: {
      current_user: userStore.userInfo.id,
      index
    },
    responseType: 'blob'
  })
  const audioBlob = new Blob([response.data], { type: 'audio/wav' });
  const audioUrl = URL.createObjectURL(audioBlob);
  address.value = audioUrl

  audio_obj.value = playWavFile(audioUrl)
}
</script>

<template>
  <div class="gpt">
    <el-container>
      <el-main class="f-position">
        <!-- nahida -->
        <Nahida class="nahida" />
      </el-main>
      <el-aside width="66vw">

        <!-- 对话框 -->
        <div class="dialog">

          <div v-for="(item, index) in userStore.history.data">
            <div class="chat chat-end">
              <div class="chat-image avatar">
                <div class="w-10 rounded-full">
                  <img alt="Tailwind CSS chat bubble component" :src="userStore.avatar" />
                </div>
              </div>
              <div class="chat-header">{{ userStore.userInfo.username }}
                <time class="text-xs opacity-50">{{ item.__data__.date }}</time>
              </div>
              <div class="chat-bubble chat-bubble-success">{{ item.__data__.question }}</div>
            </div>

            <div class="chat chat-start">
              <div class="chat-image avatar">
                <div class="w-10 rounded-full">
                  <img alt="Tailwind CSS chat bubble component" src="../images/bk.jpg" />
                </div>
              </div>
              <div v-if="isVoiceOnloading && index === dialogs.length - 1" class="loading">
                <span class="loading loading-ring loading-sm"></span>
              </div>
              <div v-else class="chat-bubble chat-bubble-neutral btn btn-neutral"
                @click="playHistoryAudio(item.__data__.index)">
                {{ item.__data__.ans }}
              </div>
              <div class="chat-header">
                AI
                <time class="text-xs opacity-50">{{ splitDate(item.__data__.date) }}</time>
              </div>
            </div>
          </div>
        </div>

        <!-- 输入框 -->
        <div class=" flex w-[100%]">
          <textarea class="input input-primary flex-1 m-10" placeholder="Shift + Enter 发送消息"></textarea>

          <button @click="handleSend" class="btn btn-primary flex-none m-10">发送</button>
        </div>
      </el-aside>
    </el-container>
  </div>
</template>

<style scoped>
@font-face {
  font-family: 'iconfont';
  src: url('../../public/font_m3kibal6kh/iconfont.ttf') format('truetype');
}

.send-btn {
  margin: 1px;
}

.iconfont {
  font-family: "iconfont" !important;
  font-size: 18px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  float: left;
  margin-left: 10px;
}

.gpt {
  text-align: center;
}


.title:hover {
  width: 15%;
  /* transition: all; */
}

.dialog {
  margin: 10px;
  padding: 10px;
  padding-top: 10px;
  box-shadow: 0px 4px 10px 5px rgba(128, 0, 0, 0.13);
  border-radius: 15px;
  height: 70vh;
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

.one-message {
  margin-left: 10px;
  margin-right: 10px;
  padding-bottom: 5px;
  width: 60%;
}

.one-message .ans {
  border-radius: 10px;
  background-color: rgb(103, 174, 103);
}

.one-message .date {
  font-size: 10px;
  border-radius: 10px;
  color: gray;
  float: right;
  margin-bottom: 15px;
}

.one-message .voice {
  padding-top: 10px;
  padding-right: 10px;
  height: 30px;
  justify-content: start;
  background-color: rgb(90, 204, 90);
  border-radius: 13px;
  box-shadow: 10 2 13 green;
}

.one-message .voice .seconds {
  font-size: 13px;
  float: right;
}

.one-message .loading img {
  font-size: 10px;
  font-weight: 100;
  width: 55px;
  height: 50px;
}

.nahida {
  /* width: 1200px; */
  height: 600px;
  flex: 1;
  /* position: center; */
}

.f-position::-webkit-scrollbar {
  display: none;
}
</style>
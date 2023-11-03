<template>
  <div>
    <audio ref="audioElement"></audio>
    <button @click="send">发送</button>
    <button @click="play">播放</button>
    <button @click="pause">暂停</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      audioContext: null,
      audioSource: null,
      isPlaying: false
    };
  },
  mounted() {
    this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
  },
  methods: {
    play() {
      if (!this.isPlaying) {
        const audioElement = this.$refs.audioElement;
        const audioURL = 'http://server-address/audio/example.wav'; // 替换为实际的服务器地址和文件路径

        audioElement.src = audioURL;
        audioElement.onloadedmetadata = () => {
          this.audioSource = this.audioContext.createMediaElementSource(audioElement);
          this.audioSource.connect(this.audioContext.destination);
          this.audioContext.resume();
          audioElement.play();
          this.isPlaying = true;
        };
      }
    },
    pause() {
      if (this.isPlaying) {
        const audioElement = this.$refs.audioElement;
        audioElement.pause();
        this.audioContext.suspend();
        this.isPlaying = false;
      }
    }
  }
};
</script>
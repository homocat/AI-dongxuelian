<script setup>
import { ref } from 'vue';
import {
  IconHeart,
  IconMessage,
  IconStar,
  IconStarFill,
  IconHeartFill,
} from '@arco-design/web-vue/es/icon';
import { useUserStore } from '../store/userStore';

const like = ref(false);
const star = ref(false);
const onLikeChange = () => {
  like.value = !like.value;
};
const onStarChange = () => {
  star.value = !star.value;
};

let commentList = ref([])
const userStore = useUserStore()
const commentHistory = userStore.comment
</script>

<template>
  <div class="QA">
    <template v-for="(item, index) in commentHistory">

    <a-comment author="Socrates" :content="item.content" :datetime="item.date">
      <template #actions>
        <span class="action" key="heart" @click="onLikeChange">
          <span v-if="like">
            <IconHeartFill :style="{ color: '#f53f3f' }" />
          </span>
          <span v-else>
            <IconHeart />
          </span>
          {{ 0 + (like ? 1 : 0) }}
        </span>
        <span class="action" key="star" @click="onStarChange">
          <span v-if="star">
            <IconStarFill style="{ color: '#ffb400' }" />
          </span>
          <span v-else>
            <IconStar />
          </span>
          {{ 3 + (star ? 1 : 0) }}
        </span>
        <span class="action" key="reply">
          <IconMessage /> Reply
        </span>
      </template>
      <template #avatar>
        <a-avatar>
          <img alt="avatar"
            src="https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/3ee5f13fb09879ecb5185e440cef6eb9.png~tplv-uwbnlip3yd-webp.webp" />
        </a-avatar>
      </template>
      <a-comment align="right"
        avatar="https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/3ee5f13fb09879ecb5185e440cef6eb9.png~tplv-uwbnlip3yd-webp.webp">
        <template #actions>
          <a-button key="0" type="secondary"> Cancel </a-button>
          <a-button key="1" type="primary"> Reply </a-button>
        </template>
        <template #content>
          <a-input placeholder="Here is you content." />
        </template>
      </a-comment>
    </a-comment>
    </template>
  </div>
</template>

<style scoped>
.action {
  display: inline-block;
  padding: 0 4px;
  color: var(--color-text-1);
  line-height: 24px;
  background: transparent;
  border-radius: 2px;
  cursor: pointer;
  transition: all 0.1s ease;
}

.action:hover {
  background: var(--color-fill-3);
}
</style>
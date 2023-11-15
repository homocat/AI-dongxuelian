<script setup>
import MindMap from "simple-mind-map";

const mindMap = new MindMap({
  el: document.getElementById('mindMapContainer'),
  data: {
    "data": {
        "text": "根节点"
    },
    "children": []
  }
});
</script>

<template>
  <div class="mindmap">
    <h2>mindmap组件</h2>
    <div id="mindMapContainer"></div>
  </div>
</template>

<style scoped></style>
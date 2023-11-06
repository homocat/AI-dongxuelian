<template>
  <canvas ref="liveCanvas" />
</template>

<script>
  import * as PIXI from 'pixi.js';
  import { Live2DModel } from 'pixi-live2d-display/cubism4';

  window.PIXI = PIXI; // 为了pixi-live2d-display内部调用

  let app; // 为了存储pixi实例
  let model; // 为了存储live2d实例

  export default {
      async mounted(){
          app = new PIXI.Application({
              view: this.$refs.liveCanvas,
              autoStart: true,
              resizeTo: window, 
              backgroundAlpha: 0,
          });

          // 打包后live2d资源会出现在dist/下，这里用相对路径就能引用到了
          model = await Live2DModel.from('../../../public/Hiyori/Hiyori.model3.json');

          app.stage.addChild(model);
          model.scale.set(0.1); // 调整缩放比例，一般原始资源尺寸非常大，需要缩小
      },

      beforeUnmount(){
          model?.destroy();
          app?.destroy();
      }
  }
</script>
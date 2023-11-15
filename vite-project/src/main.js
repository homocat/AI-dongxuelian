import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { createPinia } from 'pinia'
import ArcoVue from '@arco-design/web-vue';
import '@arco-design/web-vue/dist/arco.css';

export const pinia = createPinia()
const app = createApp(App)

app.use(router)
   .use(ElementPlus)
   .use(pinia)
   .use(ArcoVue)
   .mount('#app')

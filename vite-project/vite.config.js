import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// vite.config.js

export default defineConfig({
  server: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:80",
        // target: "http://127.0.0.1:80",
        changeOrigin: true,
      },
    }
  },
  plugins: [vue()],
});


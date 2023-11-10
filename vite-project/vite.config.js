import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// vite.config.js

export default defineConfig({
  server: {
    proxy: {
      "/api": {
        target: "http://101.42.31.45:443",
        changeOrigin: true,
      },
    }
  },
  plugins: [vue()],
});


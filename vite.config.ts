import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

import path from "path"

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 6852,
    strictPort: true
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  build: {
    outDir: "fe",
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, "index.html"),
        connectprompt: path.resolve(__dirname, "index_connection_prompt.html")
      }
    }
  },
})

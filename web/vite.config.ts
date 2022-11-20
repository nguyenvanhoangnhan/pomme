import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import path from "path"
import Components from "unplugin-vue-components/vite"
// ant design
import { AntDesignVueResolver } from "unplugin-vue-components/resolvers"

// https://vitejs.dev/config/
export default defineConfig({
    server: {
        port: 5173
    },
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "./src"),
        },
    },
    plugins: [
        vue(),
        Components({
            resolvers: [
                AntDesignVueResolver({
                    importStyle: "less",
                }),
            ],
        }),
    ],
    css: {
        preprocessorOptions: {
            less: {
                javascriptEnabled: true,
                additionalData: "@root-entry-name: default;",
                modifyVars: {
                    "primary-color": "#44af7d",
                    "border-radius-base": "0px",
                },
            },
        },
    },
})

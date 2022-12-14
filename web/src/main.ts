/* eslint-disable prettier/prettier */
import { createApp } from "vue"
import "./style.less"
import App from "./App.vue"
import router from "./router"
import { createPinia } from "pinia"
const app = createApp(App)

const pinia = createPinia()

app.use(router)
app.use(pinia)
app.mount("#app")

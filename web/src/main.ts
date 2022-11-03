/* eslint-disable prettier/prettier */
import { createApp } from "vue"
import "./style.less"
import App from "./App.vue"
import router from "./router"
import { createPinia } from "pinia"

createApp(App)
    .use(router)
    .use(createPinia())
    .mount("#app")

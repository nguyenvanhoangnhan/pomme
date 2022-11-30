import { defineStore } from "pinia"
import api from "@/api"
export const useAuthStore = defineStore({
    id: "auth",
    state: () => ({
        token: "",
        exp: 0,
        fullname: "",
        email: "",
    }),
    getters: {
        isAuthenticated(state) {
            return !!state.token
        },
    },
    actions: {
        login() {
            // handle login
        },
        logout() {
            this.token = ""
            this.exp = 0
            this.fullname = ""
            this.email = ""
            console.log("logout")
        },
    },
})

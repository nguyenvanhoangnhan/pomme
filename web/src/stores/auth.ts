import { defineStore } from "pinia"

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
            console.log("login")
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

import { defineStore } from "pinia"

export const useAuthStore = defineStore({
    id: "auth",
    state: () => ({
        token: "test",
        exp: 0,
        username: "Nhân Nguyễn",
        email: "nguyen.vh.nhan@gmail.com",
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
            this.username = ""
            this.email = ""
            console.log("logout")
        },
    },
})

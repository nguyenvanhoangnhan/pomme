import { defineStore } from "pinia"

export const useAuthStore = defineStore({
    id: "auth",
    state: () => ({
        token: "",
        exp: 0,
<<<<<<< Updated upstream
        fullName: "",
        email: "nguyen.vh.nhan@gmail.com",
    }),
=======
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
>>>>>>> Stashed changes
})

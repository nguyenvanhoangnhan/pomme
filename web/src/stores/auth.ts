import { defineStore } from "pinia"

export const useAuthStore = defineStore({
    id: "auth",
    state: () => ({
        token: "test",
        exp: 0,
        fullName: "",
        email: "nguyen.vh.nhan@gmail.com",
    }),
})

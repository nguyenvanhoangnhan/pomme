import { defineStore } from "pinia"
import { notification } from "ant-design-vue"
import api from "@/api"
export const useAuthStore = defineStore({
    id: "auth",
    state: () => ({
        data: {} as AuthData,
    }),
    getters: {
        isLoggedIn(state) {
            return !!state.data.user
        },
    },
    actions: {
        async login(data: LoginForm) {
            try {
                const { data: authData } = await api.post("/auth/login", data)
                this.data = authData
                this.saveAuthData(authData)
                notification.success({
                    message: "Thành công",
                    description: "Bạn đã đăng nhập thành công.",
                })
            } catch (error: any) {
                console.log(error)
                notification.error({
                    message: "Đăng nhập thất bại",
                    description: error.message || "Đã có lỗi xảy ra",
                })
            }
        },
        async logout() {
            try {
                await api.post("/auth/logout")
                this.data = {} as AuthData
                localStorage.removeItem("authData")
            } catch (error: any) {
                console.log(error)
            }
        },
        async register(data: RegisterForm) {
            return api.post("/auth/register", data)
        },
        saveAuthData(data: AuthData) {
            if (!data) return
            const JSONData = JSON.stringify(data)
            localStorage.setItem("authData", JSONData)
        },
        loadAuthData() {
            const JSONData = localStorage.getItem("authData")
            if (JSONData) {
                const data = JSON.parse(JSONData)
                if (data.expires_at * 1000 < Date.now()) {
                    localStorage.removeItem("authData")
                    return
                }
                this.data = data
            }
        },
    },
})

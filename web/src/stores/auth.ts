import { defineStore } from "pinia"
import { notification } from "ant-design-vue"
import api from "@/api"
export const useAuthStore = defineStore({
    id: "auth",
    state: () => ({
        data: {} as AuthData,
    }),
    getters: {
        isAuthenticated(state) {
            return !!state.data.access_token
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
            } catch (error) {
                console.log(error)
                notification.error({
                    message: "Đăng nhập thất bại",
                    description: error.response.data.message || "Đã có lỗi xảy ra",
                })
            }
        },
        async logout() {
            try {
                await api.post("/auth/logout")
                this.data = {}
                localStorage.removeItem("authData")
            } catch (error) {
                console.log(error)
            }
        },
        saveAuthData(data: AuthData) {
            if (!data) return
            const JSONData = JSON.stringify(data)
            localStorage.setItem("authData", JSONData)
        },
        loadAuthData() {
            const JSONData = localStorage.getItem("authData")
            if (JSONData) {
                this.data = JSON.parse(JSONData)
            }
        },
    },
})

import { notification } from "ant-design-vue"
import { useLoadingStore } from "./loading"
import { defineStore } from "pinia"
import api from "@/api"

export const useOrderStore = defineStore("order", {
    state: () => ({
        orders: [] as Order[],
    }),
    getters: {},
    actions: {
        async fetchOrders() {
            useLoadingStore().loadingOn()
            try {
                const { data } = await api.get("orders")
                this.orders = data
            } catch (error: any) {
                this.orders = []
                notification.error({
                    message: "Error",
                    description: error.message || "Lỗi không xác định",
                })
            }
            useLoadingStore().loadingOff()
        },
    },
})

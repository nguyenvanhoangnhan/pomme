import { notification } from "ant-design-vue"
import { useLoadingStore } from "./loading"
import { defineStore } from "pinia"
import api from "@/api"
import router from "@/router"
import { useCartStore } from "./cart"

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
        async createOrder(order: OrderForm) {
            useLoadingStore().loadingOn()
            try {
                const { data } = await api.post("orders", order)
                useCartStore().items = []
                useCartStore().updateLocalStore()
                router.push({ name: "Order Detail", params: { id: data.id } })
                notification.success({
                    message: "Success",
                    description: "Đặt hàng thành công",
                })
            } catch (error: any) {
                notification.error({
                    message: "Error",
                    description: error.message || "Lỗi không xác định",
                })
            }
            useLoadingStore().loadingOff()
        },
    },
})

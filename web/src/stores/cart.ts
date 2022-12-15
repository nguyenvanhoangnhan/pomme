import { notification } from "ant-design-vue"
import { defineStore } from "pinia"
import { useLoadingStore } from "./loading"
import api from "@/api"

export const useCartStore = defineStore({
    id: "cart",
    state: () => ({
        items: [] as UserCartProduct[],
    }),
    getters: {
        total(): number {
            return this.items.reduce((total: number, item: UserCartProduct) => {
                return total + item.pivot.quantity * ((item.price * (100 - item.discount_percent)) / 100)
            }, 0)
        },
    },
    actions: {
        async fetchCart() {
            try {
                const response = await api.get("cart")
                this.items = response.data
                this.updateLocalStore()
            } catch (error: any) {
                console.log(error)
            }
            return []
        },
        async updateLocalStore() {
            localStorage.setItem("cart", JSON.stringify(this.items))
        },
        async loadFromLocalStorage() {
            const JSONData = localStorage.getItem("cart")
            if (JSONData && JSON.parse(JSONData).length > 0) {
                this.items = JSON.parse(JSONData)
            } else {
                await this.fetchCart()
            }
        },
        async addItem(item: CartAddingForm) {
            useLoadingStore().loadingOn()
            try {
                const { data } = await api.post("cart", item)
                this.items = data
                this.updateLocalStore()
            } catch (error: any) {
                notification.error({
                    message: "Error",
                    description: error?.message || "Lỗi không xác định",
                })
                console.log(error)
            }
            useLoadingStore().loadingOff()
        },
        async removeItem(cartProductId: number) {
            useLoadingStore().loadingOn()
            try {
                const { data } = await api.delete(`cart/${cartProductId}`)
                console.log(data)
                this.items = data
                this.updateLocalStore()
            } catch (error: any) {
                notification.error({
                    message: "Error",
                    description: error?.message || "Lỗi không xác định",
                })
                console.log(error)
            }
            useLoadingStore().loadingOff()
        },
        async updateItem(productId: number, quantity: number, size: number) {
            useLoadingStore().loadingOn()
            let formData = {}
            if (size === 0) {
                formData = {
                    quantity: quantity,
                    size: null,
                }
            } else {
                formData = {
                    quantity: quantity,
                    size: size,
                }
            }
            console.log(formData)
            try {
                const { data } = await api.post(`cart/${productId}`, formData)
                this.items = data
                this.updateLocalStore()
            } catch (error: any) {
                console.log(error)
            }
            useLoadingStore().loadingOff()
        },
        async clear() {
            useLoadingStore().loadingOn()
            try {
                await api.delete(`cart`)
                this.items = []
                this.updateLocalStore()
            } catch (error: any) {
                notification.error({
                    message: "Error",
                    description: error.message || "Lỗi không xác định",
                })
                console.log(error.message)
            }
            useLoadingStore().loadingOff()
        },
    },
})

import { defineStore } from "pinia"
import api from "@/api"

export const useCartStore = defineStore({
    id: "cart",
    state: () => ({
        items: [] as UserCartProduct[],
    }),
    getters: {
        total(): number {
            return this.items.reduce((total: number, item: UserCartProduct) => {
                return total + item.pivot.quantity * item.price
            }, 0)
        },
    },
    actions: {
        async fetchCart() {
            try {
                const response = await api.get("cart")
                this.items = response.data
                localStorage.setItem("cart", JSON.stringify(response.data))
            } catch (error) {
                console.log(error)
            }
            return []
        },
        async loadFromLocalStorage() {
            const JSONData = localStorage.getItem("cart")
            if (JSONData) {
                this.items = JSON.parse(JSONData)
            } else {
                await this.fetchCart()
            }
        },
        async updateCart() {
            this.items = await this.fetchCart()
        },
        async addItem(productId: number, quantity: number, size?: string) {
            const formData = {
                product_id: productId,
                quantity: quantity,
                size: size,
            }
            try {
                await api.post("cart", formData)
            } catch (error) {
                console.log(error)
            }
            await this.updateCart()
        },
        async removeItem(productId: number) {
            try {
                await api.post(`cart/${productId}`)
            } catch (error) {
                console.log(error)
            }
            await this.updateCart()
        },
        async updateItem(productId: number, quantity: number, size?: string) {
            const formData = {
                quantity: quantity,
                size: size,
            }
            try {
                await api.put(`cart/${productId}`, formData)
            } catch (error) {
                console.log(error)
            }
            await this.updateCart()
        },
        clear() {
            this.items = []
        },
    },
})

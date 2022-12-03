import { defineStore } from "pinia"
import api from "@/api"

export const useCartStore = defineStore({
    id: "cart",
    state: () => ({
        items: [] as UserCartProduct[],
    }),
    getters: {
        total(): number {
            return this.items.reduce((total: number, item: CartItem) => total + item.price * item.quantity, 0)
        },
    },
    actions: {
        async fetchCart() {
            try {
                const response = await api.get("cart")
                return response.data
            } catch (error) {
                console.log(error)
            }
            return []
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

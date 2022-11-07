import { defineStore } from "pinia"

export const useCartStore = defineStore({
    id: "cart",
    state: () => ({
        items: [] as CartItem[],
    }),
    getters: {
        total(): number {
            return this.items.reduce((total: number, item: CartItem) => total + item.price * item.quantity, 0)
        },
    },
    actions: {
        addItem(item: CartItem) {
            this.items.push(item)
        },
        removeItem(item: CartItem) {
            this.items = this.items.filter((i) => i.id !== item.id)
        },
        clear() {
            this.items = []
        },
    },
})

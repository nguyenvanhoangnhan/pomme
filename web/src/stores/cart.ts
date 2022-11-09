import { defineStore } from "pinia"

export const useCartStore = defineStore({
    id: "cart",
    state: () => ({
        items: [
            {
                id: 1,
                name: "Shoe #1",
                price: 800000,
                thumbnailUrl: "#",
                quantity: 99,
            },
            {
                id: 2,
                name: "Shoe #2",
                price: 9999,
                thumbnailUrl: "#",
                quantity: 88,
            },
        ] as CartItem[],
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

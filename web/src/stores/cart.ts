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
        changeQuantity(item: CartItem, quantity: number) {
            const index = this.items.findIndex((i) => i.id === item.id)
            this.items[index].quantity = quantity
        },
        upQuantity(item: CartItem) {
            this.changeQuantity(item, item.quantity + 1)
        },
        downQuantity(item: CartItem) {
            this.changeQuantity(item, item.quantity - 1)
        },
        clear() {
            this.items = []
        },
    },
})

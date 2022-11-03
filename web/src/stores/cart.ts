import { defineStore } from "pinia"

export const useCartStore = defineStore({
    id: "cart",
    state: () => ({
        items: [] as CartItem[],
    }),
    getters: {
        itemsCount(): number {
            return this.items.length
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

import { defineStore } from "pinia"

export const useCartStore = defineStore({
    id: "cart",
    state: () => ({
        items: [
            {
                id: 1,
                name: "Shoe #1",
                price: 800000,
                thumbnailUrl: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
                quantity: 99,
            },
            {
                id: 2,
                name: "Shoe #2",
                price: 9999,
                thumbnailUrl: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
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

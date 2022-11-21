import { defineStore } from "pinia"

export const useCartStore = defineStore({
    id: "cart",
    state: () => ({
        items: [
            {
                product_id: 1,
                name: "Shoe #1",
                price: 800000,
                images: [
                    {
                        image_id: 1,
                        product_id: 1,
                        url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
                        is_thumbnail: true,
                    },
                ],
                type: 1,
                quantity: 99,
            },
            {
                product_id: 2,
                name: "Shoe #2",
                price: 9999,
                images: [
                    {
                        image_id: 2,
                        product_id: 2,
                        url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
                        is_thumbnail: true,
                    },
                ],
                type: 1,
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

import { defineStore } from "pinia"
export const useViewedProductsStore = defineStore({
    id: "products",
    state: () => ({
        products: [] as Product[],
    }),
    getters: {},
    actions: {
        addProduct(product: Product) {
            if (!this.products.find((p) => p.id === product.id)) {
                this.products.push(product)
            }
            if (this.products.length > 10) {
                this.products.shift()
            }
            this.saveToLocalStorage()
        },
        getFromLocalStorage() {
            const products = localStorage.getItem("viewedProducts")
            if (products) {
                this.products = JSON.parse(products)
            }
        },
        saveToLocalStorage() {
            localStorage.setItem("viewedProducts", JSON.stringify(this.products))
        },
    },
})

import { defineStore } from "pinia"
export const useViewedProductsStore = defineStore("viewed-products", {
    state: () => ({
        products: [] as ProductWithImages[],
    }),
    getters: {},
    actions: {
        addProduct(product: ProductWithImages) {
            if (!this.products.find((p) => p.id === product.id)) {
                this.products.push(product)
            }
            if (this.products.length > 10) {
                this.products.shift()
            }
            this.saveToLocalStorage()
        },
        loadFromLocalStorage() {
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

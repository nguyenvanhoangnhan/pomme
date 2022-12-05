import { defineStore } from "pinia"
import { notification } from "ant-design-vue"
import { LocationQuery } from "vue-router"
import api from "@/api"
export const useProductsStore = defineStore("products", {
    state: () => ({
        products: [] as ProductWithThumbnail[],
        current_page: 0,
        from: 0,
        last_page: 0,
        isFetchingNextPage: false,
        lovedProducts: [] as ProductWithThumbnail[],
    }),
    actions: {
        resetPagination() {
            console.log("Resetting pagination")
            this.products = []
            this.current_page = 0
            this.from = 0
            this.last_page = 0
        },
        async fetchProducts(params: LocationQuery) {
            if ((this.current_page && this.current_page === this.last_page) || this.isFetchingNextPage) return

            try {
                this.isFetchingNextPage = true
                const { data } = await api.get("/products", { params: { ...params, page: this.current_page + 1 } })
                await new Promise((resolve) => setTimeout(resolve, 500))
                this.current_page = data.current_page
                this.from = data.from
                this.last_page = data.last_page

                this.products = [...this.products, ...data.data]
            } catch (error) {
                notification.error({
                    message: "Error",
                    description: "Lỗi khi lấy danh sách sản phẩm",
                })
            } finally {
                this.isFetchingNextPage = false
            }
        },
        async toggleLoveProduct(product_id: number) {
            try {
                await api.post(`love/${product_id}`)
                // fetch loved products
                await this.fetchLovedProducts()
                console.log("Toggled love product")
            } catch (error: any) {
                notification.error({
                    message: "Error!",
                    description: error.message || "Đã có lỗi xảy ra",
                })
            }
            return false
        },
        async fetchLovedProducts() {
            try {
                const response = await api.get(`love`)
                this.lovedProducts = response.data
                localStorage.setItem("lovedProducts", JSON.stringify(response.data))
            } catch (error: any) {
                throw new Error(error)
            }
            return []
        },
        async loadFromLocalStorage() {
            const JSONData = localStorage.getItem("lovedProducts")
            if (JSONData) {
                this.lovedProducts = JSON.parse(JSONData)
            } else {
                try {
                    await this.fetchLovedProducts()
                } catch (error: any) {
                    notification.error({
                        message: "Error!",
                        description: error.message || "Đã có lỗi xảy ra",
                    })
                }
            }
        },
        isLoved(productId: number): boolean {
            return this.lovedProducts.some((product) => product.id === productId)
        },
    },
})

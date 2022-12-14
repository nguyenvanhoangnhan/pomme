import { useLoadingStore } from "@/stores/loading"
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
        async removeProduct(id: number) {
            try {
                useLoadingStore().loadingOn()
                await api.delete(`/products/${id}`)
                this.products = this.products.filter((product) => product.id !== id)
                notification.success({
                    message: "Success",
                    description: `Xóa sản phẩm #${id} thành công!`,
                })
            } catch (error) {
                notification.error({
                    message: "Error",
                    description: "Lỗi khi xóa sản phẩm",
                })
                useLoadingStore().loadingOff()
                return false
            }
            useLoadingStore().loadingOff()
            return true
        },
    },
})

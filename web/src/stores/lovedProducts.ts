import { defineStore } from "pinia"
import { notification } from "ant-design-vue"
import { useLoadingStore } from "./loading"
import api from "@/api"
export const useLovedProductsStore = defineStore("love-products", {
    state: () => ({
        lovedProducts: [] as ProductWithThumbnail[],
    }),
    actions: {
        async toggleLoveProduct(product_id: number) {
            useLoadingStore().loadingOn()
            try {
                const { data } = await api.post(`love/${product_id}`)
                this.lovedProducts = data
                console.log("Toggled love product")
            } catch (error: any) {
                notification.error({
                    message: "Error!",
                    description: error.message || "Đã có lỗi xảy ra",
                })
            }
            useLoadingStore().loadingOff()
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

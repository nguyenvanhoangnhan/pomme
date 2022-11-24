import { defineStore } from "pinia"
import api from "@/api"
export const useProductsStore = defineStore({
    id: "products",
    state: () => ({
        products: [] as string[],
        queries: {} as Record<string, string>,
    }),
    getters: {},
    actions: {
        fetchProducts(page = 1) {
            //
        },
        async fetchShoe(page = 1) {
            let [sale, price, gender, series, shape] = ["0", "0", "3", "All", "2"]
            if (this.queries.sale) sale = this.queries.sale
            if (this.queries.price) price = this.queries.price
            if (this.queries.gender) gender = this.queries.gender
            if (this.queries.series) series = this.queries.series
            if (this.queries.shape) shape = this.queries.shape
            await api.get(`shoe/filter/page/${page}/${sale}/${price}/${gender}/${series}/${shape}/`)
        },
        updateQueries(queries: Record<string, string>) {
            this.queries = queries
        },
        loveProduct(product_id: number) {
            //
        },
        unloveProduct(product_id: number) {
            //
        },
    },
})

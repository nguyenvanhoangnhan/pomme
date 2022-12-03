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
        fetchProducts(queries: Record<string, string>) {
            //
        },
        updateQueries(queries: Record<string, string>) {
            this.queries = queries
        },
        async toggleLoveProduct(product_id: number) {
            try {
                await api.post(`love/${product_id}`);
                return true;
            }
            catch (error) {
                console.log(error);
            }
            return false;
        },
        async getLovedProducts() {
            try {
                const response = await api.get(`love`);
                return response.data;
            }
            catch (error) {
                console.log(error);
            }
            return [];
        }
    },
})

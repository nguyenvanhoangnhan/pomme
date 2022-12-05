import { defineStore } from "pinia"

export const useLoadingStore = defineStore({
    id: "loading",
    state: () => ({
        isLoading: false,
    }),
    getters: {},
    actions: {
        loadingOn() {
            this.isLoading = true
        },
        loadingOff() {
            this.isLoading = false
        },
    },
})

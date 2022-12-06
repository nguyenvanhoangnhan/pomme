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
            console.log("loading on")
        },
        loadingOff() {
            this.isLoading = false
            console.log("loading off")
        },
    },
})

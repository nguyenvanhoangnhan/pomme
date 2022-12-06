<script setup lang="ts">
import { markRaw, onMounted, ref, watch } from "vue"
import { useRoute } from "vue-router"
import { useAuthStore } from "@/stores/auth"
import DefaultLayout from "@/layouts/default/index.vue"
import AdminLayout from "@/layouts/admin/index.vue"
import AuthLayout from "@/layouts/auth/index.vue"
import EmptyLayout from "@/layouts/empty/index.vue"
import HomeLayout from "@/layouts/home/index.vue"
import { useViewedProductsStore } from "@/stores/viewedProducts"
import { useProductsStore } from "./stores/products"
import { useCartStore } from "./stores/cart"
import { useLoadingStore } from "./stores/loading"
import { useLovedProductsStore } from "./stores/lovedProducts"

const auth = useAuthStore()
const cart = useCartStore()
const loading = useLoadingStore()
const loveProducts = useLovedProductsStore()
const viewedProducts = useViewedProductsStore()
auth.loadAuthData()

if (auth.isLoggedIn) {
    cart.loadFromLocalStorage()
    loveProducts.loadFromLocalStorage()
}

// handle dynamic layout
const route = useRoute()
const isLoadingLayout = ref(true)
const layouts = {
    default: DefaultLayout,
    auth: AuthLayout,
    admin: AdminLayout,
    empty: EmptyLayout,
    home: HomeLayout,
} as Record<string, typeof DefaultLayout>
const layout = ref()
watch(
    () => route.meta.layout as string | undefined,
    (layoutName: string | undefined) => {
        if (layoutName === "404") {
            layout.value = undefined
            return
        }
        try {
            layout.value = markRaw(layouts[layoutName || "default"])
        } catch (err) {
            layout.value = markRaw(layouts["default"])
        }
    },
    { immediate: true }
)

setTimeout(() => {
    isLoadingLayout.value = false
}, 400)

onMounted(() => {
    viewedProducts.loadFromLocalStorage()
})
</script>

<template>
    <div v-if="isLoadingLayout" class="loading-pomme bg-white text-primary w-screen h-screen flex justify-center items-center fixed z-[999]">
        <img src="/granny-smith-logo.svg" alt="logo" class="w-[10vw]" />
    </div>
    <div v-if="loading.$state.isLoading" class="loading bg-black bg-opacity-20 w-screen h-screen flex justify-center items-center fixed z-[999]">
        <a-spin size="large"></a-spin>
    </div>
    <Transition name="fade">
        <component v-if="!isLoadingLayout" :is="layout">
            <RouterView />
        </component>
    </Transition>
</template>

<style scoped>
/*
    Enter and leave animations can use different
    durations and timing functions.
*/
.fade-enter-active {
    transition: all 0.3s ease;
}

.fade-leave-active {
    transition: all 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>

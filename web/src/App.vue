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

const auth = useAuthStore()
auth.loadAuthData()

// handle dynamic layout
const route = useRoute()
const layouts = {
    default: DefaultLayout,
    auth: AuthLayout,
    admin: AdminLayout,
    empty: EmptyLayout,
    home: HomeLayout,
}
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

const isLoadingLayout = ref(true)
setTimeout(() => {
    isLoadingLayout.value = false
}, 400)
onMounted(() => {
    useViewedProductsStore().getFromLocalStorage()
})
</script>

<template>
    <div v-if="isLoadingLayout" class="loading bg-white text-primary w-screen h-screen flex justify-center items-center fixed z-[999]">
        <img src="/granny-smith-logo.svg" alt="logo" class="w-[10vw]" />
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

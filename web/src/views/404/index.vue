<script setup lang="ts">
import { useAuthStore } from "@/stores/auth"
import { Icon } from "@iconify/vue"
defineProps<{}>()
const auth = useAuthStore()
</script>

<template>
    <div class="404 flex flex-col justify-center items-center w-screen h-screen gap-8">
        <img src="/granny-smith-logo.svg" alt="logo" class="w-[96px]" />
        <div class="uppercase font-bold text-lg flex items-center justify-center gap-4">
            <span>404</span>
            <span class="separate-line"></span>
            <span>Page not found</span>
        </div>
        <RouterLink
            :to="auth.data.user.role === 'admin' ? { name: 'Admin' } : { name: 'Home' }"
            class="h-10 font-bold w-full max-w-[400px] bg-white border-black border-2 flex justify-center items-center text-[16px] cursor-pointer hover:text-primary hover:border-primary transition-all duration-300 group"
        >
            <span class="transition-all translate-x-2 group-hover:-translate-x-2">Trở về trang chủ</span>
            <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
        </RouterLink>
    </div>
</template>

<style lang="less" scoped>
.separate-line {
    @apply bg-slate-600 h-2/3 whitespace-nowrap;
    width: 2px;
    &__link {
        @apply flex items-center gap-1 whitespace-nowrap;
    }
}
</style>

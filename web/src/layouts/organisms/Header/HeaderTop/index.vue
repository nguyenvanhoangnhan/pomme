<script setup lang="ts">
import { useAuthStore } from "@/stores/auth"
import { useCartStore } from "@/stores/cart"
import { computed } from "@vue/reactivity"
import HeaderTopItem from "@/layouts/organisms/Header/HeaderTop/HeaderTopItem/index.vue"
const auth = useAuthStore()
const cart = useCartStore()
const name = computed(() => auth.data?.user?.name)
const handleLogout = async () => {
    localStorage.clear()
    await auth.logout()
    window.location.reload()
}
</script>

<template>
    <ul class="header__top bg-[#303030] flex items-center justify-end gap-6 pr-12 py-2">
        <HeaderTopItem title="Tra cứu đơn hàng" icon="ph:package-bold" to-view-name="Order List" />
        <HeaderTopItem title="Tìm cửa hàng" icon="ph:map-pin-bold" to-view-name="" />
        <HeaderTopItem title="Yêu thích" icon="ph:heart-bold" to-view-name="" />
        <HeaderTopItem :title="'Giỏ hàng (' + cart.items.length + ')'" icon="ph:shopping-cart-simple-bold" :to-view-name="auth.$state.data.user ? 'Cart' : 'Login'" />
        <HeaderTopItem v-if="!name" title="Đăng nhập" icon="ph:user-bold" to-view-name="Login" />
        <div v-else class="flex gap-6">
            <HeaderTopItem :title="name" icon="ph:user-bold" to-view-name="" />
            <div @click="handleLogout">
                <HeaderTopItem title="Đăng xuất" icon="ph:sign-out-bold" to-view-name="" />
            </div>
        </div>
    </ul>
</template>

<style lang="less" scoped></style>

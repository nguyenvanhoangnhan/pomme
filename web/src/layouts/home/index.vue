<script setup lang="ts">
import Header from "@/layouts/organisms/Header/index.vue"
import Footer from "@/layouts/organisms/Footer/index.vue"
import SideCart from "@/layouts/organisms/Sidecart/index.vue"
defineProps<{}>()
</script>

<template>
    <div class="__default__ min-h-screen flex flex-col">
        <Header />
        <SideCart />
        <div class="w-full max-w-[1920px] mx-auto">
            <slot />
        </div>
        <Footer />
    </div>
</template>

<style lang="less" scoped></style>

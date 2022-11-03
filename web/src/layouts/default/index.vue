<script setup lang="ts">
import Header from "@/layouts/organisms/Header/index.vue"
defineProps<{}>()
</script>

<template>
    <Header />
    <slot />
</template>

<style lang="less" scoped></style>

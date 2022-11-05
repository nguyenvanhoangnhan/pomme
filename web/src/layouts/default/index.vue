<script setup lang="ts">
import Header from "@/layouts/organisms/Header/index.vue"
defineProps<{}>()
</script>

<template>
    <div class="__default__">
        <Header />
        <slot />
    </div>
</template>

<style lang="less" scoped></style>

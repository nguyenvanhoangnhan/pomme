<script setup lang="ts">
import { Icon } from "@iconify/vue"
defineProps<{
    onClick: () => void
}>()
</script>

<template>
    <div
        @click="onClick"
        class="h-10 font-bold w-full bg-white border-black border-2 flex justify-center items-center text-[16px] cursor-pointer hover:text-primary hover:border-primary transition-all duration-300 group"
    >
        <span class="transition-all translate-x-2 group-hover:-translate-x-2"><slot /></span>
        <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
    </div>
</template>

<style lang="less" scoped></style>

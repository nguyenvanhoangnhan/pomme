<script setup lang="ts">
import { Icon } from "@iconify/vue"

defineProps<{}>()
</script>

<template>
    <div class="w-full h-full flex flex-col gap-2 justify-center items-center text-primary">
        <Icon icon="ph:wrench-duotone" class="text-[4rem]" />
        <div class="text-2xl font-bold">Coming soon...</div>
    </div>
</template>

<style lang="less" scoped></style>

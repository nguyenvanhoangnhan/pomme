<script setup lang="ts">
import { Icon } from "@iconify/vue"
import { useRouter } from "vue-router"
defineProps<{
    title: string
    toViewName?: string
    icon: string
}>()
const router = useRouter()
</script>

<template>
    <li class="flex items-center gap-[6px] text-[#fff] hover:text-green-300 cursor-pointer" @click="router.push({ name: toViewName })">
        <Icon :icon="icon" :width="20" :height="20" />
        <span>{{ title }}</span>
    </li>
</template>

<style lang="less" scoped></style>

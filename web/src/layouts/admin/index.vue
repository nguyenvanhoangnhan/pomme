<script setup lang="ts">
import AdminSidebar from "../organisms/admin/Sidebar/index.vue"
defineProps<{}>()
</script>

<template>
    <div class="__admin__ flex h-screen overflow-hidden">
        <AdminSidebar />
        <div class="flex-1 bg-white min-h-screen overflow-y-scroll px-12 py-8 relative">
            <div class="title font-bold text-2xl">
                {{ $route.meta.title }}
            </div>
            <slot />
        </div>
    </div>
</template>

<style lang="less" scoped></style>

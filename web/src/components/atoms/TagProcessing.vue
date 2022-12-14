<script setup lang="ts">
import { ClockCircleOutlined } from "@ant-design/icons-vue"
defineProps<{}>()
</script>

<template>
    <a-tag color="default">
        <template #icon>
            <clock-circle-outlined />
        </template>
        Đang xử lí
    </a-tag>
</template>

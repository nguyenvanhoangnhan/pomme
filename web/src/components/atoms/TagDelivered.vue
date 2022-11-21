<script setup lang="ts">
import { CheckCircleOutlined } from "@ant-design/icons-vue"
defineProps<{}>()
</script>

<template>
    <a-tag color="success">
        <template #icon>
            <check-circle-outlined />
        </template>
        Đã giao
    </a-tag>
</template>

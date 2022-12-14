<script setup lang="ts">
import { SyncOutlined } from "@ant-design/icons-vue"
defineProps<{}>()
</script>

<template>
    <a-tag color="processing">
        <template #icon>
            <sync-outlined />
        </template>
        Đang giao
    </a-tag>
</template>

<script setup lang="ts">
import { CloseCircleOutlined } from "@ant-design/icons-vue"
</script>

<template>
    <a-tag color="error">
        <template #icon>
            <close-circle-outlined />
        </template>
        Đã hủy
    </a-tag>
</template>

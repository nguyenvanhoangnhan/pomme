<script setup lang="ts">
import { useRoute } from "vue-router"
defineProps<{}>()
// get the product id from the route
const productId = useRoute().params.id
console.log(productId)
</script>

<template>
    <div>
        <h1>Product #{{ productId }}</h1>
        <p>This is the product page.</p>
    </div>
</template>

<style lang="less" scoped></style>

<script setup lang="ts">
defineProps<{}>()
</script>

<template>
    <!-- example: -->
    <div class="product-card">
        <div class="product-card__image">
            <img src="https://via.placeholder.com/150" alt="Product image" />
        </div>
        <div class="product-card__content">
            <h3 class="product-card__title">Product title</h3>
            <p class="product-card__description">Product description</p>
            <div class="product-card__price">$ 100</div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

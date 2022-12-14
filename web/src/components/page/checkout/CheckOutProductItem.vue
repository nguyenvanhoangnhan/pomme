<script setup lang="ts">
import { useCartStore } from "@/stores/cart"
import { Icon } from "@iconify/vue"
import { computed } from "@vue/reactivity"

const props = defineProps<{
    product: UserCartProduct
}>()

const priceAfterDiscount = computed(() => {
    return (props.product.price * (100 - props.product.discount_percent)) / 100
})
</script>

<template>
    <div class="flex gap-4">
        <div class="w-16">
            <img class="w-16 h-16 object-cover" :src="product?.thumbnail.url" />
        </div>
        <div class="flex-1 flex flex-col justify-between">
            <div class="flex justify-between text-lg font-bold">
                <span>{{ product.name }}</span>
                <span class="text-primary">{{ Number(priceAfterDiscount * product.pivot.quantity).toLocaleString() }}₫</span>
            </div>
            <div class="flex justify-between">
                <div class="flex gap-3">
                    <span>Giá: {{ Number(priceAfterDiscount).toLocaleString() }}₫ </span>
                    <span class="line-through" v-if="product.discount_percent"> {{ Number(product.price).toLocaleString() }}₫</span>
                </div>
            </div>
            <div class="flex justify-between">
                <div class="flex gap-8 font-bold">
                    <div>Số lượng: {{ product.pivot.quantity }}</div>
                    <div v-if="product.pivot.size">Size: {{ product.pivot.size }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

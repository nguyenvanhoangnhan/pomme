<script setup lang="ts">
import { Icon } from "@iconify/vue"

defineProps<{
    // eslint-disable-next-line no-undef
    orderProduct: OrderProduct
}>()
</script>

<template>
    <div class="flex gap-8 w-full">
        <div class="w-[180px]">
            <img class="w-[180px] h-[180px] object-cover" :src="orderProduct.product.images.find((item) => item.is_thumbnail)?.url" />
        </div>
        <div class="flex-1 flex flex-col justify-between text-secondary">
            <div class="text-lg font-bold">{{ orderProduct.product.name }}</div>
            <div class="flex flex-col gap-2 font-bold">
                <span>Giá: {{ Number(orderProduct.price_at_order).toLocaleString() }} </span>
                <span>Số lượng: {{ orderProduct.quantity }}</span>
                <span v-if="orderProduct.size">Size: {{ orderProduct.size }}</span>
            </div>
            <div class="text-primary text-lg font-bold">{{ Number(orderProduct.product.price * orderProduct.quantity).toLocaleString() }} VNĐ</div>
        </div>
    </div>
    <div class="divider--dashed my-2"></div>
</template>

<style lang="less" scoped></style>

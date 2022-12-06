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
            <img class="w-[180px] h-[180px] object-cover" :src="orderProduct.thumbnail.url" />
        </div>
        <div class="flex-1 flex flex-col justify-between text-secondary">
            <div class="text-lg font-bold">{{ orderProduct.name }}</div>
            <div class="flex flex-col gap-2 font-bold">
                <span>Giá: {{ Number(orderProduct.pivot.price_at_order).toLocaleString() }} </span>
                <span>Số lượng: {{ orderProduct.pivot.quantity }}</span>
                <span v-if="orderProduct.pivot.size">Size: {{ orderProduct.pivot.size }}</span>
            </div>
            <div class="text-primary text-lg font-bold">{{ Number(orderProduct.price * orderProduct.pivot.quantity).toLocaleString() }}₫</div>
        </div>
    </div>
    <div class="divider--dashed my-2"></div>
</template>

<style lang="less" scoped></style>

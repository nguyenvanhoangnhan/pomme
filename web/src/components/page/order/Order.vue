<script setup lang="ts">
defineProps<{
    order: Order
}>()
</script>

<template>
    <RouterLink :to="{ name: 'Order Detail', params: { id: order.order_id } }">
        <div class="order flex cursor-pointer text-black group transition-all">
            <div class="order__image w-[180px] h-[180px] overflow-hidden">
                <img :src="order.products[0].product.images[0].url" alt="order image" class="cover group-hover:scale-110 transition-all" />
            </div>
            <div class="flex flex-col gap-2 p-4" style="width: calc(100% - 180px - 16px - 60px)">
                <div class="order__name font-bold text-xl text-ellipsis overflow-hidden whitespace-nowrap">
                    <span v-for="product in order.products" :key="product.product_id">
                        {{ product.product.name }}
                        <span v-if="product !== order.products[order.products.length - 1]">, </span>
                    </span>
                    <br />
                    <TagProcessing v-if="order.status === 0" />
                    <TagShipping v-if="order.status === 1" />
                    <TagDelivered v-if="order.status === 2" />
                </div>
                <div class="order__total font-bold text-primary text-xl">{{ Number(order.total).toLocaleString() }} VNĐ</div>
            </div>
        </div>
        <div class="divider--dashed py-4"></div>
    </RouterLink>
</template>

<style lang="less" scoped></style>

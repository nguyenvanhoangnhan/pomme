<script setup lang="ts">
import TagCanceled from "@/components/atoms/TagCanceled.vue"
defineProps<{
    order: Order
}>()
</script>

<template>
    <RouterLink :to="{ name: 'Order Detail', params: { id: order.id } }">
        <div class="order flex cursor-pointer text-black group transition-all">
            <div class="order__image w-[180px] h-[180px] overflow-hidden">
                <img :src="order.image_url" alt="order image" class="cover group-hover:scale-110 transition-all" />
            </div>
            <div class="flex flex-col gap-2 p-4" style="width: calc(100% - 180px - 16px - 60px)">
                <div class="order__name font-bold text-xl text-ellipsis overflow-hidden whitespace-nowrap">
                    <span> {{ order.name }}</span>
                    <br />
                    <TagProcessing v-if="order.status === 'pending'" />
                    <TagShipping v-if="order.status === 'shipping'" />
                    <TagDelivered v-if="order.status === 'delivered'" />
                    <TagCanceled v-if="order.status === 'canceled'" />
                </div>
                <div class="order__total font-bold text-primary text-xl">{{ Number(order.total_price + order.delivery_fee).toLocaleString() }}₫</div>
            </div>
        </div>
        <div class="divider--dashed py-4"></div>
    </RouterLink>
</template>

<style lang="less" scoped></style>

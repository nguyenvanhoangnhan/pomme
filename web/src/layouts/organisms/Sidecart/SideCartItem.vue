<script setup lang="ts">
defineProps<{
    item: UserCartProduct
}>()
</script>

<template>
    <li class="list-none">
        <div class="flex">
            <img :src="item?.thumbnail?.url" alt="#" class="item-thumbnail w-20 h-20 object-cover mr-[10px]" />
            <div class="item-info w-[180px] h-[80px] flex flex-col justify-between">
                <div class="name font-bold text-base leading-[1.1] text-2-line">{{ item.name }}</div>
                <div class="text-[12px] leading-[1.1]">
                    <div class="price w-full flex justify-between">
                        <span class="current-price font-bold">{{ Number((item.price * (100 - item.discount_percent)) / 100).toLocaleString() }}₫</span>
                        <span v-if="item.discount_percent" class="price-before-sale line-through">{{ Number(item.price).toLocaleString() }}</span>
                    </div>
                    <div class="quantity flex w-full justify-between">
                        <span>Số lượng</span>
                        <span>{{ item.pivot.quantity }}</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="divider--dashed my-4"></div>
    </li>
</template>

<style lang="less" scoped></style>

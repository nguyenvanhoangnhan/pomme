<script setup lang="ts">
import { Icon } from "@iconify/vue"

defineProps<{}>()
</script>

<template>
    <div class="w-full flex flex-col items-center gap-4 pt-16">
        <router-view />
        <div class="text-2xl font-bold">Chọn loại sản phẩm muốn thêm</div>
        <div class="flex flex-col lg:flex-row gap-4">
            <router-link :to="{ name: 'Product Management - Create Shoe' }">
                <div class="product-select-card">
                    Giày
                    <Icon icon="mdi:shoe-print" class="text-[2rem]" />
                </div>
            </router-link>
            <router-link :to="{ name: 'Product Management - Create Accessory' }">
                <div class="product-select-card">
                    Phụ kiện
                    <Icon icon="tabler:icons" class="text-[2rem]" />
                </div>
            </router-link>
            <router-link :to="{ name: 'Product Management - Create Clothes' }">
                <div class="product-select-card">
                    Áo quần
                    <Icon icon="icon-park-outline:clothes-crew-neck" class="text-[2rem]" />
                </div>
            </router-link>
        </div>
    </div>
</template>

<style lang="less" scoped>
.product-select-card {
    @apply p-8 border-dashed border-primary rounded-lg w-48 h-48 flex flex-col justify-center items-center font-bold text-lg transition-all cursor-pointer hover:scale-110 hover:bg-primary hover:text-white;
    border-width: 3px;
}
</style>

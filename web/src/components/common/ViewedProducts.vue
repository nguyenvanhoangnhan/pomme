<script setup lang="ts">
import { Carousel, Slide, Navigation } from "vue3-carousel"
import { useViewedProductsStore } from "@/stores/viewedProducts"
import { computed } from "@vue/reactivity"
const viewedProducts = computed(() => useViewedProductsStore().products)
const PRODUCT_TYPES = {
    shoe: "Shoe",
    accessory: "Accessory",
    clothes: "Clothes",
} as Record<string, string>
</script>

<template>
    <div class="w-full flex flex-col gap-3">
        <div class="font-bold text-2xl uppercase text-center">Sản phẩm đã xem</div>
        <Carousel v-if="viewedProducts.length !== 0" id="thumbnails" :wrap-around="true" :items-to-show="5" :mouse-drag="false" class="p-1">
            <Slide v-for="(product, index) in viewedProducts || 0" :key="index" :index="index">
                <div class="carousel__item overflow-hidden w-full m-1 cursor-pointer" @click="$router.push({ name: PRODUCT_TYPES[product.type] + ' Detail', params: { id: product.id } })">
                    <img :src="product.images.find((item) => item.is_thumbnail)?.url" alt="#" class="hover:scale-110 transition-all duration-300" />
                </div>
            </Slide>
            <template #addons>
                <Navigation />
            </template>
        </Carousel>
    </div>
</template>

<style lang="less" scoped></style>

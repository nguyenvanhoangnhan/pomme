<script setup lang="ts">
import { Carousel, Slide, Navigation, Pagination } from "vue3-carousel"
defineProps<{}>()
const images = ["/images/home/carousel/0.png", "/images/home/carousel/1.webp", "/images/home/carousel/2.webp"]
</script>

<template>
    <Carousel id="home__gallery" :items-to-show="1" :wrap-around="true" :mouse-drag="true" class="home__gallery w-full mx-auto">
        <Slide v-for="(image, index) in images" :key="index" :index="index">
            <div class="carousel__item w-full">
                <img :src="image" class="w-full aspect-[32/9] object-cover" />
            </div>
        </Slide>
        <template #addons>
            <Navigation />
            <Pagination class="custom-position-pagination" />
        </template>
    </Carousel>
</template>

<style lang="less" scoped></style>

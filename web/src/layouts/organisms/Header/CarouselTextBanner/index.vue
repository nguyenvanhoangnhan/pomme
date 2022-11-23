<script setup lang="ts">
import { ref } from "vue"
import { Carousel, Slide, Navigation, Pagination } from "vue3-carousel"
import "vue3-carousel/dist/carousel.css"

const texts = ref(["Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "Tempore laborum illo temporibus?", "Laborum facilis omnis commodi.", "Harum, similique?"])
</script>

<template>
    <div class="w-full bg-[#F1F1F1]">
        <Carousel id="gallery" :items-to-show="1" :wrap-around="true" class="py-3 w-full lg:w-2/3 mx-auto">
            <Slide v-for="(text, index) in texts" :key="index" :index="index">
                <div class="carousel__item flex items-center justify-center italic text-base uppercase">
                    {{ text }}
                </div>
            </Slide>
            <template #addons>
                <Navigation />
            </template>
        </Carousel>
    </div>
</template>

<style lang="less" scoped></style>

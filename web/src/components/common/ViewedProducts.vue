<script setup lang="ts">
import { useRouter } from "vue-router"
import { ref } from "vue"
import { Carousel, Slide, Navigation, Pagination } from "vue3-carousel"
const viewedProducts = ref<Product[]>([
    {
        product_id: 1,
        name: "Shoe #1",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 1,
                product_id: 1,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 2,
                product_id: 1,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
    {
        product_id: 1,
        name: "Shoe #2",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 3,
                product_id: 2,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 4,
                product_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
    {
        product_id: 1,
        name: "Shoe #2",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 3,
                product_id: 2,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 4,
                product_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
    {
        product_id: 1,
        name: "Shoe #2",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 3,
                product_id: 2,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 4,
                product_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
    {
        product_id: 1,
        name: "Shoe #2",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 3,
                product_id: 2,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 4,
                product_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
    {
        product_id: 1,
        name: "Shoe #2",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 3,
                product_id: 2,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 4,
                product_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
    {
        product_id: 1,
        name: "Shoe #2",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 3,
                product_id: 2,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 4,
                product_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
    {
        product_id: 1,
        name: "Shoe #2",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 3,
                product_id: 2,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 4,
                product_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
    {
        product_id: 1,
        name: "Shoe #2",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 3,
                product_id: 2,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 4,
                product_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
    {
        product_id: 1,
        name: "Shoe #2",
        price: 100000,
        sale_percent: 0,
        in_stock: 10,
        images: [
            {
                image_id: 3,
                product_id: 2,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
            {
                image_id: 4,
                product_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
            },
        ],
        type: 1,
    },
])
const PRODUCT_TYPES = {
    "1": "Shoe",
    "2": "Accessory",
    "3": "Clothes",
}
</script>

<template>
    <div class="w-full flex flex-col gap-3">
        <div class="font-bold text-2xl uppercase text-center">Sản phẩm đã xem</div>
        <Carousel id="thumbnails" :wrap-around="true" :items-to-show="5" :mouse-drag="false" class="p-1">
            <Slide v-for="(product, index) in viewedProducts || 0" :key="index" :index="index">
                <div class="carousel__item overflow-hidden w-full m-1 cursor-pointer" @click="$router.push({ name: PRODUCT_TYPES[product.type] + ' Detail', params: { id: product.product_id } })">
                    <img
                        :src="
                            product.images.find((item) => {
                                return item.is_thumbnail === true
                            })?.url
                        "
                        alt="#"
                        class="hover:scale-110 transition-all duration-300"
                    />
                </div>
            </Slide>
            <template #addons>
                <Navigation />
            </template>
        </Carousel>
    </div>
</template>

<style lang="less" scoped></style>

<script setup lang="ts">
import { ref } from "vue"
defineProps<{}>()
const products = ref<Product[]>([
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
</script>

<template>
    <div class="flex gap-4 max-w-[1200px] mx-auto">
        <div class="left">
            <SideFilter />
        </div>
        <div class="right flex-1 flex flex-col gap-8">
            <div class="w-full aspect-[32/9] overflow-hidden px-2">
                <img src="/images/image5.jpg" alt="#" class="w-full h-full object-cover object-top" />
            </div>
            <div class="flex w-full flex-wrap">
                <ProductCard v-for="product in products" :key="product.product_id" :product="product" />
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

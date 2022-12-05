<script setup lang="ts">
import { onMounted, reactive } from "vue"
import { useRoute } from "vue-router"
import { useProductsStore } from "@/stores/products"
import { Icon } from "@iconify/vue"
defineProps<{}>()

const route = useRoute()
const products = useProductsStore()

onMounted(async () => {
    products.resetPagination()
    products.fetchProducts(route.query)
})

// if scroll to bottom, fetch more products
const handleScroll = () => {
    if (window.scrollY + window.innerHeight >= document.body.scrollHeight - 300) {
        products.fetchProducts(route.query)
    }
}
window.addEventListener("scroll", handleScroll)
</script>

<template>
    <div class="flex gap-4 max-w-[1200px] mx-auto">
        <div class="left">
            <SideFilter />
        </div>
        <div class="right flex-1 flex flex-col gap-8">
            <!-- <div class="w-full aspect-[32/9] overflow-hidden px-2">
                <img src="/images/image5.jpg" alt="#" class="w-full h-full object-cover object-top" />
            </div> -->
            <div class="flex w-full flex-wrap">
                <ProductCard v-for="product in products.$state.products" :key="product.id" :product="product" />
                <div class="no-data w-full flex flex-col items-center gap-8 text-2xl font-bold mt-16" v-if="products.$state.products.length === 0 && !products.$state?.isFetchingNextPage">
                    <Icon icon="ph:heart-straight-break" :width="72" :height="72"></Icon>
                    <div>Không có sản phẩm phù hợp</div>
                </div>
                <template v-if="products.$state?.isFetchingNextPage">
                    <div v-for="index in 9" :key="index" class="product-skeleton px-2 pt-[3px] mb-4 w-1/3 flex flex-col items-center gap-2">
                        <a-skeleton-avatar :active="true" class="ant-skeleton-full-square" shape="square" />
                        <a-skeleton-button :active="true"></a-skeleton-button>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

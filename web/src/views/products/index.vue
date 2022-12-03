<script setup lang="ts">
import { onMounted, reactive, ref } from "vue"
// import axios from "axios"
import api from "@/api"
import { useRoute } from "vue-router"
defineProps<{}>()
const route = useRoute()
const products = ref<ProductWithThumbnail[]>([])
const pagination = reactive({
    isFetchingNextPage: false,
    current: 1,
    isEnd: false,
})

onMounted(async () => {
    const { data } = await api.get("/product/page/1/")
    pagination.current += 1
    products.value = data.data as Product[]
})

// on scroll to bottom fetch more data
window.addEventListener("scroll", async () => {
    if (window.innerHeight + window.scrollY >= document.body.scrollHeight) {
        if (pagination.isEnd) return
        pagination.isFetchingNextPage = true
        await new Promise((resolve) => setTimeout(resolve, 500))
        const { data } = await api.get(`/product/page/${pagination.current}/`)
        pagination.isFetchingNextPage = false
        if (data.data.length > 0) {
            pagination.current += 1
            products.value = [...products.value, ...data.data]
        } else {
            pagination.isEnd = true
        }
    }
})
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
                <ProductCard v-for="product in products" :key="product.id" :product="product" />
                <template v-if="pagination.isFetchingNextPage">
                    <div v-for="index in 3" :key="index" class="product-skeleton px-2 pt-[3px] mb-4 w-1/3 flex flex-col items-center gap-2">
                        <a-skeleton-avatar :active="true" :size="282" shape="square" />
                        <a-skeleton-button :active="true"></a-skeleton-button>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

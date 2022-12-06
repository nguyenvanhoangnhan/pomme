<script setup lang="ts">
import { computed, onMounted, ref } from "vue"
import { Icon } from "@iconify/vue"
import { useRoute } from "vue-router"
import { Carousel, Slide, Navigation, Pagination } from "vue3-carousel"
import "vue3-carousel/dist/carousel.css"
import ViewedProducts from "@/components/common/ViewedProducts.vue"
import { useViewedProductsStore } from "@/stores/viewedProducts"
import router from "@/router"

import NoImg from "@/assets/NoImage"
import api from "@/api"
import { useLoadingStore } from "@/stores/loading"
import { useLovedProductsStore } from "@/stores/lovedProducts"
defineProps<{}>()

const loveProducts = useLovedProductsStore()

const productId = useRoute().params.id
const accessory = ref<AccessoryWithProduct | null>()
const currentSlide = ref(0)
const isFetched = ref(false)

const slideTo = (val: number) => {
    currentSlide.value = val
}

const toggleLove = async () => {
    await loveProducts.toggleLoveProduct(Number(productId))
}
const isLoved = computed(() => {
    return loveProducts.isLoved(Number(productId))
})

const fetchData = async () => {
    try {
        const { data } = await api.get(`/products/accessories/${productId}/`)
        accessory.value = data as AccessoryWithProduct
        if (accessory.value.product.images.length == 0) {
            accessory.value.product.images = [...NoImg]
        }
        await new Promise((resolve) => setTimeout(resolve, 500))
        isFetched.value = true
    } catch (err) {
        console.log(err)
        router.replace("/404")
    }
}

const toCapFirst = (str: string) => {
    return str.charAt(0).toUpperCase() + str.slice(1)
}

onMounted(async () => {
    await fetchData()
    if (accessory.value) {
        useViewedProductsStore().addProduct(accessory.value.product)
    }
})
</script>

<template>
    <div class="product max-w-[1200px] mx-auto">
        <div class="product__breadcrumb text-lg px-1">
            <div>
                <a-breadcrumb>
                    <a-breadcrumb-item><RouterLink :to="{ name: 'Products', query: { type: 'accessory' } }">Phụ kiện</RouterLink></a-breadcrumb-item>
                    <a-breadcrumb-item
                        ><RouterLink :to="{ name: 'Products', query: { type: 'accessory', category: accessory?.category } }">{{ accessory?.category }}</RouterLink></a-breadcrumb-item
                    >
                    <a-breadcrumb-item>{{ accessory?.product.name }}</a-breadcrumb-item>
                </a-breadcrumb>
            </div>
        </div>
        <div class="px-1">
            <div class="divider--solid mt-2 mb-6"></div>
        </div>
        <div class="product__detail flex-col lg:flex-row flex w-full gap-12">
            <div class="product__detail__left w-full lg:w-[640px]">
                <div v-if="!isFetched" class="skeleton flex flex-col gap-2">
                    <a-skeleton-avatar :active="true" :size="640" shape="square" />
                    <div class="flex gap-2">
                        <a-skeleton-avatar :active="true" :size="208" shape="square" />
                        <a-skeleton-avatar :active="true" :size="208" shape="square" />
                        <a-skeleton-avatar :active="true" :size="208" shape="square" />
                    </div>
                </div>
                <Carousel v-if="isFetched" id="gallery" :items-to-show="1" :wrap-around="true" v-model="currentSlide" class="p-1">
                    <Slide v-for="index in accessory?.product.images.length || 0" :key="index - 1" :index="index">
                        <div class="carousel__item w-full aspect-square p-1">
                            <img :src="accessory?.product.images[index - 1].url" alt="#" class="w-full aspect-square object-cover" />
                        </div>
                    </Slide>
                    <template #addons>
                        <Navigation />
                    </template>
                </Carousel>

                <Carousel v-if="isFetched" id="thumbnails" :wrap-around="true" :items-to-show="3" :mouse-drag="false" v-model="currentSlide" class="p-1">
                    <Slide v-for="index in accessory?.product.images.length || 0" :key="index - 1" :index="index">
                        <div class="carousel__item" @click="slideTo(index - 1)">
                            <img :src="accessory?.product.images[index - 1].url" alt="#" class="p-1" />
                        </div>
                    </Slide>
                    <template #addons>
                        <Navigation />
                        <Pagination />
                    </template>
                </Carousel>
            </div>
            <div class="product__detail__right flex-1">
                <div class="font-black text-3xl uppercase mb-4">
                    {{ accessory?.product.name }}
                </div>
                <div class="text-base mb-4">Mã sản phẩm: {{ accessory?.product_id }}</div>
                <div class="text-2xl font-bold text-primary">{{ Number(accessory?.product.price).toLocaleString() }}₫</div>
                <!--  -->
                <div class="divider--dashed my-6"></div>
                <!--  -->
                <div class="lorem">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam saepe, ipsum minima deleniti iusto dicta officiis doloribus iste. Aliquam praesentium hic harum quia asperiores
                    perspiciatis omnis distinctio culpa odit. Laudantium, placeat nostrum modi omnis, necessitatibus explicabo perferendis impedit minima harum fuga rem. Possimus nemo ipsam quas magni
                    porro aliquam dignissimos maxime voluptatem, sit adipisci quia neque assumenda reiciendis vitae, dolorem laudantium accusantium eligendi quo praesentium quos nam architecto at.
                </div>
                <!--  -->
                <div class="divider--dashed my-6"></div>
                <!--  -->
                <div class="grid grid-cols-2 gap-y-4 gap-x-2 mb-4">
                    <div class="font-black text-2xl uppercase">Số lượng</div>
                    <div></div>
                    <AInputNumber min="0" style="width: 100%" size="large" />
                    <div></div>
                </div>
                <!--  -->
                <div class="grid grid-row-2 grid-cols-4 gap-x-2 gap-y-2">
                    <div class="col-span-3 button bg-primary text-white">Thêm vào giỏ hàng</div>
                    <div class="col-span-1 button bg-black text-primary" @click="toggleLove">
                        <Icon icon="ph:heart-straight-fill" :color="isLoved ? '#44AF7D' : 'white'" :width="30" :height="30" />
                    </div>
                </div>
                <!--  -->
                <div class="my-8">
                    <div class="font-bold text-xl text-primary uppercase">Thông tin sản phẩm</div>
                    <ul>
                        <li>Loại sản phẩm: {{ accessory?.category }}</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="divider--dashed my-8"></div>
        <ViewedProducts />
    </div>
</template>

<style lang="less" scoped>
.button {
    @apply flex justify-center py-5 items-center font-black text-xl uppercase cursor-pointer;
}
</style>

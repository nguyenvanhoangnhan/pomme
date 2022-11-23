<script setup lang="ts">
import { ref, watch } from "vue"
import { Icon } from "@iconify/vue"
import { useRoute } from "vue-router"
import { Carousel, Slide, Navigation, Pagination } from "vue3-carousel"
import "vue3-carousel/dist/carousel.css"
import ViewedProducts from "@/components/common/ViewedProducts.vue"
defineProps<{}>()
// get the product id from the route
const productId = useRoute().params.id

const clothes = ref<Clothes | null>({
    clothes_id: 1,
    product_id: 1,
    category: 1,
    product: {
        product_id: 1,
        name: "Tee shirt #1",
        price: 99999999,
        sale_percent: 0,
        in_stock: 100,
        images: [
            {
                product_id: 1,
                image_id: 1,
                is_thumbnail: true,
                url: "https://ananas.vn/wp-content/uploads/pro_AGT0020_4-1.jpg",
            },
            {
                product_id: 1,
                image_id: 2,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/pro_AGT0020_4-1.jpg",
            },
            {
                product_id: 1,
                image_id: 3,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/pro_AGT0020_4-1.jpg",
            },
            {
                product_id: 1,
                image_id: 4,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/pro_AGT0020_4-1.jpg",
            },
            {
                product_id: 1,
                image_id: 5,
                is_thumbnail: false,
                url: "https://ananas.vn/wp-content/uploads/pro_AGT0020_4-1.jpg",
            },
        ],
        type: 2,
    },
})
const currentSlide = ref(0)

const slideTo = (val: number) => {
    currentSlide.value = val
}

const CATEGORIES = {
    0: "N/A",
    1: "Áo thun",
    2: "Áo hoodie",
    3: "Áo dài tay",
}
</script>

<template>
    <div class="product max-w-[1200px] mx-auto">
        <div class="product__breadcrumb text-lg px-1">
            <div>
                <a-breadcrumb>
                    <a-breadcrumb-item><a href="/products?type=2">Phụ kiện</a></a-breadcrumb-item>
                    <a-breadcrumb-item
                        ><a href="#">{{ CATEGORIES[clothes?.category === undefined ? 0 : clothes?.category] }}</a></a-breadcrumb-item
                    >
                    <a-breadcrumb-item>{{ clothes?.product?.name }}</a-breadcrumb-item>
                </a-breadcrumb>
            </div>
        </div>
        <div class="px-1">
            <div class="divider--solid mt-2 mb-6"></div>
        </div>
        <div class="product__detail flex-col lg:flex-row flex w-full gap-12">
            <div class="product__detail__left w-full lg:w-[640px]">
                <Carousel id="gallery" :items-to-show="1" :wrap-around="true" v-model="currentSlide" class="p-1">
                    <Slide v-for="index in clothes?.product.images.length || 0" :key="index - 1" :index="index">
                        <div class="carousel__item w-full aspect-square p-1">
                            <img :src="clothes?.product.images[index - 1].url" alt="#" class="w-full aspect-square object-cover" />
                        </div>
                    </Slide>
                    <template #addons>
                        <Navigation />
                    </template>
                </Carousel>

                <Carousel id="thumbnails" :wrap-around="true" :items-to-show="3" :mouse-drag="false" v-model="currentSlide" class="p-1">
                    <Slide v-for="index in clothes?.product.images.length || 0" :key="index - 1" :index="index">
                        <div class="carousel__item" @click="slideTo(index - 1)">
                            <img :src="clothes?.product.images[index - 1].url" alt="#" class="p-1" />
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
                    {{ clothes?.product.name }}
                </div>
                <div class="text-base mb-4">Mã sản phẩm: {{ clothes?.product_id }}</div>
                <div class="text-2xl font-bold text-primary">{{ Number(clothes?.product.price).toLocaleString() }} VNĐ</div>
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
                    <div class="col-span-3 button bg-black text-white">Thêm vào giỏ hàng</div>
                    <div class="col-span-1 button bg-black text-primary">
                        <Icon icon="ph:heart-straight-fill" color="white" :width="30" :height="30" />
                    </div>
                    <div class="col-span-4 button bg-primary text-white">Thanh toán</div>
                </div>
                <!--  -->
                <div class="my-8">
                    <div class="font-bold text-xl text-primary uppercase">Thông tin sản phẩm</div>
                    <ul>
                        <li>Loại sản phẩm: {{ CATEGORIES[clothes?.category === undefined ? 0 : clothes?.category] }}</li>
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

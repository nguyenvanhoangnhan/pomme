<script setup lang="ts">
import { useCartStore } from "@/stores/cart"
import { Icon } from "@iconify/vue"
import NavButton from "@/components/atoms/NavButton.vue"
import { useLoadingStore } from "@/stores/loading"
import { Modal } from "ant-design-vue"
import { useLovedProductsStore } from "@/stores/lovedProducts"
import WishListItem from "@/components/page/wishlist/WishListItem.vue"
defineProps<{}>()

const lovedProducts = useLovedProductsStore()
</script>

<template>
    <div class="wishlish flex">
        <div class="cart__left flex-1 pr-10">
            <div class="flex flex-col gap-4 mb-8">
                <div class="cart__left__title uppercase font-bold text-lg bg-[#F1F1F1] py-2 px-4">Sản phẩm yêu thích</div>
                <div class="cart__product-list flex flex-col">
                    <div v-if="lovedProducts.$state.lovedProducts.length === 0" class="flex flex-col items-center justify-center gap-3 p-8 mx-auto">
                        <Icon icon="ph:heart-straight-break" :width="72" :height="72" />
                        <h3 class="text-center text-xl font-bold w-36">Trong này chưa có gì cả bạn ơi!</h3>
                    </div>
                    <div v-for="item in lovedProducts.$state.lovedProducts" :key="item.id">
                        <WishListItem :product="item" />
                        <div class="divider--dashed my-8"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

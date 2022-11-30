<script setup lang="ts">
import { useCartStore } from "@/stores/cart"
import { ref } from "vue"
import { Icon } from "@iconify/vue"
const cart = useCartStore()
const isShow = ref(false)

const toggleSideCart = () => {
    isShow.value = !isShow.value
}
</script>

<template>
    <div class="side-cart fixed top-56 right-0 hidden lg:flex z-[555]" :class="isShow ? 'side-cart--show-menu' : 'side-cart--hide-menu'">
        <div class="side-cart__menu overflow-hidden">
            <div class="bg-[#C6E7D8] text-black flex flex-col px-[15px]">
                <div class="cart__title py-[10px] uppercase font-bold flex justify-between">
                    <span> Giỏ hàng ({{ cart.items.length }}) </span>
                    <span class="caret"></span>
                </div>
                <template v-if="cart.items.length">
                    <div class="divider--solid my-4"></div>
                    <ul class="cart__items py-[10px] flex flex-col max-h-[312px] overflow-y-scroll">
                        <li v-for="item in cart.items" :key="item.id" class="list-none">
                            <div class="flex">
                                <img :src="item.images.find((item) => item.is_thumbnail)?.url" alt="#" class="item-thumbnail w-20 h-20 object-cover mr-[10px]" />
                                <div class="item-info w-[180px] h-[80px] flex flex-col justify-between">
                                    <div class="name font-bold text-base leading-[1.1] text-2-line">{{ item.name }}</div>
                                    <div class="text-[12px] leading-[1.1]">
                                        <div class="price w-full flex justify-between">
                                            <span class="current-price font-bold">{{ Number(item.price).toLocaleString() }} VNĐ</span>
                                            <span class="price-before-sale line-through">{{ Number(1000000).toLocaleString() }}</span>
                                        </div>
                                        <div class="quantity flex w-full justify-between">
                                            <span>Số lượng</span>
                                            <span>{{ item.quantity }}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="divider--dashed my-4"></div>
                        </li>
                    </ul>
                    <div class="divider--solid mb-4"></div>
                    <div class="cart__total flex justify-between py-[5px] font-bold text-base">
                        <div>Total:</div>
                        <div class="text-love">{{ cart.total.toLocaleString() }} VNĐ</div>
                    </div>
                    <div class="cart__pay-btn-container py-[5px]"></div>
                    <div class="pt-[5px] pb-[10px]">
                        <AButton class="uppercase font-bold" type="primary" size="large" block>THANH TOÁN</AButton>
                    </div>
                </template>
                <template v-else>
                    <div class="flex flex-col items-center justify-center gap-3 p-8">
                        <Icon icon="ph:heart-straight-break" :width="48" :height="48" />
                        <h3 class="text-center font-bold w-36">Trong này chưa có gì cả bạn ơi!</h3>
                    </div>
                </template>
            </div>
        </div>
        <div class="side-cart__trigger-btn cursor-pointer w-10 h-[80px] bg-primary text-white flex flex-col items-center justify-center gap-2" @click="toggleSideCart">
            <div class="order-count text-center text-md font-bold">{{ cart.items.length }}</div>
            <Icon icon="ph:shopping-cart-simple-bold" />
        </div>
    </div>
</template>

<style lang="less" scoped>
.side-cart {
    &__menu,
    &__menu--empty {
        height: 472px;
        transition: height ease-in-out 0.5s;
    }
    &--show-menu > &__menu,
    &--show-menu > &__menu--empty {
    }
    &--hide-menu > &__menu,
    &--hide-menu > &__menu--empty {
        height: 0px !important;
        user-select: none;
        pointer-events: none;
    }
}

.text-2-line {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}
.caret {
    content: "";
    display: block;
    width: 0;
    height: 0;
    border-width: 6px 6px;
    border-style: solid;
    border-color: transparent;
    border-bottom-color: #44af7d;
    -webkit-transform: rotate(-90deg);
    -moz-transform: rotate(-90deg);
    -ms-transform: rotate(-90deg);
    -o-transform: rotate(-90deg);
    transform: rotate(-90deg) translateY(15px);
}
</style>

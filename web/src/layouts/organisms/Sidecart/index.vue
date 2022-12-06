<script setup lang="ts">
import { useCartStore } from "@/stores/cart"
import { ref } from "vue"
import { Icon } from "@iconify/vue"
import SideCartItem from "./SideCartItem.vue"
const cart = useCartStore()
const isShow = ref(false)

const toggleSideCart = () => {
    isShow.value = !isShow.value
}
</script>

<template>
    <div class="side-cart fixed top-56 right-0 hidden lg:flex z-[555]" :class="isShow ? 'side-cart--show-menu' : 'side-cart--hide-menu'">
        <div class="side-cart__menu overflow-hidden">
            <div class="bg-[#C6E7D8] text-black flex flex-col">
                <div class="cart__title py-[10px] uppercase font-bold flex justify-between px-[15px]">
                    <span> Giỏ hàng ({{ cart.items.length }}) </span>
                    <span class="caret"></span>
                </div>
                <template v-if="cart.items.length">
                    <div class="divider--solid my-4 mx-[15px]"></div>
                    <ul class="cart__items py-[10px] flex flex-col max-h-[312px] overflow-y-scroll px-[15px]">
                        <SideCartItem v-for="item in cart.items" :key="item.id" :item="item" />
                    </ul>
                    <div class="divider--solid my-4 mx-[15px]"></div>
                    <div class="cart__total flex justify-between py-[5px] px-[15px] font-bold text-base">
                        <div>Total:</div>
                        <div class="text-love">{{ cart.total.toLocaleString() }}₫</div>
                    </div>
                    <div class="cart__pay-btn-container py-[5px]"></div>
                    <div class="pt-[5px] pb-[10px] px-[15px]">
                        <RouterLink :to="{ name: 'Cart' }">
                            <AButton class="uppercase font-bold" type="primary" size="large" block>THANH TOÁN</AButton>
                        </RouterLink>
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
        height: 524px;
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

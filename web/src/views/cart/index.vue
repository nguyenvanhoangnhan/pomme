<script setup lang="ts">
import { useCartStore } from "@/stores/cart"
import { Icon } from "@iconify/vue"
import NavButton from "@/components/atoms/NavButton.vue"
defineProps<{}>()

const cart = useCartStore()

const handleOrder = () => {
    //
}

const handleDeleteAll = () => {
    //
}
</script>

<template>
    <div class="cart flex container mx-auto py-8">
        <div class="cart__left flex-1 pr-10">
            <SuggestBuyMore />
            <div class="flex flex-col gap-4 mb-8">
                <div class="cart__left__title uppercase font-bold text-lg bg-[#F1F1F1] py-2 px-4">Giỏ hàng</div>
                <div class="cart__product-list flex flex-col">
                    <div v-for="item in cart.items" :key="item.id">
                        <ProductItem :product="item" />
                        <div class="divider--dashed my-8"></div>
                    </div>
                </div>
            </div>

            <div class="flex justify-between gap-32">
                <AButton type="primary" size="large" block danger> <span class="uppercase font-semibold">Xóa hết</span> </AButton>
                <AButton type="primary" size="large" block @click="$router.push({ name: 'Home' })"><span class="uppercase font-semibold">Quay lại mua hàng</span></AButton>
            </div>
        </div>

        <div class="cart__right">
            <div class="cart__order-form p-5 w-[380px] bg-[#F1F1F1]">
                <div class="order-form__title font-bold text-2xl uppercase">Đơn hàng</div>
                <div class="divider--solid my-4"></div>
                <div class="order-form__coupon">
                    <div class="font-bold uppercase text-base mb-2">Nhập mã khuyến mãi</div>
                    <div class="flex">
                        <AInput class="flex-1" size="large" />
                        <AButton class="uppercase" style="font-weight: 600" type="primary" size="large">Áp dụng</AButton>
                    </div>
                </div>
                <div class="divider--dashed my-8"></div>
                <div class="order-form__calc font-bold text-base text-[#666]">
                    <div class="flex justify-between">
                        <span>Đơn hàng</span>
                        <span>{{ Number(cart.total).toLocaleString() }} VNĐ</span>
                    </div>
                    <div class="flex justify-between">
                        <span>Giảm</span>
                        <span>{{ Number(0).toLocaleString() }} VNĐ</span>
                    </div>
                </div>
                <div class="divider--dashed my-8"></div>
                <div class="order-form__total flex justify-between uppercase font-bold text-lg">
                    <span>Tạm tính</span>
                    <span>{{ Number(9999999).toLocaleString() }} VNĐ</span>
                </div>
                <div class="order-form__order-button mt-6">
                    <NavButton :onClick="handleOrder"> Tiếp tục thanh toán </NavButton>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

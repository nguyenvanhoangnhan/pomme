<script setup lang="ts">
import Order from "@/components/page/order/Order.vue"
import { ref } from "vue"

defineProps<{}>()
const orderStatus = ref("-1")
//  -1: all, 0: in progress, 1: shipping, 2: delivered

const orders = ref<Order[]>([
    {
        order_id: 1,
        user_id: 1,
        address: "123 Đường 3/2, Phường 12, Quận 10, Thành phố Hồ Chí Minh",
        province_id: 79,
        district_id: 703,
        commune_id: 53001,
        status: 0,
        total: 1000000,
        discount: 0,
        created_at: "2021-08-01T00:00:00.000Z",
        shipping_at: "2021-08-01T00:00:00.000Z",
        delivered_at: "2021-08-01T00:00:00.000Z",
        products: [
            {
                order_product_id: 1,
                product_id: 1,
                order_id: 1,
                quantity: 1,
                price_at_order: 1000000,
                size: 41,
                product: {
                    product_id: 1,
                    name: "Shoe #1",
                    price: 1000000,
                    sale_percent: 0,
                    in_stock: 0,
                    images: [
                        {
                            image_id: 1,
                            product_id: 1,
                            is_thumbnail: false,
                            url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
                        },
                    ],
                    type: 1,
                },
            },
            {
                order_product_id: 2,
                product_id: 2,
                order_id: 1,
                quantity: 2,
                price_at_order: 1000000,
                size: 41,
                product: {
                    product_id: 2,
                    name: "Shoe #2",
                    price: 1000000,
                    sale_percent: 0,
                    in_stock: 0,
                    images: [
                        {
                            image_id: 1,
                            product_id: 1,
                            is_thumbnail: false,
                            url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
                        },
                    ],
                    type: 1,
                },
            },
        ],
    },
    {
        order_id: 2,
        user_id: 1,
        address: "123 Đường 3/2, Phường 12, Quận 10, Thành phố Hồ Chí Minh",
        province_id: 79,
        district_id: 703,
        commune_id: 53001,
        status: 2,
        total: 1000000,
        discount: 0,
        created_at: "2021-08-01T00:00:00.000Z",
        shipping_at: "2021-08-01T00:00:00.000Z",
        delivered_at: "2021-08-01T00:00:00.000Z",
        products: [
            {
                order_product_id: 3,
                product_id: 2,
                order_id: 2,
                quantity: 2,
                price_at_order: 1000000,
                size: 40,
                product: {
                    product_id: 2,
                    name: "Shoe #2",
                    price: 1000000,
                    sale_percent: 0,
                    in_stock: 0,
                    images: [
                        {
                            image_id: 1,
                            product_id: 1,
                            is_thumbnail: false,
                            url: "https://ananas.vn/wp-content/uploads/Pro_AV00070_1-500x500.jpg",
                        },
                    ],
                    type: 1,
                },
            },
        ],
    },
])
</script>

<template>
    <div class="flex flex-col items-center">
        <div class="order-list w-full">
            <div class="order-list__title font-bold uppercase text-2xl text-center">Danh sách đơn hàng</div>
            <div class="divider--solid my-8"></div>
            <div class="bg-[#F2F2F2] p-4 flex flex-col gap-8">
                <ARadioGroup v-model:value="orderStatus" size="large" button-style="solid" class="w-full">
                    <ARadioButton value="-1" class="w-1/4 text-center font-bold text-lg">Tất cả</ARadioButton>
                    <ARadioButton value="0" class="w-1/4 text-center font-bold text-lg">Đang xử lí</ARadioButton>
                    <ARadioButton value="1" class="w-1/4 text-center font-bold text-lg">Đang giao</ARadioButton>
                    <ARadioButton value="2" class="w-1/4 text-center font-bold text-lg">Đã giao</ARadioButton>
                </ARadioGroup>
                <div class="flex flex-col gap-1">
                    <Order v-for="order in orders" :key="order.order_id" :order="order" />
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

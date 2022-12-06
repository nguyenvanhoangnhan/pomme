<script setup lang="ts">
import OrderProduct from "@/components/page/order/OrderProduct.vue"
import { useLoadingStore } from "@/stores/loading"
import { computed, onMounted, ref } from "vue"
import { useRoute } from "vue-router"
import router from "@/router"
import api from "@/api"
defineProps<{}>()

// get route param
const route = useRoute()
const { id } = route.params
const order = ref<OrderWithProducts>({})

onMounted(async () => {
    useLoadingStore().loadingOn()
    try {
        const { data } = await api.get(`/orders/${id}`)
        order.value = await data
    } catch (error) {
        router.push("/404")
    }
    useLoadingStore().loadingOff()
})
</script>

<template>
    <div v-if="order" class="order flex flex-col items-center">
        <div class="order__title font-bold uppercase text-2xl">Thông tin đơn hàng</div>
        <div class="divider--solid my-6"></div>
        <div class="font-bold text-lg uppercase">
            Trạng thái đơn hàng
            <span class="text-primary">#{{ id }}</span>
        </div>
        <div class="steps w-4/5 my-8">
            <ASteps :current="0">
                <AStep title="Đặt hàng thành công" description="6:12 - 13/03/2021" />
                <AStep title="Đang giao hàng" description="This is a description." />
                <AStep title="Giao hàng thành công" description="This is a description." />
            </ASteps>
            <div v-if="order.status === 'canceled'">Đã hủy</div>
        </div>
        <div class="divider--dashed my-4"></div>
        <div class="flex w-full gap-4">
            <div class="order__shipping-info flex-1 bg-[#F2F2F2] p-4">
                <div class="font-bold text-base uppercase">Thông tin giao nhận</div>
                <div class="divider--solid my-4"></div>
                <ul class="font-medium text-secondary">
                    <li>Họ tên: {{ "--họ tên--" }}</li>
                    <li>SĐT: {{ "--điện thoại--" }}</li>
                    <li>Email: {{ "--email--" }}</li>
                    <li>Địa chỉ: {{ "--địa chỉ--" }}</li>
                    <li>Phường/Xã: {{ "--phường/xã--" }}</li>
                    <li>Quận/Huyện: {{ "--quận/huyện--" }}</li>
                    <li>Thành phố/Tỉnh: {{ "--thành phố/tỉnh--" }}</li>
                </ul>
            </div>
            <div class="order__payment-info flex-1 bg-[#F2F2F2] p-4">
                <div class="font-bold text-base uppercase">Thanh toán</div>
                <div class="divider--solid my-4"></div>
                <ul class="font-medium text-secondary">
                    <li>
                        <span>Trị giá đơn hàng</span><span>{{ Number(order.total_price).toLocaleString() }}₫</span>
                    </li>
                    <li>
                        <span>Giảm giá</span><span>{{ Number(0).toLocaleString() }}₫</span>
                    </li>
                    <li>
                        <span>Phí giao hàng</span><span>{{ Number(order.delivery_fee).toLocaleString() }}₫</span>
                    </li>
                    <li>
                        <span>Phí thanh toán</span><span>{{ Number(0).toLocaleString() }}₫</span>
                    </li>
                    <div class="divider--dashed my-6"></div>
                    <li>
                        <span>Tổng thanh toán</span><span>{{ Number(order.delivery_fee + order.total_price).toLocaleString() }}₫</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="divider--dashed my-4"></div>
        <div class="order__product-list bg-[#F2F2F2] w-full flex flex-col items-center p-4">
            <div class="font-bold text-base uppercase">Danh sách sản phẩm</div>
            <div class="divider--solid my-4"></div>
            <OrderProduct v-for="(orderProduct, index) in order.products" :key="index" :order-product="orderProduct" />
        </div>
        <div class="mt-4 w-96 self-end">
            <NavButton :on-click="() => $router.push('/')">Quay lại trang chủ</NavButton>
        </div>
    </div>
</template>

<style lang="less" scoped>
.order {
    &__payment-info {
        ul li {
            @apply flex justify-between;

            span:nth-child(2) {
                @apply font-bold;
            }
        }
        ul li:last-child {
            @apply text-xl font-bold;
        }
    }
}
</style>

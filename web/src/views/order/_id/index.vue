<script setup lang="ts">
import OrderProduct from "@/components/page/order/OrderProduct.vue"
import { useLoadingStore } from "@/stores/loading"
import { computed, onMounted, ref } from "vue"
import { useRoute } from "vue-router"
import moment from "moment"
import router from "@/router"
import api from "@/api"
defineProps<{}>()

interface AreaCommuneResponse {
    code: string
    name: string
    district: string
    province: string
}

// get route param
const route = useRoute()
const { id } = route.params
const order = ref<OrderWithProducts | null>()
const deliveryLocation = ref<AreaCommuneResponse | null>()
const currentStep = computed(() => {
    switch (order.value?.status) {
        case "pending":
            return 0
        case "shipping":
            return 1
        case "delivered":
            return 2
        default:
            return 0
    }
})
const orderDates = computed(() => {
    let shippingAt = moment(order.value?.shipping_at).format("HH:mm - DD/MM/YYYY")
    shippingAt = shippingAt === "Invalid date" ? "" : shippingAt
    let deliveredAt = moment(order.value?.delivered_at).format("HH:mm - DD/MM/YYYY")
    deliveredAt = deliveredAt === "Invalid date" ? "" : deliveredAt
    return {
        orderAt: moment(order.value?.created_at).format("HH:mm - DD/MM/YYYY"),
        shippingAt,
        deliveredAt,
    }
})

onMounted(async () => {
    useLoadingStore().loadingOn()
    try {
        const { data } = await api.get(`/orders/${id}`)
        order.value = data
        const { data: districtCommunes } = await api.get(`https://api.mysupership.vn/v1/partner/areas/commune?district=${order.value?.district_code}`)
        deliveryLocation.value = districtCommunes.results.find((commune: AreaCommuneResponse) => commune.code === order.value?.commune_code)
    } catch (error: any) {
        router.push("/404")
        console.log(error)
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
            <ASteps :current="currentStep">
                <AStep title="Đặt hàng thành công" :description="orderDates.orderAt" />
                <AStep title="Đang giao hàng" :description="orderDates.shippingAt" />
                <AStep title="Giao hàng thành công" :description="orderDates.deliveredAt" />
            </ASteps>
            <div v-if="order.status === 'canceled'">Đã hủy</div>
        </div>
        <div class="divider--dashed my-4"></div>
        <div class="flex w-full gap-4">
            <div class="order__shipping-info flex-1 bg-[#F2F2F2] p-4">
                <div class="font-bold text-base uppercase">Thông tin giao nhận</div>
                <div class="divider--solid my-4"></div>
                <ul class="font-medium text-secondary">
                    <li>Họ tên: {{ order.receiver_name }}</li>
                    <li>SĐT: {{ order.phone }}</li>
                    <li>Địa chỉ: {{ order.address }}</li>
                    <li>Phường/Xã: {{ deliveryLocation?.name }}</li>
                    <li>Quận/Huyện: {{ deliveryLocation?.district }}</li>
                    <li>Thành phố/Tỉnh: {{ deliveryLocation?.province }}</li>
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

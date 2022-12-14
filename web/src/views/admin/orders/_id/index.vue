<script setup lang="ts">
import OrderProduct from "@/components/page/order/OrderProduct.vue"
import { useLoadingStore } from "@/stores/loading"
import { computed, onMounted, ref } from "vue"
import { useRoute } from "vue-router"
import moment from "moment"
import router from "@/router"
import api from "@/api"
import { notification } from "ant-design-vue"
defineProps<{}>()

// get route param
const route = useRoute()
const { id } = route.params
const initialLoading = ref(true)
const order = ref<OrderWithProducts | null>()
const deliveryLocation = ref<AreaCommune | null>()
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
    try {
        const { data } = await api.get(`/orders/${id}`)
        order.value = data
        const { data: districtCommunes } = await api.get(`https://api.mysupership.vn/v1/partner/areas/commune?district=${order.value?.district_code}`)
        deliveryLocation.value = districtCommunes.results.find((commune: AreaCommune) => commune.code === order.value?.commune_code)
        if (order.value?.status === "finished") order.value.status = "delivered"
    } catch (error: any) {
        router.push("/404")
        console.log(error)
    } finally {
        initialLoading.value = false
    }
})

const onOk = () => {
    router.push("/admin/orders")
}
const onCancel = () => {
    router.push("/admin/orders")
}
</script>

<template>
    <a-modal
        class="order-detail-modal"
        :visible="$route.name === 'Order Management - Detail'"
        style="top: 40px"
        title="Thông tin đơn hàng"
        cancel-text="Hủy"
        @ok="onOk"
        width="824px"
        @cancel="onCancel"
    >
        <div v-if="initialLoading">
            <a-skeleton active :paragraph="{ rows: 12 }"></a-skeleton>
        </div>
        <div v-else-if="order" class="order flex flex-col items-center max-h-[70vh] overflow-y-scroll px-4">
            <div class="font-bold text-lg uppercase">
                Trạng thái đơn hàng
                <span class="text-primary">#{{ id }}</span>
            </div>
            <div class="steps w-full my-8">
                <ASteps :current="currentStep">
                    <AStep title="Đặt hàng thành công" :description="orderDates.orderAt" />
                    <AStep title="Đang giao hàng" :description="order.status !== 'canceled' ? orderDates.shippingAt : ''" />
                    <AStep title="Giao hàng thành công" :description="order.status !== 'canceled' ? orderDates.deliveredAt : ''" />
                </ASteps>
                <div v-if="order.status === 'canceled'" class="text-center text-red-500 font-medium">Đã hủy</div>
            </div>
            <div class="divider--dashed my-4"></div>
            <div class="flex flex-col w-full gap-4">
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
        </div>
        <div v-else>
            <a-result status="404" title="404" :sub-title="`Không tìm thấy đơn hàng có mã ${id}`"></a-result>
        </div>
    </a-modal>
</template>

<style lang="less">
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
.order-detail-modal .ant-modal-footer .ant-btn:first-child {
    display: none !important;
}
</style>

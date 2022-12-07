<script setup lang="ts">
import Order from "@/components/page/order/Order.vue"
import { useOrderStore } from "@/stores/order"
import { computed } from "@vue/reactivity"
import { onMounted, ref } from "vue"

defineProps<{}>()
const orderStatus = ref("all")
const orders = computed(() => useOrderStore().orders)
onMounted(() => {
    useOrderStore().fetchOrders()
})
</script>

<template>
    <div class="flex flex-col items-center">
        <div class="order-list w-full">
            <div class="order-list__title font-bold uppercase text-2xl text-center">Danh sách đơn hàng</div>
            <div class="divider--solid my-8"></div>
            <div class="bg-[#F2F2F2] p-4 flex flex-col gap-8">
                <ARadioGroup v-model:value="orderStatus" size="large" button-style="solid" class="w-full">
                    <ARadioButton value="all" class="w-full text-center font-bold text-sm md:text-lg">Tất cả</ARadioButton>
                    <ARadioButton value="pending" class="w-1/4 text-center font-bold text-sm md:text-lg">Đang xử lí</ARadioButton>
                    <ARadioButton value="shipping" class="w-1/4 text-center font-bold text-sm md:text-lg">Đang giao</ARadioButton>
                    <ARadioButton value="delivered" class="w-1/4 text-center font-bold text-sm md:text-lg">Đã giao</ARadioButton>
                    <ARadioButton value="canceled" class="w-1/4 text-center font-bold text-sm md:text-lg">Đã hủy</ARadioButton>
                </ARadioGroup>
                <div class="flex flex-col gap-1">
                    <div v-for="order in orders" :key="order.id">
                        <Order :order="order" v-if="orderStatus === 'all' || orderStatus === order.status" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

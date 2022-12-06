<script setup lang="ts">
import Order from "@/components/page/order/Order.vue"
import { useOrderStore } from "@/stores/order"
import { computed } from "@vue/reactivity"
import { onMounted, ref } from "vue"

defineProps<{}>()
const orderStatus = ref("-1")
//  -1: all, 0: in progress, 1: shipping, 2: delivered
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
                    <ARadioButton value="-1" class="w-1/4 text-center font-bold text-lg">Tất cả</ARadioButton>
                    <ARadioButton value="0" class="w-1/4 text-center font-bold text-lg">Đang xử lí</ARadioButton>
                    <ARadioButton value="1" class="w-1/4 text-center font-bold text-lg">Đang giao</ARadioButton>
                    <ARadioButton value="2" class="w-1/4 text-center font-bold text-lg">Đã giao</ARadioButton>
                </ARadioGroup>
                <div class="flex flex-col gap-1">
                    <Order v-for="order in orders" :key="order.id" :order="order" />
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

<script setup lang="ts">
import { useCartStore } from "@/stores/cart"
import { useLoadingStore } from "@/stores/loading"
import { Icon } from "@iconify/vue"
import { computed } from "@vue/reactivity"

const props = defineProps<{
    product: UserCartProduct
}>()

const changeQuantity = (e: any) => {
    console.log("size: ", props.product.pivot.size)
    if (props.product.pivot.size) {
        useCartStore().updateItem(props.product.id, e, props.product.pivot.size)
        return
    }
    useCartStore().updateItem(props.product.id, e, 0)
}
const removeFromCart = async () => {
    await useCartStore().removeItem(props.product.pivot.id)
}

const TYPE = {
    shoe: "Giày",
    clothes: "Quần áo",
    accessory: "Phụ Kiện",
} as Record<string, string>

const priceAfterDiscount = computed(() => {
    return (props.product.price * (100 - props.product.discount_percent)) / 100
})
</script>

<template>
    <div class="flex gap-8">
        <RouterLink :to="{ name: product.type.charAt(0).toUpperCase() + product.type.slice(1) + ' Detail', params: { id: product.id } }">
            <div class="w-[180px]">
                <img class="w-[180px] h-[180px] object-cover" :src="product?.thumbnail.url" />
            </div>
        </RouterLink>
        <div class="flex-1 flex flex-col justify-between">
            <div class="flex justify-between text-lg font-bold">
                <RouterLink :to="{ name: product.type.charAt(0).toUpperCase() + product.type.slice(1) + ' Detail', params: { id: product.id } }">
                    <span class="">{{ product.name }}</span>
                </RouterLink>
                <span class="text-primary">{{ Number(priceAfterDiscount * product.pivot.quantity).toLocaleString() }}₫</span>
            </div>
            <span class="font-bold"> {{ TYPE[product.type] }} </span>
            <div class="flex justify-between">
                <div class="flex gap-3">
                    <span>Giá: {{ Number(priceAfterDiscount).toLocaleString() }}₫ </span>
                    <span class="line-through" v-if="product.discount_percent"> {{ Number(product.price).toLocaleString() }}₫</span>
                </div>
                <span class="text-primary" v-if="product.in_stock > 0">Còn hàng</span>
                <span class="text-red-600" v-else>Hết hàng</span>
            </div>
            <div class="flex justify-between">
                <div class="flex gap-8">
                    <div>
                        <div class="font-bold ml-[2px]">Số lượng</div>
                        <AInputNumber style="width: 96px" default-value="1" min="1" max="12" :value="product.pivot.quantity" @change="changeQuantity" :precision="0" />
                    </div>
                    <div v-if="product.pivot.size">
                        <div class="font-bold ml-[2px]">Size</div>
                        <div class="text-sm pt-[6px] text-center">{{ product.pivot.size }}</div>
                    </div>
                </div>
                <div class="flex flex-col items-end justify-end gap-4">
                    <div class="py-2 px-12 bg-[#303030] text-white cursor-pointer" @click="removeFromCart">
                        <Icon icon="ph:trash-bold" :width="20" :height="20" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

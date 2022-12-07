<script setup lang="ts">
import { useLovedProductsStore } from "@/stores/lovedProducts"
import { Icon } from "@iconify/vue"
import { computed } from "@vue/reactivity"

const props = defineProps<{
    product: ProductWithThumbnail
}>()

const lovedProducts = useLovedProductsStore()

const toggleLove = async () => {
    await lovedProducts.toggleLoveProduct(props.product.id)
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
                <span class="text-primary">{{ Number(priceAfterDiscount).toLocaleString() }}₫</span>
            </div>
            <span class="font-bold"> {{ TYPE[product.type] }} </span>
            <div class="flex justify-between">
                <div class="flex gap-3">
                    <span></span>
                    <span class="line-through" v-if="product.discount_percent"> {{ Number(product.price).toLocaleString() }}₫</span>
                </div>
                <span class="text-primary" v-if="product.in_stock > 0">Còn hàng</span>
                <span class="text-red-600" v-else>Hết hàng</span>
            </div>
            <div class="flex justify-between">
                <div></div>
                <div class="flex flex-col items-end justify-end gap-4">
                    <div class="py-2 px-12 bg-[#303030] text-white cursor-pointer" @click="toggleLove">
                        <Icon icon="ph:trash-fill" :width="20" :height="20" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

<script setup lang="ts">
import { Icon } from "@iconify/vue"

defineProps<{
    // eslint-disable-next-line no-undef
    product: CartItem
}>()
</script>

<template>
    <div class="flex gap-8">
        <div class="w-[180px]">
            <img class="w-[180px] h-[180px] object-cover" :src="product.images.find((item) => item.is_thumbnail)?.url" />
        </div>
        <div class="flex-1 flex flex-col justify-between">
            <div class="flex justify-between text-lg font-bold">
                <span class="">{{ product.name }}</span>
                <span class="text-primary">{{ Number(product.price * product.quantity).toLocaleString() }} VNĐ</span>
            </div>
            <div class="flex justify-between">
                <span>Giá: {{ Number(product.price).toLocaleString() }} </span>
                <span class="text-primary">Còn hàng</span>
            </div>
            <div class="flex justify-between">
                <div class="flex gap-8">
                    <div>
                        <div class="font-bold ml-[2px]">Size</div>
                        <ASelect placeholder="Size" class="w-24">
                            <ASelectOption :value="35" :key="35"> 35 </ASelectOption>
                            <ASelectOption :value="36" :key="36"> 36 </ASelectOption>
                            <ASelectOption :value="37" :key="37"> 38 </ASelectOption>
                            <ASelectOption :value="38" :key="38"> 38 </ASelectOption>
                            <ASelectOption :value="39" :key="39"> 39 </ASelectOption>
                            <ASelectOption :value="40" :key="40"> 40 </ASelectOption>
                            <ASelectOption :value="41" :key="41"> 41 </ASelectOption>
                            <ASelectOption :value="42" :key="42"> 42 </ASelectOption>
                            <ASelectOption :value="43" :key="43"> 43 </ASelectOption>
                            <ASelectOption :value="44" :key="44"> 44 </ASelectOption>
                            <ASelectOption :value="45" :key="45"> 45 </ASelectOption>
                            <ASelectOption :value="46" :key="46"> 46 </ASelectOption>
                        </ASelect>
                    </div>
                    <div>
                        <div class="font-bold ml-[2px]">Số lượng</div>
                        <AInputNumber style="width: 96px" defaultValue="1" min="1" max="12" />
                    </div>
                </div>
                <div class="flex flex-col gap-4">
                    <div class="py-2 px-12 color-primary border border-black">
                        <Icon icon="ph:heart-bold" :width="20" :height="20" />
                    </div>
                    <div class="py-2 px-12 bg-[#303030] text-white">
                        <Icon icon="ph:trash-bold" :width="20" :height="20" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

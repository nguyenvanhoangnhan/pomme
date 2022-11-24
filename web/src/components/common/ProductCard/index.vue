<script setup lang="ts">
import { Icon } from "@iconify/vue"
import { computed } from "@vue/reactivity"

const props = defineProps<{
    product: Product
}>()

const productType = computed(() => {
    switch (props.product.type) {
        case 1:
            return "Shoe"
        case 2:
            return "Accessory"
        case 3:
            return "Clothes"
    }
})

const addLove = () => {
    console.log("add love")
}
const removeLove = () => {
    console.log("remove love")
}

const productThumbnail = (product: Product) => {
    const img = product.images.find((image) => image.is_thumbnail)?.url;
    return img ? img : "https://via.placeholder.com/500?text=No+Image"
}
</script>

<template>
    <div class="w-1/3 px-2 mb-4">
        <div class="w-full group border-[3px] border-white hover:border-primary transition-all duration-250">
            <div @click="$router.push({ name: productType + ' Detail', params: { id: product.product_id } })">
                <div class="w-full aspect-square overflow-hidden relative cursor-pointer">
                    <img :src="productThumbnail(product)" :alt="product.name" class="w-full aspect-square cover group-hover:scale-110 transition-all duration-[0.4s]" />
                    <div v-if="true" @click.stop="addLove" class="love-icon hover:text-primary">
                        <Icon icon="ph:heart-bold" :width="32" :height="32" />
                    </div>
                    <div v-else @click.stop="removeLove" class="love-icon text-primary hover:text-secondary">
                        <Icon icon="ph:heart-duotone" :width="32" :height="32" />
                    </div>
                </div>
            </div>
            <div class="flex flex-col items-center my-2 gap-2">
                <RouterLink :to="{ name: productType + ' Detail', params: { id: product.product_id } }" class="font-bold text-lg text-center">
                    {{ product.name }}
                </RouterLink>
                <div class="font-bold text-base">{{ Number(product.price).toLocaleString() }} VNĐ</div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped>
.love-icon {
    @apply bottom-2 right-2 absolute isolate font-black transition-all;
}
</style>

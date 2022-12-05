<script setup lang="ts">
import { Icon } from "@iconify/vue"
import { computed } from "@vue/reactivity"
import { useProductsStore } from "@/stores/products"
import { useLoadingStore } from "@/stores/loading"
import { useAuthStore } from "@/stores/auth"
const props = defineProps<{
    product: ProductWithThumbnail
}>()
const products = useProductsStore()
const auth = useAuthStore()

const productType = computed(() => {
    return props.product.type.charAt(0).toUpperCase() + props.product.type.slice(1)
})

const toggleLove = async () => {
    useLoadingStore().loadingOn()
    await products.toggleLoveProduct(props.product.id)
    useLoadingStore().loadingOff()
}
const isLoved = computed(() => {
    return products.isLoved(props.product.id)
})
</script>

<template>
    <div class="w-1/3 px-2 mb-4">
        <div class="w-full group border-[3px] border-white hover:border-primary transition-all duration-250">
            <div @click="$router.push({ name: productType + ' Detail', params: { id: product.id } })">
                <div class="w-full aspect-square overflow-hidden relative cursor-pointer">
                    <img :src="product.thumbnail.url" :alt="product.name" class="w-full aspect-square cover group-hover:scale-110 transition-all duration-[0.4s]" />
                    <div v-if="!isLoved && auth.$state.data.user" @click.stop="toggleLove" class="love-icon hover:text-primary">
                        <Icon icon="ph:heart-bold" :width="32" :height="32" />
                    </div>
                    <div v-else-if="auth.$state.data.user" @click.stop="toggleLove" class="love-icon text-primary hover:text-secondary">
                        <Icon icon="ph:heart-duotone" :width="32" :height="32" />
                    </div>
                </div>
            </div>
            <div class="flex flex-col items-center my-2 gap-2">
                <RouterLink :to="{ name: productType + ' Detail', params: { id: product.id } }" class="font-bold text-lg text-center">
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

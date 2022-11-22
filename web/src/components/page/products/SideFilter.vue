<script setup lang="ts">
import { ref } from "vue"
import { useRoute } from "vue-router"
import { Icon } from "@iconify/vue"
const { query } = useRoute()
console.log(query)
const TYPES = {
    all: "0",
    shoe: "1",
    accessory: "2",
    clothes: "3",
}

const isShowMenus = ref({
    series: false,
    gender: false,
    shape: false,
})
</script>

<template>
    <div id="side-filter" class="w-[270px]">
        <div class="type font-extrabold uppercase text-2xl flex flex-col gap-4 text-secondary">
            <div class="cursor-pointer" :class="{ 'text-black': !query?.type || query?.type === TYPES.all }">Tất cả</div>
            <div class="side-filter__shoe">
                <div class="cursor-pointer" :class="{ 'text-black': query?.type === TYPES.shoe }">Giày</div>
                <div v-show="query?.type === TYPES.shoe">
                    <div class="filter" :class="{ 'filter--minimize': !isShowMenus.series }">
                        <div class="filter__title" @click="() => (isShowMenus.series = !isShowMenus.series)">
                            Dòng sản phẩm
                            <Icon icon="ph:caret-right-fill" :width="16" :height="16" />
                        </div>
                        <div class="filter__menu" style="height: calc(5 * 32px + 4 * 4px)">
                            <div class="filter__option filter__option--active">Tất cả</div>
                            <div class="filter__option">GSmith</div>
                            <div class="filter__option">Crispin</div>
                            <div class="filter__option">Shizuka</div>
                            <div class="filter__option">Rhode</div>
                        </div>
                    </div>
                    <div class="filter" :class="{ 'filter--minimize': !isShowMenus.gender }">
                        <div class="filter__title" @click="() => (isShowMenus.gender = !isShowMenus.gender)">
                            Giới tính
                            <Icon icon="ph:caret-right-fill" :width="16" :height="16" />
                        </div>
                        <div class="filter__menu" style="height: calc(3 * 32px + 2 * 4px)">
                            <div class="filter__option filter__option--active">Tất cả</div>
                            <div class="filter__option">Giày nam</div>
                            <div class="filter__option">Giày nữ</div>
                        </div>
                    </div>
                    <div class="filter" :class="{ 'filter--minimize': !isShowMenus.shape }">
                        <div class="filter__title" @click="() => (isShowMenus.shape = !isShowMenus.shape)">
                            Kiểu dáng
                            <Icon icon="ph:caret-right-fill" :width="16" :height="16" />
                        </div>
                        <div class="filter__menu" style="height: calc(3 * 32px + 2 * 4px)">
                            <div class="filter__option filter__option--active">Tất cả</div>
                            <div class="filter__option">High Top</div>
                            <div class="filter__option">Low top</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="divider--dashed"></div>
            <div class="cursor-pointer" :class="{ 'text-black': query?.type === TYPES.accessory }">Phụ kiện</div>
            <div class="divider--dashed"></div>
            <div class="cursor-pointer" :class="{ 'text-black': query?.type === TYPES.clothes }">Áo quần</div>
        </div>
    </div>
</template>

<style lang="less" scoped>
.separate-line {
    @apply bg-slate-400 whitespace-nowrap;
    width: 2px;
    height: 20px;
}
.filter {
    &__title {
        @apply text-primary text-lg flex items-center gap-2 cursor-pointer transition-all;
    }
    &__option {
        @apply px-2 py-1 flex justify-between cursor-pointer;
        &--active {
            @apply bg-secondary bg-opacity-20;
        }
    }
    &__menu {
        @apply flex flex-col gap-1 font-normal text-base normal-case text-black overflow-hidden transition-all;
    }
    .iconify {
        @apply rotate-90 transition-all;
    }
}

.filter.filter--minimize {
    .filter__title {
        @apply text-black;
    }
    .filter__menu {
        height: 0 !important;
    }
    .iconify {
        @apply rotate-0;
    }
}
</style>

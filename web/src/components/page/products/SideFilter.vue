<script setup lang="ts">
import { reactive, ref, watch } from "vue"
import { useRoute, useRouter } from "vue-router"
import { Icon } from "@iconify/vue"
import { useProductsStore } from "@/stores/products"

const productsStore = useProductsStore()
const router = useRouter()
const route = useRoute()
const queryRef = ref(route.query)
const TYPES = {
    all: "",
    shoe: "shoe",
    accessory: "accessory",
    clothes: "clothes",
}
const ACCESSORY_CATEGORIES = {
    Tất: "shock",
    "Túi tote": "tote",
    Balo: "backpack",
    "Dây giày": "shoelace",
}
const CLOTHES_CATEGORIES = {
    "Áo phông": "tee",
    Hoodie: "hoodie",
    Sweatshirt: "sweatshirt",
}
const SHOE_SERIES = { GSmith: "GSmith", Crispin: "Crispin", Shizuka: "Shizuka", Rhode: "Rhode" }
const SHOE_GENDERS = {
    Nam: "1",
    Nữ: "2",
    Unisex: "3",
}
const SHOE_SHAPES = {
    "Low Top": "0",
    "High Top": "1",
}

const isShowMenus = reactive({
    series: false,
    gender: false,
    shape: false,
    accessoryCategory: false,
    clothesCategory: false,
})

if ("series" in queryRef.value) {
    isShowMenus.series = true
}
if ("gender" in queryRef.value) {
    isShowMenus.gender = true
}
if ("shape" in queryRef.value) {
    isShowMenus.shape = true
}
if (queryRef.value?.type == TYPES.accessory && "category" in queryRef.value) {
    isShowMenus.accessoryCategory = true
}
if (queryRef.value?.type == TYPES.clothes && "category" in queryRef.value) {
    isShowMenus.clothesCategory = true
}
const handleQueries = (attr: string, val: string | null) => {
    alert("Filter is not implemented yet")
    return

    if (val == "Tất cả") {
        val = null
    }
    router.replace({
        query: {
            ...queryRef.value,
            [attr]: val,
        },
    })
    queryRef.value = {
        ...queryRef.value,
        [attr]: val,
    }
}
const handleQueryType = (type: string) => {
    alert("Filter is not implemented yet")
    return

    if (type.length === 0) {
        router.replace({ query: {} })
        queryRef.value = {}
    }
    router.replace({
        query: { type: type },
    })
    queryRef.value = { type: type }
}
watch(queryRef, (newVal) => {
    productsStore.updateQueries(queryRef.value)
    if ("series" in newVal) {
        isShowMenus.series = true
    }
    if ("gender" in newVal) {
        isShowMenus.gender = true
    }
    if ("shape" in newVal) {
        isShowMenus.shape = true
    }
    if (newVal.type == TYPES.accessory && "category" in newVal) {
        isShowMenus.accessoryCategory = true
    }
    if (newVal.type == TYPES.clothes && "category" in newVal) {
        isShowMenus.clothesCategory = true
    }
})
</script>

<template>
    <div id="side-filter" class="w-[270px]">
        <div class="side-filter__types font-extrabold uppercase text-2xl flex flex-col gap-4 text-secondary">
            <div class="cursor-pointer transition-all" :class="{ 'text-black': !$route.query?.type || $route.query?.type === TYPES.all }" @click="handleQueryType('')">Tất cả</div>
            <div class="divider--dashed"></div>
            <div class="side-filter__shoe">
                <div class="cursor-pointer transition-all" :class="{ 'text-black': $route.query?.type === TYPES.shoe }" @click="handleQueryType(TYPES.shoe)">Giày</div>
                <div v-show="$route.query?.type === TYPES.shoe" class="transition-all">
                    <div class="filter" :class="{ 'filter--minimize': !isShowMenus.series }">
                        <div class="filter__title" @click="() => (isShowMenus.series = !isShowMenus.series)">
                            Dòng sản phẩm
                            <Icon icon="ph:caret-right-fill" :width="16" :height="16" />
                        </div>
                        <div class="filter__menu" style="height: calc(5 * 32px + 4 * 4px)">
                            <div
                                class="filter__option"
                                :class="{
                                    'filter__option--active': !$route.query.series,
                                }"
                                @click="handleQueries('series', 'Tất cả')"
                            >
                                Tất cả
                            </div>
                            <div
                                v-for="series in Object.keys(SHOE_SERIES)"
                                :key="series"
                                class="filter__option"
                                :class="{ 'filter__option--active': $route.query?.series == SHOE_SERIES[series] }"
                                @click="handleQueries('series', SHOE_SERIES[series])"
                            >
                                {{ series }}
                            </div>
                        </div>
                    </div>
                    <div class="filter" :class="{ 'filter--minimize': !isShowMenus.gender }">
                        <div class="filter__title" @click="() => (isShowMenus.gender = !isShowMenus.gender)">
                            Giới tính
                            <Icon icon="ph:caret-right-fill" :width="16" :height="16" />
                        </div>
                        <div class="filter__menu" style="height: calc(3 * 32px + 2 * 4px)">
                            <div
                                class="filter__option"
                                :class="{
                                    'filter__option--active': !$route.query.gender,
                                }"
                                @click="handleQueries('gender', 'Tất cả')"
                            >
                                Tất cả
                            </div>
                            <div
                                v-for="gender in Object.keys(SHOE_GENDERS)"
                                :key="gender"
                                class="filter__option"
                                :class="{ 'filter__option--active': $route.query?.gender == SHOE_GENDERS[gender] }"
                                @click="handleQueries('gender', SHOE_GENDERS[gender])"
                            >
                                {{ gender }}
                            </div>
                        </div>
                    </div>
                    <div class="filter" :class="{ 'filter--minimize': !isShowMenus.shape }">
                        <div class="filter__title" @click="() => (isShowMenus.shape = !isShowMenus.shape)">
                            Kiểu dáng
                            <Icon icon="ph:caret-right-fill" :width="16" :height="16" />
                        </div>
                        <div class="filter__menu" style="height: calc(3 * 32px + 2 * 4px)">
                            <div
                                class="filter__option"
                                :class="{
                                    'filter__option--active': !$route.query.shape,
                                }"
                                @click="handleQueries('shape', 'Tất cả')"
                            >
                                Tất cả
                            </div>
                            <div
                                v-for="shape in Object.keys(SHOE_SHAPES)"
                                :key="shape"
                                class="filter__option"
                                :class="{ 'filter__option--active': $route.query?.shape == SHOE_SHAPES[shape] }"
                                @click="handleQueries('shape', SHOE_SHAPES[shape])"
                            >
                                {{ shape }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="divider--dashed"></div>
            <div class="side-filter__accessory">
                <div class="cursor-pointer transition-all" :class="{ 'text-black': $route.query?.type === TYPES.accessory }" @click="handleQueryType(TYPES.accessory)">Phụ kiện</div>
                <div v-show="$route.query?.type === TYPES.accessory" class="transition-all">
                    <div class="filter" :class="{ 'filter--minimize': !isShowMenus.accessoryCategory }">
                        <div class="filter__title" @click="() => (isShowMenus.accessoryCategory = !isShowMenus.accessoryCategory)">
                            Loại phụ kiện
                            <Icon icon="ph:caret-right-fill" :width="16" :height="16" />
                        </div>
                        <div class="filter__menu" style="height: calc(5 * 32px + 4 * 4px)">
                            <div
                                class="filter__option"
                                :class="{
                                    'filter__option--active': !$route.query.category,
                                }"
                                @click="handleQueries('category', 'Tất cả')"
                            >
                                Tất cả
                            </div>
                            <div
                                v-for="category in Object.keys(ACCESSORY_CATEGORIES)"
                                :key="category"
                                class="filter__option"
                                :class="{ 'filter__option--active': $route.query?.category == ACCESSORY_CATEGORIES[category] }"
                                @click="handleQueries('category', ACCESSORY_CATEGORIES[category])"
                            >
                                {{ category }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="divider--dashed"></div>
            <div class="side-filter__clothes">
                <div class="cursor-pointer transition-all" :class="{ 'text-black': $route.query?.type === TYPES.clothes }" @click="handleQueryType(TYPES.clothes)">Áo quần</div>
                <div v-show="$route.query?.type === TYPES.clothes" class="transition-all">
                    <div class="filter" :class="{ 'filter--minimize': !isShowMenus.clothesCategory }">
                        <div class="filter__title" @click="() => (isShowMenus.clothesCategory = !isShowMenus.clothesCategory)">
                            Loại áo quần
                            <Icon icon="ph:caret-right-fill" :width="16" :height="16" />
                        </div>
                        <div class="filter__menu" style="height: calc(5 * 32px + 4 * 4px)">
                            <div
                                class="filter__option"
                                :class="{
                                    'filter__option--active': !$route.query.category,
                                }"
                                @click="handleQueries('category', 'Tất cả')"
                            >
                                Tất cả
                            </div>
                            <div
                                v-for="category in Object.keys(CLOTHES_CATEGORIES)"
                                :key="category"
                                class="filter__option"
                                :class="{ 'filter__option--active': $route.query?.category == CLOTHES_CATEGORIES[category] }"
                                @click="handleQueries('category', CLOTHES_CATEGORIES[category])"
                            >
                                {{ category }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
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

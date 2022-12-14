<script setup lang="ts">
import router from "@/router"
import { ref } from "vue"
import { useRoute } from "vue-router"

// defineProps<{}>()
const route = useRoute()
interface Selection {
    label: string
    value: string
    options?: Selection[]
    children?: Selection[]
}

const typeSelection = {
    label: "Loại sản phẩm",
    value: "type",
    options: [
        {
            label: "Tất cả",
            value: "",
        },
        {
            label: "Giày",
            value: "shoe",
        },
        {
            label: "Áo quần",
            value: "clothes",
        },
        {
            label: "Phụ kiện",
            value: "accessory",
        },
    ],
    children: [
        {
            label: "Giày",
            value: "shoe",
            children: [
                {
                    label: "Giới tính",
                    value: "gender",
                    options: [
                        {
                            label: "Tất cả",
                            value: "",
                        },
                        {
                            label: "Nam",
                            value: "0",
                        },
                        {
                            label: "Nữ",
                            value: "1",
                        },
                    ],
                },
                {
                    label: "Dòng sản phẩm",
                    value: "series",
                    options: [
                        {
                            label: "Tất cả",
                            value: "",
                        },

                        {
                            label: "GSmith",
                            value: "GSmith",
                        },
                        {
                            label: "Crispin",
                            value: "Crispin",
                        },
                        {
                            label: "Shizuka",
                            value: "Shizuka",
                        },
                        {
                            label: "Rhode",
                            value: "Rhode",
                        },
                    ],
                },
                {
                    label: "Kiểu dáng",
                    value: "shape",
                    options: [
                        {
                            label: "Tất cả",
                            value: "",
                        },
                        {
                            label: "Low Top",
                            value: "0",
                        },
                        {
                            label: "High Top",
                            value: "1",
                        },
                    ],
                },
            ],
        },
        {
            label: "Áo quần",
            value: "clothes",
            children: [
                {
                    label: "Loại áo quần",
                    value: "category",
                    options: [
                        {
                            label: "Tất cả",
                            value: "",
                        },
                        {
                            label: "Áo phông",
                            value: "tee",
                        },
                        {
                            label: "Sweatshirt",
                            value: "sweatshirt",
                        },
                        {
                            label: "Hoodie",
                            value: "hoodie",
                        },
                    ],
                },
            ],
        },
        {
            label: "Phụ kiện",
            value: "accessory",
            children: [
                {
                    label: "Loại phụ kiện",
                    value: "category",
                    options: [
                        {
                            label: "Tất cả",
                            value: "",
                        },
                        {
                            label: "Tất",
                            value: "shock",
                        },
                        {
                            label: "Túi tote",
                            value: "tote",
                        },
                        {
                            label: "Balo",
                            value: "backpack",
                        },
                        {
                            label: "Dây giày",
                            value: "shoelace",
                        },
                    ],
                },
            ],
        },
    ],
} as Selection

const selectedType = ref(route.query.type ?? "")
router.afterEach(() => {
    selectedType.value = route.query.type ?? ""
})
</script>

<template>
    <div class="flex gap-8">
        <div class="flex flex-col mt-2">
            <span class="font-bold">Loại sản phẩm</span>
            <a-select
                :options="typeSelection.options"
                placeholder="Loại sản phẩm"
                :style="{ width: '160px' }"
                v-model:value="selectedType"
                @select="$router.push({ query: { type: selectedType } })"
            ></a-select>
        </div>
        <template v-if="selectedType !== '' && typeSelection.children?.find((item) => item.value === selectedType)">
            <div class="flex flex-col mt-2" v-for="selection in typeSelection.children?.find((item) => item.value === selectedType)?.children" :key="selection.value">
                <span class="font-bold">{{ selection.label }}</span>
                <a-select
                    :default-value="''"
                    :options="selection.options"
                    style="width: 160px"
                    :placeholder="selection.label"
                    @select="$router.push({ query: { ...$route.query, [selection.value]: $event } })"
                >
                </a-select>
            </div>
        </template>
    </div>
</template>

<style lang="less" scoped></style>

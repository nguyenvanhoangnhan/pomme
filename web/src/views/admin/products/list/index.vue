<script setup lang="ts">
import Selections from "@/components/page/admin/products/Selections.vue"
import router from "@/router"
import { useRoute } from "vue-router"
import type { ColumnsType } from "ant-design-vue/es/table/interface"
import { onMounted, reactive, ref } from "vue"
import api from "@/api"
import { notification, TableProps } from "ant-design-vue"
import { useLoadingStore } from "@/stores/loading"
import { Icon } from "@iconify/vue"
import { useProductsStore } from "@/stores/products"

const route = useRoute()
const products = ref<ProductWithThumbnail[] | null>(null)
const pagination = reactive<PaginationInfo>({
    current_page: Number(route.query.page) || 1,
    last_page: 1,
    next_page_url: null,
    prev_page_url: null,
    per_page: 12,
    total: 0,
})

const fetchProducts = async () => {
    const queryParams = route.query
    try {
        useLoadingStore().loadingOn()
        const { data: dataWithPagination } = await api.get("/products", { params: queryParams })
        products.value = dataWithPagination.data
        pagination.current_page = dataWithPagination.current_page
        pagination.last_page = dataWithPagination.last_page
        pagination.next_page_url = dataWithPagination.next_page_url
        pagination.prev_page_url = dataWithPagination.prev_page_url
        pagination.per_page = dataWithPagination.per_page
        pagination.total = dataWithPagination.total
    } catch (err: any) {
        notification.error({
            message: "Error",
            description: err?.message || "Something went wrong",
        })
    }
    useLoadingStore().loadingOff()
}

onMounted(async () => {
    await fetchProducts()
})

const handleChangePage = (page: number) => {
    router.push({ query: { ...route.query, page } })
}

router.afterEach(async (to, from) => {
    if (to.path !== "/admin/products" || to.fullPath === from.fullPath) {
        return
    }
    await fetchProducts()
})

const columns = [
    {
        title: "Mã",
        dataIndex: "id",
        key: "id",
        align: "center",
        width: 60,
    },
    {
        title: "Thumbnail",
        dataIndex: "thumbnail",
        key: "thumbnail",
        align: "center",
        slots: { customRender: "thumbnail" },
        width: 120,
    },
    {
        title: "Tên sản phẩm",
        dataIndex: "name",
        key: "name",
        align: "center",
    },
    {
        title: "Giá",
        dataIndex: "price",
        sorter: true,
        key: "price",
        width: 140,
        align: "center",
        slots: { customRender: "price" },
    },
    {
        title: "Giảm giá (%)",
        dataIndex: "discount_percent",
        width: 120,
        key: "discount_percent",
        align: "center",
    },
    {
        title: "Trong kho",
        dataIndex: "in_stock",
        width: 120,
        key: "in_stock",
        align: "center",
    },
    {
        title: "Đã bán",
        dataIndex: "sold",
        width: 120,
        key: "sold",
        align: "center",
    },
    {
        title: "Loại",
        dataIndex: "type",
        slots: { customRender: "type" },
        width: 120,
        key: "type",
        align: "center",
    },
    {
        title: "Thao tác",
        key: "action",
        align: "center",
        slots: { customRender: "action" },
        width: 220,
    },
] as ColumnsType<ProductWithThumbnail>

const handleChange: TableProps["onChange"] = (pagination, filters, sorter) => {
    console.log("Sorter", sorter)
    // check if sorter is not empty or not an array
    if (sorter && !Array.isArray(sorter) && sorter.field === "price") {
        if (sorter.order !== "ascend" && sorter.order !== "descend") {
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            const { price_sort, ...rest } = route.query
            router.push({ query: rest })
            return
        }
        const order = sorter.order === "ascend" ? "asc" : "desc"
        router.push({ query: { ...route.query, price_sort: order } })
    }
}

const handleDelete = async (record: ProductWithThumbnail) => {
    const deleteSuccess = await useProductsStore().removeProduct(record.id)
    if (deleteSuccess) {
        // delete on products ref
        products.value = products.value?.filter((product) => product.id !== record.id) || []
        if (products.value.length === 0) {
            fetchProducts()
        }
    }
}

const handleEdit = (id: number, type: string) => {
    router.push(`/admin/products/edit/${type}/${id}`)
}
</script>

<template>
    <Selections />
    <RouterView />
    <div class="flex flex-col gap-8 w-full mt-4">
        <a-pagination
            show-quick-jumper
            :current="pagination.current_page"
            :total="pagination.total"
            :page-size="pagination.per_page"
            :show-size-changer="false"
            @change="handleChangePage"
        ></a-pagination>
        <a-table class="self-stretch" :columns="columns" :data-source="products" :pagination="false" :row-key="(record: ProductWithThumbnail) => record.id" @change="handleChange">
            <template #thumbnail="{ text }">
                <a-image :src="text.url" width="80px" height="80px" style="object-fit: cover" />
            </template>
            <template #type="{ text }">
                <span v-if="text === 'shoe'">Giày</span>
                <span v-if="text === 'accessory'">Phụ kiện</span>
                <span v-if="text === 'clothes'">Áo quần</span>
            </template>
            <template #price="{ text }">
                <span>{{ text.toLocaleString() }}đ</span>
            </template>
            <template #action="{ record }">
                <div class="flex flex-col gap-1">
                    <a :href="`/product/${record.type}/${record.id}`" target="_blank">
                        <a-button type="primary" block>
                            <template #icon><Icon icon="ph:magnifying-glass-bold" class="mr-2" /></template>Trang chi tiết
                        </a-button>
                    </a>
                    <div class="flex justify-center gap-1">
                        <a-button type="primary" @click="handleEdit(record.id, record.type)" block>
                            <template #icon><Icon icon="ph:note-pencil-bold" class="mr-2" /></template>Sửa
                        </a-button>
                        <a-button type="primary" danger @click="handleDelete(record)" block>
                            <template #icon><Icon icon="ph:trash-simple-bold" class="mr-2" /> </template>Xóa
                        </a-button>
                    </div>
                </div>
            </template>
        </a-table>
        <a-pagination
            show-quick-jumper
            :current="pagination.current_page"
            :total="pagination.total"
            :page-size="pagination.per_page"
            :show-size-changer="false"
            @change="handleChangePage"
        ></a-pagination>
    </div>
</template>

<style lang="less">
.ant-image-preview-img {
    max-height: 50vh;
    @apply shadow-lg;
}
.ant-image-preview-img-wrapper {
    @apply flex justify-center items-center;
}
</style>

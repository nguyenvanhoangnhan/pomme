<script setup lang="ts">
import api from "@/api"
import { ColumnsType } from "ant-design-vue/lib/table"
import { onMounted, ref } from "vue"
import moment from "moment"
import { notification } from "ant-design-vue"
import { Icon } from "@iconify/vue"
defineProps<{}>()

const orders = ref<Order[]>([])
const initialLoading = ref(true)
onMounted(async () => {
    try {
        const { data } = await api.get("/orders")
        orders.value = data
    } catch (err: any) {
        notification.error({
            message: "Lỗi khi tải dữ liệu",
            description: err.message || "Thông tin lỗi không xác định",
        })
    }
    initialLoading.value = false
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
        dataIndex: "image_url",
        key: "image_url",
        align: "center",
        slots: { customRender: "thumbnail" },
        width: 120,
    },
    {
        title: "Tên đơn hàng",
        dataIndex: "name",
        key: "name",
        align: "center",
    },
    {
        title: "Giá trị",
        sorter: {
            compare: (a: Order, b: Order) => a.total_price + a.delivery_fee - (b.total_price + b.delivery_fee),
            multiple: 1,
        },
        key: "total",
        width: 200,
        align: "center",
        slots: { customRender: "total" },
    },
    {
        title: "Trạng thái",
        dataIndex: "status",
        width: 160,
        key: "status",
        align: "center",
        filters: [
            { text: "Chờ xử lý", value: "pending" },
            { text: "Đang giao hàng", value: "shipping" },
            { text: "Đã giao hàng", value: "delivered" },
            { text: "Đã hoàn thành", value: "finished" },
            { text: "Đã hủy", value: "canceled" },
        ],
        slots: { customRender: "status" },
    },
    {
        title: "Đặt lúc",
        dataIndex: "created_at",
        width: 160,
        key: "created_at",
        align: "center",
        slots: { customRender: "created_at" },
    },
    {
        title: " ",
        key: "action",
        align: "center",
        slots: { customRender: "action" },
        width: 140,
    },
] as ColumnsType<ProductWithThumbnail>

const handleChangeStatus = async (record: Order, status: string) => {
    try {
        await api.put(`/orders/${record.id}/status?status=${status}`)
        const index = orders.value.findIndex((order) => order.id === record.id)
        orders.value[index].status = status
        notification.success({
            message: "Cập nhật trạng thái đơn hàng thành công",
        })
    } catch (err: any) {
        notification.error({
            message: "Cập nhật trạng thái đơn hàng thất bại",
            description: err.response.data.message,
        })
    }
}
const STATUSES = {
    pending: "Chờ xử lý",
    shipping: "Đang giao hàng",
    delivered: "Đã giao hàng",
    finished: "Đã hoàn thành",
    canceled: "Đã hủy",
}

const pagination = {
    showSizeChanger: true,
    position: ["topLeft", "bottomLeft"],
}
</script>
<template>
    <router-view></router-view>
    <div class="skeleton" v-show="initialLoading"><a-skeleton active :paragraph="{ rows: 8 }" /></div>
    <a-table v-show="!initialLoading" class="self-stretch mt-4" :columns="columns" :data-source="orders" :pagination="pagination" :row-key="(record: ProductWithThumbnail) => record.id">
        <template #thumbnail="{ text }">
            <a-image :src="text" width="80px" height="80px" style="object-fit: cover" />
        </template>
        <template #total="{ record }">
            <span>{{ Number(record.total_price + record.delivery_fee).toLocaleString() }}đ</span>
        </template>
        <template #status="{ record }">
            <div v-if="record.status === 'canceled'" class="text-red-500">Đã hủy</div>
            <a-select v-else class="w-36" :value="record.status" @change="(e: string) => handleChangeStatus(record, e)">
                <a-select-option v-for="(value, key) in STATUSES" :key="key" :value="key">{{ value }}</a-select-option>
            </a-select>
        </template>
        <template #created_at="{ record }"> {{ moment.utc(record.created_at).local().format("HH:mm DD/MM/YYYY") }}</template>
        <template #action="{ record }">
            <a-button type="primary" @click="() => $router.push(`/admin/orders/${record.id}`)">
                <template #icon><Icon icon="ph:magnifying-glass-bold" class="mr-2" /></template>Chi tiết
            </a-button>
        </template>
    </a-table>
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

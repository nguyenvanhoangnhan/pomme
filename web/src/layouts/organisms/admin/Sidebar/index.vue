<script lang="ts" setup>
import { ref } from "vue"
import { MenuUnfoldOutlined, MenuFoldOutlined } from "@ant-design/icons-vue"
import { Modal } from "ant-design-vue"
import { useAuthStore } from "@/stores/auth"
import { Icon } from "@iconify/vue"
import router from "@/router"
const auth = useAuthStore()
// selected if current route name is equal to key or parent route name is equal to key
const selectedKeys = ref<string[]>([router.currentRoute.value.name as string, ...router.currentRoute.value.matched.map((route) => route.name as string)])
const collapsed = ref<boolean>(false)
const handleCollapse = () => {
    collapsed.value = !collapsed.value
}
// eslint-disable-next-line @typescript-eslint/no-explicit-any
const handleSelect = (event: any) => {
    router.push({ name: event?.key })
}

const handleLogout = () => {
    Modal.confirm({
        title: "Bạn có chắc muốn đăng xuất?",
        centered: true,
        okText: "Có",
        cancelText: "Không",
        onOk: async () => {
            await auth.logout()
            window.location.replace("/")
        },
    })
}
</script>
<template>
    <div class="gap-4 bg-[#001529] flex flex-col text-white z-[666]">
        <a-button type="primary" block class="mb-8" @click="handleCollapse">
            <template #icon>
                <MenuUnfoldOutlined v-if="collapsed" />
                <MenuFoldOutlined v-else />
            </template>
        </a-button>
        <div class="flex flex-col gap-3 mb-12" :class="{ 'pl-6': !collapsed, 'items-center': collapsed }">
            <div class="avatar aspect-square overflow-hidden rounded-lg" :class="{ 'w-24': !collapsed, 'w-12': collapsed }">
                <img src="https://res.cloudinary.com/cyantiz/image/upload/v1670993022/YagamiLightRingo_moramg.png" class="w-full h-full object-cover" alt="#" />
            </div>
            <div v-if="!collapsed">
                <div class="font-bold text-lg">{{ auth?.data?.user?.name }} (Admin)</div>
                <div class="text-gray-300">admin@pomme.tech</div>
            </div>
        </div>
        <a-menu
            :style="{ width: collapsed ? '64px' : '256px' }"
            id="admin-side-menu"
            @select="handleSelect"
            v-model:selectedKeys="selectedKeys"
            mode="inline"
            theme="dark"
            :inline-collapsed="collapsed"
            :open-keys="!collapsed ? ['Product Management'] : []"
        >
            <a-sub-menu key="Product Management">
                <template #icon><Icon icon="ph:tag-duotone" /></template>
                <template #title>Quản lý sản phẩm</template>
                <a-menu-item key="Product Management - List"> Danh sách sản phẩm </a-menu-item>
                <a-menu-item key="Product Management - Create"> Thêm sản phẩm </a-menu-item>
            </a-sub-menu>
            <a-menu-item key="Order Management">
                <template #icon>
                    <Icon icon="ph:package-bold" />
                </template>
                Quản lý đơn hàng
            </a-menu-item>
            <a-menu-item key="User Management">
                <template #icon>
                    <Icon icon="ph:user-bold" />
                </template>
                Quản lý người dùng
            </a-menu-item>
        </a-menu>

        <a-menu
            :style="{ width: collapsed ? '64px' : '256px', marginTop: 'auto', marginBottom: '2rem' }"
            id="admin-side-logout"
            mode="inline"
            theme="dark"
            :inline-collapsed="collapsed"
            :selected-keys="[]"
        >
            <a-menu-item key="Logout" @click="handleLogout">
                <template #icon> <Icon icon="ph:sign-out" /> </template>
                Đăng xuất
            </a-menu-item>
        </a-menu>
    </div>
</template>

<style lang="less" scoped>
* {
    transition: all ease 0.2s !important;
}
</style>

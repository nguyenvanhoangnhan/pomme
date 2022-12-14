import { useLoadingStore } from "@/stores/loading"
import { useAuthStore } from "@/stores/auth"
import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            name: "Home",
            path: "/",
            component: () => import("@/views/home/index.vue"),
            meta: {
                title: "Home",
                layout: "home",
                auth: "customer",
            },
        },
        {
            name: "Login",
            path: "/login",
            component: () => import("@/views/login/index.vue"),
            meta: {
                title: "Đăng nhập",
                layout: "auth",
                auth: false,
            },
        },
        {
            name: "Register",
            path: "/register",
            component: () => import("@/views/register/index.vue"),
            meta: {
                title: "Đăng ký",
                layout: "auth",
                auth: false,
            },
        },
        {
            name: "Reset Password",
            path: "/reset-password",
            component: () => import("@/views/reset-password/index.vue"),
            meta: {
                title: "Khôi phục mật khẩu",
                layout: "auth",
                auth: false,
            },
            children: [
                {
                    name: "Reset Password OTP",
                    path: "auth-otp",
                    component: () => import("@/views/reset-password/auth-otp/index.vue"),
                    meta: {
                        title: "Xác thực OTP",
                    },
                },
            ],
        },
        {
            name: "About",
            path: "/about",
            component: () => import("@/views/about/index.vue"),
            meta: {
                auth: "customer",
            },
        },
        {
            name: "Cart",
            path: "/cart",
            component: () => import("@/views/cart/index.vue"),
            meta: {
                title: "Giỏ hàng",
                layout: "default",
                auth: "customer",
            },
        },
        {
            name: "Checkout",
            path: "/checkout",
            component: () => import("@/views/checkout/index.vue"),
            meta: {
                title: "Thanh toán",
                layout: "default",
                auth: "customer",
            },
        },
        {
            name: "Wishlist",
            path: "/wishlist",
            component: () => import("@/views/wishlist/index.vue"),
            meta: {
                title: "Yêu thích",
                layout: "default",
                auth: "customer",
            },
        },
        {
            name: "Order List",
            path: "/orders",
            component: () => import("@/views/orders/index.vue"),
            meta: {
                title: "Danh sách đơn hàng",
                layout: "default",
                auth: "customer",
            },
        },
        {
            name: "Order Detail",
            path: "/order/:id",
            component: () => import("@/views/order/_id/index.vue"),
            meta: {
                title: "Chi tiết đơn hàng",
                layout: "default",
                auth: "customer",
            },
        },
        {
            name: "Products",
            path: "/products",
            component: () => import("@/views/products/index.vue"),
            meta: {
                auth: "customer",
            },
        },
        {
            name: "Shoe Detail",
            path: "/product/shoe/:id",
            component: () => import("@/views/product/shoe/_id/index.vue"),
            meta: {
                auth: false,
            },
        },
        {
            name: "Accessory Detail",
            path: "/product/accessory/:id",
            component: () => import("@/views/product/accessory/_id/index.vue"),
            meta: {
                auth: false,
            },
        },
        {
            name: "Clothes Detail",
            path: "/product/clothes/:id",
            component: () => import("@/views/product/clothes/_id/index.vue"),
            meta: {
                auth: false,
            },
        },
        {
            name: "404",
            path: "/:pathMatch(.*)*",
            component: () => import("@/views/404/index.vue"),
            meta: {
                title: "404",
                layout: "empty",
                auth: false,
            },
        },
        {
            name: "Admin",
            path: "/admin",
            component: () => import("@/views/admin/index.vue"),
            meta: {
                title: "Admin",
                layout: "admin",
                auth: "admin",
            },
            redirect: (to) => {
                return { name: "Product Management - List" }
            },
            children: [
                {
                    name: "Order Management",
                    path: "/admin/orders",
                    component: () => import("@/views/admin/orders/index.vue"),
                    meta: {
                        title: "Quản lý đơn hàng",
                    },
                    children: [
                        {
                            name: "Order Management - Detail",
                            path: "/admin/orders/:id",
                            component: () => import("@/views/admin/orders/_id/index.vue"),
                            meta: {
                                title: "Chi tiết đơn hàng",
                            },
                        },
                    ],
                },
                {
                    name: "User Management",
                    path: "/admin/users",
                    component: () => import("@/views/admin/users/index.vue"),
                    meta: {
                        title: "Quản lý người dùng",
                    },
                },
                {
                    name: "Product Management - List",
                    path: "/admin/products",
                    component: () => import("@/views/admin/products/list/index.vue"),
                    meta: {
                        title: "Danh sách sản phẩm",
                    },
                    children: [
                        {
                            name: "Product Management - Edit Shoe",
                            path: "/admin/products/edit/shoe/:id",
                            component: () => import("@/views/admin/products/edit/shoe/_id/index.vue"),
                            meta: { title: "Chỉnh sửa sản phẩm" },
                        },
                        {
                            name: "Product Management - Edit Accessory",
                            path: "/admin/products/edit/accessory/:id",
                            component: () => import("@/views/admin/products/edit/accessory/_id/index.vue"),
                            meta: { title: "Chỉnh sửa sản phẩm" },
                        },
                        {
                            name: "Product Management - Edit Clothes",
                            path: "/admin/products/edit/clothes/:id",
                            component: () => import("@/views/admin/products/edit/clothes/_id/index.vue"),
                            meta: { title: "Chỉnh sửa sản phẩm" },
                        },
                    ],
                },
                {
                    name: "Product Management - Create",
                    path: "/admin/products/create",
                    component: () => import("@/views/admin/products/create/index.vue"),
                    meta: {
                        title: "Thêm sản phẩm",
                    },
                    children: [
                        {
                            name: "Product Management - Create Shoe",
                            path: "/admin/products/create/shoe",
                            component: () => import("@/views/admin/products/create/shoe/index.vue"),
                        },
                        {
                            name: "Product Management - Create Accessory",
                            path: "/admin/products/create/accessory",
                            component: () => import("@/views/admin/products/create/accessory/index.vue"),
                        },
                        {
                            name: "Product Management - Create Clothes",
                            path: "/admin/products/create/clothes",
                            component: () => import("@/views/admin/products/create/clothes/index.vue"),
                        },
                    ],
                },
            ],
        },
    ],
})

const DEFAULT_TITLE = "Pomme"
router.afterEach((to, from) => {
    const title = to.meta.title ? `Pomme ${to.meta.auth === "admin" ? "Admin" : ""} | ` + to.meta.title : DEFAULT_TITLE
    document.title = title
    useLoadingStore().loadingOff()
})

router.beforeEach(async (to, from) => {
    console.log(to.fullPath)
    useLoadingStore().loadingOn()
    if (to.meta.auth && !useAuthStore()?.data?.user) {
        router.push({ name: "Login" })
        return
    }
    //  if customer try to access admin page => redirect to home
    if (useAuthStore()?.data?.user?.role === "customer" && to.meta.auth === "admin") {
        router.push("/")
        return
    }
    // if admin try to access customer page => redirect to admin page
    if (useAuthStore()?.data?.user?.role === "admin" && to.meta.auth === "customer") {
        router.push({ name: "Product Management - List" })
    }
})

export default router

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
                layout: "default",
            },
        },
        {
            name: "Login",
            path: "/login",
            component: () => import("@/views/login/index.vue"),
        },
        {
            name: "About",
            path: "/about",
            component: () => import("@/views/about/index.vue"),
        },
        {
            name: "Products",
            path: "/products",
            component: () => import("@/views/products/index.vue"),
        },
        {
            name: "Product Detail",
            path: "/product/:id",
            component: () => import("@/views/products/_id/index.vue"),
        },
    ],
})

export default router

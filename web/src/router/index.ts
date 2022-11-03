import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            component: () => import("@/views/home/index.vue"),
            meta: {
                title: "Home",
                layout: "admin",
            },
        },
        {
            path: "/login",
            component: () => import("@/views/login/index.vue"),
        },
        {
            path: "/about",
            component: () => import("@/views/about/index.vue"),
        },
        {
            path: "/products",
            component: () => import("@/views/products/index.vue"),
        },
        {
            path: "/products/:id",
            component: () => import("@/views/products/_id/index.vue"),
        },
    ],
})

export default router

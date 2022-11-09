<script setup lang="ts">
import { Icon } from "@iconify/vue"
import { ref } from "vue"
defineProps<{}>()
const subscribeEmail = ref("")
const handleSubscribe = () => {
    console.log(subscribeEmail.value)
}
</script>

<template>
    <div class="footer flex bg-[#4C4C4C] text-white w-screen p-8 mt-auto">
        <div class="footer__left flex flex-col items-center justify-center gap-4 w-60 min-w-40">
            <img src="/images/store.png" class="w-full" alt="#" />
            <RouterLink
                :to="{ name: 'Home' }"
                class="h-10 font-bold w-full max-w-[400px] bg-white border-white text-black border-2 flex justify-center items-center text-[16px] cursor-pointer hover:text-primary hover:border-primary transition-all duration-300 group"
            >
                <span class="transition-all translate-x-2 group-hover:-translate-x-2">TÌM CỬA HÀNG</span>
                <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
            </RouterLink>
        </div>
        <div class="footer__right flex-1 px-24 flex flex-col gap-8">
            <div class="row footer__nav flex justify-between w-full">
                <section class="footer__nav__section">
                    <h2 class="title">Sản phẩm</h2>
                    <ul>
                        <li><RouterLink to="#"> Giày nam </RouterLink></li>
                        <li><RouterLink to="#"> Giày nữ </RouterLink></li>
                        <li><RouterLink to="#"> Thời trang & Phụ kiện </RouterLink></li>
                        <li><RouterLink to="#"> Sale-off </RouterLink></li>
                    </ul>
                </section>
                <section class="footer__nav__section">
                    <h2 class="title">Về công ty</h2>
                    <ul>
                        <li><RouterLink to="#"> Tuyển dụng </RouterLink></li>
                        <li><RouterLink to="#"> Liên hệ nhượng quyền </RouterLink></li>
                        <li><RouterLink to="#"> Về Pomme </RouterLink></li>
                    </ul>
                </section>
                <section class="footer__nav__section">
                    <h2 class="title">Hỗ trợ</h2>
                    <ul>
                        <li><RouterLink to="#"> FAQs </RouterLink></li>
                        <li><RouterLink to="#"> Bảo mật thông tin </RouterLink></li>
                        <li><RouterLink to="#"> Chính sách chung </RouterLink></li>
                        <li><RouterLink to="#"> Tra cứu đơn hàng </RouterLink></li>
                    </ul>
                </section>
                <section class="footer__nav__section">
                    <h2 class="title">Liên hệ</h2>
                    <ul>
                        <li>Email góp ý</li>
                        <li>nguyen.vh.nhan@gmail.com</li>
                        <li>Hotline</li>
                        <li>+84 854 xxx xxx</li>
                    </ul>
                </section>
            </div>
            <div class="row flex gap-8">
                <div class="social">
                    <h2 class="title uppercase font-bold">Social</h2>
                    <ul class="flex gap-2">
                        <li>
                            <RouterLink to="#">
                                <Icon icon="ph:facebook-logo" :width="28" :height="28" />
                            </RouterLink>
                        </li>
                        <li>
                            <RouterLink to="#">
                                <Icon icon="ph:twitter-logo" :width="28" :height="28" />
                            </RouterLink>
                        </li>
                        <li>
                            <RouterLink to="#">
                                <Icon icon="ph:instagram-logo" :width="28" :height="28" />
                            </RouterLink>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="row">
                <h2 class="title uppercase font-bold">Đăng ký nhận mail</h2>
                <div class="flex gap-4 w-[512px]">
                    <AInput v-model:value="subscribeEmail" placeholder="Email" />
                    <div
                        class="h-10 font-bold px-12 bg-white border-white text-black border-2 flex justify-center items-center text-[16px] cursor-pointer hover:text-primary hover:border-primary transition-all duration-300 group"
                        @click="handleSubscribe"
                    >
                        <span class="transition-all translate-x-2 group-hover:-translate-x-2">Subscribe</span>
                        <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
                    </div>
                </div>
            </div>
            <div class="row">Copyright © 2022 Pomme. All rights reserved.</div>
        </div>
    </div>
</template>

<style lang="less" scoped>
.footer__nav__section {
    @apply px-2;
    .title {
        @apply font-bold uppercase;
    }
    ul {
        @apply flex flex-col gap-1 text-[#ccc];
        li a {
            @apply whitespace-nowrap;
        }
    }
}
.min-w-40 {
    min-width: calc(40 * 0.25rem);
}
</style>

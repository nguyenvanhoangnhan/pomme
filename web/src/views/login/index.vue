<script setup lang="ts">
import { useAuthStore } from "@/stores/auth"
import { reactive } from "vue"
import { useRouter } from "vue-router"
import { Icon } from "@iconify/vue"
interface LoginFormState {
    email: string
    password: string
}

defineProps<{}>()
const auth = useAuthStore()
const router = useRouter()
if (auth.token) {
    // push back to home "/"
    router.push("/")
}

//handle form
const loginFormState = reactive<LoginFormState>({
    email: "",
    password: "",
})
const onFinish = () => {
    // login
}
const onFinishFailed = (errInfo: any) => {
    // handle error
}
</script>

<template>
    <div id="login" class="my-auto">
        <!-- Title -->
        <h1 class="login__title font-black text-5xl mb-16">Đăng nhập</h1>

        <!-- Login form -->
        <AForm class="login__form" :model="loginFormState" layout="vertical" @finish="onFinish" @finishFailed="onFinishFailed">
            <AFormItem name="email" :rules="[{ required: true, message: 'Xin vui lòng nhập email!' }]">
                <AInput type="text" size="large" v-model:value="loginFormState.email" placeholder="Email" auto-complete="off">
                    <template #prefix> <Icon icon="ph:envelope-simple-bold" /> </template
                ></AInput>
            </AFormItem>
            <AFormItem name="password" :rules="[{ required: true, message: 'Xin vui lòng nhập mật khẩu!' }]">
                <AInput type="password" size="large" v-model:value="loginFormState.password" placeholder="Mật khẩu" auto-complete="off">
                    <template #prefix> <Icon icon="ph:lock-simple-bold" /> </template
                ></AInput>
            </AFormItem>
            <div class="forgot-password mb-2 flex justify-end">
                <RouterLink to="#" class="inline-flex items-center justify-end group gap-0 -mr-3">
                    <span class="transition-all group-hover:-translate-x-2"> Quên mật khẩu? </span>
                    <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
                </RouterLink>
            </div>
            <AFormItem>
                <AButton size="large" class="font-bold" type="primary" html-type="submit" block> Đăng nhập </AButton>
            </AFormItem>
        </AForm>

        <!-- Suggest create new account -->
        <div class="login__suggest-register flex flex-col mt-20">
            <span class="text-center text-[16px] mb-2 cursor-default">Bạn chưa có tài khoản à?</span>

            <RouterLink
                to="/register"
                class="h-10 font-bold w-full max-w-[336px] bg-white border-black border-2 flex justify-center items-center text-[16px] cursor-pointer hover:text-primary hover:border-primary transition-all duration-300 group"
            >
                <span class="transition-all translate-x-2 group-hover:-translate-x-2">Đăng ký ngay</span>
                <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
            </RouterLink>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

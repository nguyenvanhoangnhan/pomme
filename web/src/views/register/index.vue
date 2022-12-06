<script setup lang="ts">
import { useAuthStore } from "@/stores/auth"
import { reactive } from "vue"
import { useRouter } from "vue-router"
import { Icon } from "@iconify/vue"
import { Modal } from "ant-design-vue"
import { useLoadingStore } from "@/stores/loading"

defineProps<{}>()
const auth = useAuthStore()
const router = useRouter()
if (auth.data.user) {
    // push back to home "/"
    router.push("/")
}

//handle form
const registerForm = reactive<RegisterForm>({
    name: "",
    email: "",
    password: "",
    password_confirmation: "",
})
const onFinish = () => {
    const data = {
        name: registerForm.name,
        email: registerForm.email,
        password: registerForm.password,
        password_confirmation: registerForm.password_confirmation,
    }
    useLoadingStore().loadingOn()
    auth.register(data)
        .then(() => {
            Modal.success({
                title: "Đăng ký thành công",
                content: "Nhấn OK để chuyển đến trang đăng nhập",
            })
            router.push("/login")
        })
        .catch((err) => {
            Modal.error({
                title: "Đăng ký thất bại",
                content: err,
            })
        })
        .finally(() => {
            useLoadingStore().loadingOff()
        })
}
const onFinishFailed = (errInfo: any) => {
    Modal.error({
        title: "Đăng ký thất bại",
        content: errInfo,
    })
}
</script>

<template>
    <div id="register" class="my-auto">
        <!-- Title -->
        <h1 class="register__title font-black text-5xl mb-16">Đăng ký</h1>

        <!-- Register form -->
        <AForm class="register__form" :model="registerForm" layout="vertical" @finish="onFinish" @finishFailed="onFinishFailed">
            <AFormItem name="name" :rules="[{ required: true, message: 'Xin vui lòng nhập trường này!' }]">
                <AInput type="text" size="large" v-model:value="registerForm.name" placeholder="Họ và tên">
                    <template #prefix> <Icon icon="ph:user-bold" /> </template
                ></AInput>
            </AFormItem>
            <AFormItem name="email" :rules="[{ required: true, message: 'Xin vui lòng nhập trường này!' }]">
                <AInput type="text" size="large" v-model:value="registerForm.email" placeholder="Email">
                    <template #prefix> <Icon icon="ph:envelope-simple-bold" /> </template
                ></AInput>
            </AFormItem>
            <AFormItem name="password" :rules="[{ required: true, message: 'Xin vui lòng nhập trường này!' }]">
                <AInput type="password" size="large" v-model:value="registerForm.password" placeholder="Mật khẩu">
                    <template #prefix> <Icon icon="ph:lock-simple-bold" /> </template
                ></AInput>
            </AFormItem>
            <AFormItem name="password_confirmation" :rules="[{ required: true, message: 'Xin vui lòng nhập trường này!' }]">
                <AInput type="password" size="large" v-model:value="registerForm.password_confirmation" placeholder="Xác nhận mật khẩu">
                    <template #prefix> <Icon icon="ph:lock-simple-bold" /> </template
                ></AInput>
            </AFormItem>
            <AFormItem>
                <AButton size="large" class="font-bold" type="primary" html-type="submit" block> Đăng ký </AButton>
            </AFormItem>
        </AForm>

        <!-- Suggest sign in -->
        <div class="login__suggest-register flex flex-col mt-20">
            <span class="text-center text-[16px] mb-2 cursor-default">Bạn có tài khoản rồi à?</span>

            <RouterLink
                to="/login"
                class="h-10 font-bold w-full max-w-[336px] bg-white border-black border-2 flex justify-center items-center text-[16px] cursor-pointer hover:text-primary hover:border-primary transition-all duration-300 group"
            >
                <span class="transition-all translate-x-2 group-hover:-translate-x-2">Tới trang đăng nhập</span>
                <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
            </RouterLink>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

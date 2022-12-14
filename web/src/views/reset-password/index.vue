<script setup lang="ts">
import { useAuthStore } from "@/stores/auth"
import { reactive, ref } from "vue"
import { useRouter } from "vue-router"
import { Icon } from "@iconify/vue"
interface ResetPwdFormState {
    email: string
}

defineProps<{}>()
const auth = useAuthStore()
const router = useRouter()
if (auth.data.user) {
    // push back to home "/"
    router.push("/")
}

//handle form
const resetPwdFormState = reactive<ResetPwdFormState>({
    email: "",
})
const handling = ref(false)

const onFinish = async () => {
    console.log(resetPwdFormState.email)

    try {
        handling.value = true
        // fake calling api
        await new Promise((resolve) => setTimeout(resolve, 3000))

        // => handle success
        localStorage.setItem(
            "resetPwd",
            JSON.stringify({
                email: resetPwdFormState.email,
                expiredAt: new Date().getTime() + 1000 * 60 * 3,
            })
        )
        router.push("/reset-password/auth-otp")
    } catch (err) {
        console.log(err)
    } finally {
        handling.value = false
    }
}
const onFinishFailed = (errInfo: any) => {
    // handle error
}
</script>

<template>
    <div id="reset-pwd" class="my-auto">
        <!-- nested route -->
        <RouterView />

        <!-- Title -->
        <h1 class="reset-pwd__title font-black text-5xl mb-16">Khôi phục mật khẩu</h1>
        <div class="back-to-login mb-2 flex justify-end">
            <RouterLink :to="{ name: 'Login' }" class="inline-flex items-center justify-end group gap-0 -mr-3">
                <span class="transition-all group-hover:-translate-x-2"> Trở về trang đăng nhập? </span>
                <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
            </RouterLink>
        </div>
        <!-- Reset password form -->
        <AForm class="reset-pwd__form" :model="resetPwdFormState" layout="vertical" @finish="onFinish" @finishFailed="onFinishFailed">
            <AFormItem name="email" :rules="[{ required: true, message: 'Xin vui lòng nhập email!' }]">
                <AInput type="text" size="large" v-model:value="resetPwdFormState.email" placeholder="Email" auto-complete="off">
                    <template #prefix> <Icon icon="ph:envelope-simple-bold" /> </template
                ></AInput>
            </AFormItem>
            <AFormItem>
                <button
                    type="submit"
                    class="h-10 font-bold w-full max-w-[336px] bg-white border-black border-2 flex justify-center items-center text-[16px] cursor-pointer hover:text-primary hover:border-primary transition-all duration-300 group"
                    :class="handling ? 'cursor-not-allowed border-primary' : ''"
                >
                    <template v-if="!handling">
                        <span class="transition-all translate-x-2 group-hover:-translate-x-2">Tiếp tục</span>
                        <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
                    </template>
                    <!-- disable button when handling -->
                    <template v-else>
                        <Icon icon="fluent:spinner-ios-20-filled" class="animate-spin text-primary" :width="20" :height="20" />
                    </template>
                </button>
            </AFormItem>
        </AForm>
    </div>
</template>

<style lang="less" scoped></style>

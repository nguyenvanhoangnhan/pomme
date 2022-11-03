<script setup lang="ts">
import { useAuthStore } from "@/stores/auth"
import { useRouter } from "vue-router"

defineProps<{}>()

const auth = useAuthStore()
const router = useRouter()
if (auth.token) {
    // push back to home "/"
    router.push("/")
}
</script>

<template>
    <div class="w-screen h-screen flex flex-col justify-center items-center">
        <div class="login-form-container">
            <div class="title ant-row">
                <h1 class="ant-col-offset-8 font-bold">Login</h1>
            </div>
            <AForm :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }">
                <AFormItem label="Username" name="username" rules="required">
                    <AInput />
                </AFormItem>
                <AFormItem label="Password" name="password" rules="required">
                    <AInput type="password" />
                </AFormItem>
            </AForm>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

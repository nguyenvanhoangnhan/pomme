<script setup lang="ts">
import { useAuthStore } from "@/stores/auth"
import { useRouter } from "vue-router"
import { Icon } from "@iconify/vue"
import { onMounted, ref } from "vue"
import $ from "jquery"
defineProps<{}>()
const auth = useAuthStore()
const router = useRouter()

const isSuccess = ref(false)
const isHandling = ref(false)
const email = ref("")
if (auth.token) {
    // push back to home "/"
    router.push("/")
}
onMounted(() => {
    const resetPwd = JSON.parse(localStorage.getItem("resetPwd"))
    if (!resetPwd || resetPwd.expiredAt < new Date().getTime() || !resetPwd?.email) {
        localStorage.removeItem("resetPwd")
        router.push("/reset-password")
        return
    }
    email.value = resetPwd.email
    OTPInput()
    document.getElementById
})

const OTPInput = () => {
    // eslint-disable-next-line no-undef
    $("#otp > *[id]").on("keydown", (event) => {
        const index = Number($(event.target).attr("index"))
        const value = $(event.target).val()
        if (event.key === "Backspace") {
            if (index === 1 && value === "") return
            if (index === 1 && value !== "") {
                $(event.target).val("")
                return
            }
            if (value === "") {
                $(event.target).val("")
                $(`#otp > #otp${index - 1} `).focus()
                return
            }
            return
        }
        if (Number(event.key) >= 0 && Number(event.key) <= 9) {
            $(event.target).val(event.key)
            if (index < 6) {
                $(`#otp > #otp${index + 1} `).focus()
            }
            return
        }
        event.preventDefault()
    })
}
const handleSubmitOTP = async () => {
    const otpCode = $<HTMLInputElement>("#otp > *[id]")
        .toArray()
        .reduce((res, element) => {
            return res + element.value
        }, "")

    if (otpCode.length !== 6) {
        // handle nhập thiếu otp
        return
    }

    // handle submit otp
    try {
        isHandling.value = true
        // fake api calling
        await new Promise((resolve) => setTimeout(resolve, 3000))

        // handle isSuccess
        isSuccess.value = true
        localStorage.removeItem("resetPwd")
    } catch (err) {
        // handle error (sai otp)
        console.log(err)
    } finally {
        isHandling.value = false
    }
}
const handleClose = () => {
    localStorage.removeItem("resetPwd")
    router.push("/reset-password")
}
</script>

<template>
    <div id="confirm-otp" class="fixed w-screen h-screen top-0 left-0 z-[888] bg-black bg-opacity-40 flex items-center justify-center">
        <div class="bg-white p-8 items-center relative text-center flex flex-col gap-8">
            <template v-if="isSuccess">
                <div>
                    <Icon icon="ph:check-circle-light" class="text-primary" :width="80" :height="80" />
                    <h2 class="font-bold text-primary">Khôi phục mật khẩu thành công!!</h2>
                </div>
                <RouterLink
                    :to="{ name: 'Login' }"
                    class="h-10 font-bold w-full max-w-[336px] bg-white border-black border-2 flex justify-center items-center text-[16px] cursor-pointer hover:text-primary hover:border-primary transition-all duration-300 group"
                >
                    <span class="transition-all translate-x-2 group-hover:-translate-x-2">Trở về trang đăng nhập</span>
                    <Icon icon="ph:arrow-right-bold" class="opacity-0 -translate-x-6 group-hover:-translate-x-1 group-hover:opacity-100 transition-all" />
                </RouterLink>
            </template>
            <template v-else-if="isHandling">
                <div class="loading w-[320px] h-[270px] flex items-center justify-center">
                    <Icon icon="vaadin:spinner-arc" class="text-primary animate-spin" :width="40" :height="40" />
                </div>
            </template>
            <template v-else>
                <Icon icon="ph:x-circle" :width="28" :height="28" class="cursor-pointer absolute top-4 right-4" @click="handleClose" Cancel />
                <div class="flex flex-col gap-2 items-center mt-8">
                    <div class="flex flex-col text-center">
                        <span>Nhập OTP được gửi đến mail</span>
                        <span class="font-bold">{{ email }}</span>
                    </div>
                    <div class="flex items-center text-primary cursor-pointer"><span class="font-bold">Gửi lại OTP</span></div>
                </div>

                <div id="otp" class="flex flex-row text-center mt-5 gap-4">
                    <input
                        v-for="index in 6"
                        class="border border-primary h-10 w-10 text-center form-control focus:outline-none focus:ring-2 ring-primary transition-all"
                        type="text"
                        :id="`otp${index}`"
                        maxlength="1"
                        :index="index"
                        :key="index"
                    />
                </div>
                <div class="buttons flex gap-4 w-full">
                    <AButton size="large" @click="handleClose" block> Trở lại </AButton>
                    <AButton type="primary" size="large" @click="handleSubmitOTP" block> Xác nhận </AButton>
                </div>
            </template>
        </div>
    </div>
</template>

<style lang="less" scoped></style>

<script setup lang="ts">
import { useAuthStore } from "@/stores/auth"
import { computed } from "@vue/reactivity"
import { Icon } from "@iconify/vue"
defineProps<{}>()
const auth = useAuthStore()
const email = computed(() => auth.email)
</script>

<template>
    <div class="bg-gray-800 text-white w-screen h-screen flex flex-col justify-center items-center">
        <Icon icon="bi:house-fill" :width="40" :height="40" />
        <h1>Home</h1>
        <p>This is the home page.</p>
        <p v-if="email">You are logged in as {{ email }}</p>
        <p v-else>You are not logged in. -> <router-link to="/login">Login</router-link></p>
    </div>
</template>

<style lang="less" scoped></style>

<script setup lang="ts">
defineProps<{}>()
</script>

<template>
    <div class="__auth__">
        <div class="flex flex-col justify-start left p-8 w-[400px]">
            <RouterLink to="/" class="cursor-pointer">
                <img src="/granny-smith-logo.svg" alt="logo" class="h-[60px]" />
            </RouterLink>
            <slot />
        </div>
        <div class="right p-8 hidden lg:block flex-1">
            <div class="bg-image w-full h-full">
                <div class="w-full h-full bg-black bg-opacity-25 text-white text-[4vw] leading-none font-bold p-[4vw] flex items-end">
                    One more step <br />
                    to walk more <br />
                    comfortable steps
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped>
.__auth__ {
    @apply flex w-screen h-screen justify-center;
}
.bg-image {
    background-color: #44af7d;
    background-image: url(/images/auth-layout-img.jpg);
    background-position: center;
    background-size: cover;
}
</style>

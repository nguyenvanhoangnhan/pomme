<script setup lang="ts">
import { Icon } from "@iconify/vue"
</script>

<template>
    <div class="header__bottom flex flex-wrap justify-between">
        <div class="header__bottom__left py-2 pl-24">
            <RouterLink to="/" class="flex flex-col items-center justify-center">
                <img src="/granny-smith-logo.svg" alt="logo" class="h-[60px]" />
            </RouterLink>
        </div>
        <ul class="header__bottom__middle nav flex items-center gap-6">
            <li class="nav__item">
                <RouterLink :to="{ name: 'Products' }" class="nav__item__link">
                    Sản phẩm
                    <Icon icon="ph:caret-down-bold" :width="20" :height="20" />
                </RouterLink>
            </li>
            <li class="nav__separate-line"></li>
            <li class="nav__item">
                <RouterLink to="#" class="nav__item__link">
                    Nam
                    <Icon icon="ph:caret-down-bold" :width="20" :height="20" />
                </RouterLink>
            </li>
            <li class="nav__separate-line"></li>
            <li class="nav__item">
                <RouterLink to="#" class="nav__item__link">
                    Nữ
                    <Icon icon="ph:caret-down-bold" :width="20" :height="20" />
                </RouterLink>
            </li>
            <li class="nav__separate-line"></li>
            <li class="nav__item">
                <RouterLink to="#" class="nav__item__link"> Sale off </RouterLink>
            </li>
        </ul>
        <div class="header__bottom_right flex items-center justify-center pr-8">
            <AInput placeholder="Tìm kiếm" size="large" style="width: 250px">
                <template #prefix>
                    <Icon icon="ph:magnifying-glass-bold" />
                </template>

            </AInput>
        </div>
    </div>
</template>

<style lang="less" scoped>
.nav__item {
    @apply uppercase font-black text-xl;
    &__link {
        @apply flex items-center gap-1 whitespace-nowrap;
    }
}
.nav__separate-line {
    @apply bg-slate-200 h-1/3 whitespace-nowrap;
    width: 2px;
}
</style>

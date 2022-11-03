<script setup lang="ts">
import { markRaw, ref, watch } from "vue"
import { useRoute } from "vue-router"
import DefaultLayout from "@/layouts/default/index.vue"

// handle layout
const route = useRoute()
const layout = ref()
watch(
    () => route.meta?.layout as string | undefined,
    async (metaLayout: string | undefined) => {
        try {
            const component = metaLayout && (await import(/* @vite-ignore */ `@/layouts/${metaLayout}/index.vue`))
            layout.value = markRaw(component?.default || DefaultLayout)
        } catch (e) {
            layout.value = markRaw(DefaultLayout)
        }
    },
    { immediate: true }
)
</script>

<template>
    <component :is="layout">
        <RouterView />
    </component>
</template>

<style scoped>
.logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
}
.logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
    filter: drop-shadow(0 0 2em #42b883aa);
}
</style>

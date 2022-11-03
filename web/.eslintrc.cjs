module.exports = {
    root: true,
    parser: "vue-eslint-parser",
    parserOptions: {
        parser: "@typescript-eslint/parser",
    },
    extends: ["plugin:vue/strongly-recommended", "eslint:recommended", "@vue/typescript/recommended", "prettier"],
    plugins: ["@typescript-eslint", "prettier"],
    rules: {
        "prettier/prettier": "error",
        // for naming file index.vue
        "vue/multi-word-component-names": "off",

        // defineProps no warning on type {}
        "@typescript-eslint/ban-types": "off",

        // not needed for vue 3
        "vue/no-multiple-template-root": "off",
    },
}

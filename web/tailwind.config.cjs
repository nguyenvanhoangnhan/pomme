/* eslint-disable no-undef */
/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
    theme: {
        extend: {
            colors: {
                primary: "#44af7d",
                secondary: "#808080",
            },
        },
    },
    plugins: [],
}

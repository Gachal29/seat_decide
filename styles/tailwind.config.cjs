module.exports = {
    variants: {
        extend: {
        },
    },
    content: [
        "./*.html",
        "../templates/**/*.html",
        "../js/**/*.{js}"
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require("daisyui"),
    ],
    daisyui: {
    }
}
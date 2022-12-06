<script setup lang="ts">
import NavButton from "@/components/atoms/NavButton.vue"
</script>

<template>
    <div class="home__introduce h-[400px] flex justify-center">
        <div class="flex flex-col justify-center items-center gap-3">
            <div class="text-right scale-125">
                <span class="text-base font-bold"> Xin chào, đây là </span>
                <span class="text-5xl text-primary font-bold uppercase" style="font-family: 'Montserrat', sans-serif">Pomme</span>
                <br />
                <span class="text-base font-bold"> - Vườn táo rộng hơn cả Eden</span>
            </div>
            <NavButton :on-click="() => $router.push({ name: 'Products' })" class="w-[400px] mt-4"> Dạo một vòng quanh vườn </NavButton>
        </div>
    </div>
    <HomeCarousel />
    <div class="divider--dashed my-8"></div>
    <div class="container mx-auto mb-8">
        <div class="mb-8 text-center font-black text-2xl uppercase">Danh mục mua hàng</div>
        <div class="grid grid-cols-3 gap-x-4 w-full text-white">
            <div class="home__catalogy home-bg-catalogy-1">
                <div class="bg-black bg-opacity-30 w-full h-full text-center">
                    <div class="pt-4 lg:pt-16">
                        <RouterLink :to="{ name: 'Products', query: { type: 'shoe' } }"> Giày </RouterLink>
                    </div>
                    <ul>
                        <li><RouterLink :to="{ name: 'Products', query: { type: 'shoe', series: 'GSmith' } }"> GSmith </RouterLink></li>
                        <li><RouterLink :to="{ name: 'Products', query: { type: 'shoe', series: 'Crispin' } }"> Crispin </RouterLink></li>
                        <li><RouterLink :to="{ name: 'Products', query: { type: 'shoe', series: 'Shizuka' } }"> Shizuka </RouterLink></li>
                        <li><RouterLink :to="{ name: 'Products', query: { type: 'shoe', series: 'Rhode' } }"> Rhode </RouterLink></li>
                    </ul>
                </div>
            </div>
            <div class="home__catalogy home-bg-catalogy-2">
                <div class="bg-black bg-opacity-30 w-full h-full text-center">
                    <div class="pt-4 lg:pt-16">
                        <RouterLink :to="{ name: 'Products', query: { type: 'accessory' } }"> Phụ kiện </RouterLink>
                    </div>
                    <ul>
                        <li><RouterLink :to="{ name: 'Products', query: { type: 'accessory', category: 'shock' } }"> Tất </RouterLink></li>
                        <li><RouterLink :to="{ name: 'Products', query: { type: 'accessory', category: 'tote' } }"> Túi Tote </RouterLink></li>
                        <li><RouterLink :to="{ name: 'Products', query: { type: 'accessory', category: 'backpack' } }"> Balo </RouterLink></li>
                        <li><RouterLink :to="{ name: 'Products', query: { type: 'accessory', category: 'shoelace' } }"> Dây giày </RouterLink></li>
                    </ul>
                </div>
            </div>
            <div class="home__catalogy home-bg-catalogy-3">
                <div class="bg-black bg-opacity-30 w-full h-full text-center">
                    <div class="bg-black bg-opacity-30 w-full h-full text-center">
                        <div class="pt-4 lg:pt-16">
                            <RouterLink :to="{ name: 'Products', query: { type: 'clothes' } }"> Áo quần </RouterLink>
                        </div>
                        <ul>
                            <li><RouterLink :to="{ name: 'Products', query: { type: 'clothes', category: 'tee' } }"> Áo thun </RouterLink></li>
                            <li><RouterLink :to="{ name: 'Products', query: { type: 'clothes', category: 'hoodie' } }"> Hoodie </RouterLink></li>
                            <li><RouterLink :to="{ name: 'Products', query: { type: 'clothes', category: 'sweatshirt' } }"> Áo dài tay </RouterLink></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="less">
.custom-position-pagination {
    position: absolute;
    transform: scale(200%) translateX(-25%);
    bottom: 10px;
    left: 50%;
    .carousel__pagination-item > button.carousel__pagination-button.carousel__pagination-button--active::after {
        background: #41b883 !important;
    }
    .carousel__pagination-item > button.carousel__pagination-button::after {
        width: 36px;
        height: 3px;
    }
}
</style>

<style lang="less" scoped>
.home-bg-catalogy-1 {
    background-image: url("/images/home/catalogy/catalogy-1.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
.home-bg-catalogy-2 {
    background-image: url("/images/home/catalogy/catalogy-2.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
.home-bg-catalogy-3 {
    background-image: url("/images/home/carousel/0.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.home__catalogy {
    aspect-ratio: 4/3;
}
.home__catalogy > div {
    @apply text-center w-full;
    a {
        @apply font-black text-2xl uppercase;
    }
    ul {
        @apply flex flex-col gap-2 mt-4;
        li a {
            @apply text-base font-bold;
        }
    }
}
</style>

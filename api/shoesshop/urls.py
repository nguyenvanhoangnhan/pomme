from rest_framework import routers
from shoesshop.views import (
    ShoeView,
    UserView,
    ImageView,
    ProductView,
    ProductView,
    AccessoryView,
    ClothesView,
    UserLoveProductView,
    UserCartProductView,
)
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)


router = routers.SimpleRouter()
router.register(r"user_profiles", UserView)
router.register(r"shoe", ShoeView)
router.register(r"clothes", ClothesView)
router.register(r"accessory", AccessoryView)
router.register(r"user-cart-product", UserCartProductView)
router.register(r"user-love-product", UserLoveProductView)
urlpatterns = [
    path("register/", UserView.as_view({"post": "create"})),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login-refresh/", TokenRefreshView.as_view(), name="login_refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    # -----------------------------------------
    path("upload-image/", ImageView.as_view()),
    # -----------------------------------------
    path("shoe/page/<int:page>/", ShoeView.getListShoe),
    # -----------------------------------------
    path("clothes/page/<int:page>/", ClothesView.getListClothes),
    path(
        "clothes/filter/page/<int:page>/<int:category>/<int:sale>/<int:price>/",
        ClothesView.filterClothes,
    ),
    # -----------------------------------------
    path("accessory/page/<int:page>/", AccessoryView.getListAccessory),
    path(
        "accessory/filter/page/<int:page>/<int:category>/<int:sale>/<int:price>/",
        AccessoryView.filterAccessory,
    ),
    # -----------------------------------------
    path("product/page/<int:page>/", ProductView.getListProduct),
    path("product/page/<int:page>/<str:key>/", ProductView.searchProduct),
    path(
        "product/filter/page/<int:page>/<int:sale>/<int:price>/",
        ProductView.filterProduct,
    ),
    path("", include(router.urls)),
]

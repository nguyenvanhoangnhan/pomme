from rest_framework import routers
from .ProductOrderView import (
        UserOrderView,
        OrderProductList,
        OrderProductDetail,
        
)
  # OrderProductView
from .accessoryView import AccessoryView
from .productView import ProductView
from .clothesView import ClothesView
from .imageView import ImageView
from .shoeView import ShoeView
from shoesshop.views import (
    UserView,
    UserLoveProductView,
    UserCartProductView,
)
from django.urls import path, include
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="ShoeShopAPI",
        default_version='1.0.0',
        description= "API documentation of App"
        
        
    ),
    public= True
    
)

router = routers.SimpleRouter()
router.register(r"user_profiles", UserView)
router.register(r"shoe", ShoeView)
router.register(r"clothes", ClothesView)
router.register(r"accessory", AccessoryView)
router.register(r"user-cart-product", UserCartProductView)
router.register(r"user-love-product", UserLoveProductView)
urlpatterns = [
    path('swagger/schema/',schema_view.with_ui('swagger',cache_timeout=0),name =" swagger-schema"),
    path("register/", UserView.as_view({"post": "create"})),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login-refresh/", TokenRefreshView.as_view(), name="login_refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    # -----------------------------------------
    path("upload-image/", ImageView.as_view()),
    # -----------------------------------------
    path("shoe/page/<int:page>/", ShoeView.getListShoe),
    path("shoe_product/", ShoeView.getShoeByProductId),
    
    
    path("shoe/shoechild/<int:shoe>/", ShoeView.getShoeChild),
    path(
        "shoe/filter/page/<int:page>/<int:gender>/<int:shape>/<str:series>/<int:sale>/<int:price>/",
        ShoeView.filterShoe,
    ),
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
    path("product/<int:id>/", ProductView.getProductByID),
    
    path("product/detail/<int:id>/", ProductView.getDetailTypeByID),
    path("product/<int:id>/", ProductView.deleteProduct),
    path("product/page/<int:page>/", ProductView.getListProduct),
    path("product/page/<int:page>/<str:key>/", ProductView.searchProduct),
    path(
        "product/filter/page/<int:page>/<int:sale>/<int:price>/",
        ProductView.filterProduct,
    ),
    # -------------------------------------------
    path("order-products/", OrderProductList.as_view()),
    path("order-products/<int:pk>/", OrderProductDetail.as_view()),
    
    
    
    
    path("user-order/", UserOrderView.list),
    
    # path("orderproduct/", OrderProductView.list),
    path("user-order/<int:pk>/", UserOrderView.retrieve),
    path("", include(router.urls)),
]

from rest_framework import routers
from shoesshop.views import ShoeView, UserView, ImageView
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)


router = routers.SimpleRouter()
router.register(r"user_profiles", UserView)
router.register(r"shoe", ShoeView)

urlpatterns = [
    path("register/", UserView.as_view({"post": "create"})),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login-refresh/", TokenRefreshView.as_view(), name="login_refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("upload-image/", ImageView.as_view()),
    path("shoe/page/<int:page>/", ShoeView.getListShoe),
    path("", include(router.urls)),
]

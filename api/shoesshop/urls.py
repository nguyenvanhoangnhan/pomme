
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenBlacklistView

from shoesshop.views import UserView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user_profiles', UserView)

urlpatterns = [
    path('register/', UserView.as_view({'post': 'create'})),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login-refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('', include(router.urls)),
]

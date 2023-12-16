from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('message.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

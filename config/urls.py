from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_simplejwt import views as jwt_views

from loans_api.loans.routers import router as loans_router

from .schema import schema_view


urlpatterns = [
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(loans_router.urls)),
]

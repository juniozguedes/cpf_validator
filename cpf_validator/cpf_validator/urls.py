
from django.contrib import admin
from django.urls import include,path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('cpf/', include('cpf.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh', TokenRefreshView.as_view()),
]

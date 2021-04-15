
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('cpf/', include('cpf.urls')),
    path('admin/', admin.site.urls),
]

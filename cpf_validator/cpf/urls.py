from django.urls import path

from . import views

urlpatterns = [
    path('list/denied', views.DeniedCpfViewSet.as_view(), name='denied'),
    path('details', views.CpfDetail.as_view(), name='retrieve_delete')
]
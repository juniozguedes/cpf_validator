from django.urls import path

from . import views

urlpatterns = [
    path('list', views.List.as_view(), name='list'),
    path('denied', views.Denied.as_view(), name='denied'),
    path('details', views.Detail.as_view(), name='details'),
    path('create', views.Create.as_view(), name='create'),
]

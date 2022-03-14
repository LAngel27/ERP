from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_home, name='sale'),
    path("list_view/", views.list_view_sales, name="sale_list")
]

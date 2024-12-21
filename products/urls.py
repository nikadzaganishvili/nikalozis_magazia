from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('create_product/', views.create_product, name='create_product'),
    path('product/<int:product_id>/update/', views.update_product, name='product_update'),
    path('product/<int:product_id>/delete/', views.delete_product, name='product_delete'),
]

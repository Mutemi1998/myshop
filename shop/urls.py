from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'shop'
urlpatterns = [
    # product and category apis
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('product/', views.ProductViewSet.as_view(), name='product'),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('category/', views.CategoryViewSet.as_view(), name='product'),


    ##Legacy codes to be removed
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]

# router = routers.DefaultRouter()
# router.register('product', views.ProductViewSet, basename='product')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
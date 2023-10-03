from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'shop'
urlpatterns = [
    # product and category apis
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('products/', views.ProductViewSet.as_view(), name='product'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('categories/', views.CategoryViewSet.as_view(), name='product'),
    path('ratings/createOrEdit/', views.CreateRatingView.as_view(), name='create-rating'),
    path('reviews/createOrEdit/', views.CreateReviewView.as_view(), name='create-review'),
    path('ratings/', views.RatingViewSet.as_view(), name='create-rating'),
    path('reviews/', views.RatingViewSet.as_view(), name='create-review'),


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
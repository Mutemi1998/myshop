from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm
from rest_framework import viewsets, generics, status
from rest_framework import permissions
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response


# get all products 
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, 
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

# get product by id and slug
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                         slug=slug,
                                         available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

class CategoryViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

class CategoryDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]



class ProductViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    


class CreateRatingView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        product_id = self.request.data.get('product')
        try:
            product = Product.objects.get(pk=product_id)
            return Rating.objects.get(user=user, product=product)
        except (Rating.DoesNotExist, Product.DoesNotExist):
            return None


    def create(self, request, *args, **kwargs):
        user = self.request.user
        product_id = self.request.data.get('product')
        # Check if the user has already rated this product
        existing_rating = Rating.objects.filter(user=user, product=product_id).first()

        if existing_rating:
            # If the user has already rated this product, update the existing rating
            serializer = self.get_serializer(existing_rating, data=request.data, partial=True)
        else:
            # If this is a new rating, create it with the user
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_instance = Product.objects.get(pk=product_id)
        serializer.validated_data['product'] = product_instance
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        product = self.request.data.get('product')  # Assuming you send the product ID in the request data
        try:
            return Review.objects.get(user=user, product=product)
        except Review.DoesNotExist:
            return None
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        product_id = self.request.data.get('product')
        # Check if the user has already rated this product
        existing_review = Review.objects.filter(user=user, product=product_id).first()

        if existing_review:
            # If the user has already rated this product, update the existing rating
            serializer = self.get_serializer(existing_review, data=request.data, partial=True)
        else:
            # If this is a new rating, create it with the user
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_instance = Product.objects.get(pk=product_id)
        serializer.validated_data['product'] = product_instance
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RatingViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
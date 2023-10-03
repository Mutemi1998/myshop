from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductThumpNailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductThumpNail
        fields = ['id','image']

class ProductSerializer(serializers.ModelSerializer):
    product_thump_nails = ProductThumpNailSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    
    
    def get_rating(self, obj):
        return obj.calculate_average_rating()

    def get_reviews(self, obj):
        return obj.number_of_reviews()

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
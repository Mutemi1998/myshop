from django.contrib import admin
from .models import *
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(ProductThumpNail)
class Thump_nailsAdmin(admin.ModelAdmin):
   list_display = ['id','product','image'] 
   
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
   list_display = ['product','user','rating'] 
   
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
   list_display = ['product','user','text']
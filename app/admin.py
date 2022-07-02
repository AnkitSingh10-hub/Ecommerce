from django.contrib import admin
from .models import *

class Product_Images(admin.TabularInline):
    model = Product_Image

class Additional_Informations(admin.TabularInline):
    model = Additional_Information


class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images, Additional_Informations)
    list_display = ('product_name', 'Categories', 'section','price')
    list_editable = ('Categories','section')


# Register your models here.
admin.site.register(Slider)
admin.site.register(Banner)
admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Section)
admin.site.register(Product, Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)


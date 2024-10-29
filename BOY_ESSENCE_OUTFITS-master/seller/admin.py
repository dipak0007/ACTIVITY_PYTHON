from django.contrib import admin
from .models import MyProductsModel
from .models import MyCategoriesModel

class MyProductsModelAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'display_image', 'title', 'content', 'category_id', 'mrp_price', 'selling_price', 'discount')

    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'

admin.site.register(MyProductsModel, MyProductsModelAdmin)
admin.site.register(MyCategoriesModel)
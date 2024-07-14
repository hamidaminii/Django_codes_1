from django.contrib import admin
from . import models


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_filter =['is_active','category']

    # prepopulated_fields = {
    #     'slug': ['title']
    # }
    list_display = ['__str__', 'title', 'is_active','price','is_delete']

    list_editable = ['price','is_active']


admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)

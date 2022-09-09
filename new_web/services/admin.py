from django.contrib import admin
from .models import Product, Basket

#admin.site.register(Product)
admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cost']
    # fields = ['id']
    list_filter = ['cost']
    search_fields = ['title']


#admin.site.register(Product, ProductAdmin)

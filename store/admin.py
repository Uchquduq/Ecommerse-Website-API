from django.contrib import admin
from store import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['user__first_name', 'user__last_name']
    list_per_page = 10
    list_select_related = ['user']

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

# admin.site.register(models.Customer)
admin.site.register(models.Promotion)
admin.site.register(models.Collection)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
admin.site.register(models.Address)

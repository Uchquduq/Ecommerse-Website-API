from django.contrib import admin
from store.models import Product
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from tags.models import TaggedItem
from core.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
    }),
)


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


from django.contrib import admin
from tags.models import Tag, TaggedItem

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']

admin.site.register(TaggedItem)

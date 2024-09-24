from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'status')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'published_date', 'categories', 'tags')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

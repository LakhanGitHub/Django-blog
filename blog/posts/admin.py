from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title', 'published_date']
    list_display_links = ['id', 'post_title']
    list_filter = ['published_date']
    search_fields = ['post_title']


#admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
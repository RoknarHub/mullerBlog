from django.contrib import admin

# Register your models here.
from .models import BlogEntry


class BlogEntryAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Blog Entry',       {'fields': ['blog_title', 'blog_content']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Blog Preview',     {'fields': ['blog_description', 'blog_thumbnail', 'is_preview'], 'classes': ['collapse']}),
    ]
    list_display = ('blog_title', 'blog_description', 'pub_date', 'was_published_recently', 'blog_entry_is_released')
    list_filter = ['pub_date']
    search_fields = ['blog_title']

admin.site.register(BlogEntry, BlogEntryAdmin)

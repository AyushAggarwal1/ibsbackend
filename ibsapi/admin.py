from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import homePageForm, blogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_on', 'preview_link')

    def preview_link(self, obj):
        preview_url = reverse('previewBlog', args=[obj.id])
        return format_html('<a href="{}" target="_blank">Preview</a>', preview_url)

    preview_link.short_description = 'Preview'

#home page data
class homePageFormToDisplay(admin.ModelAdmin):
    list_display = ('name', 'date', 'time')

class blogPageFormToDisplay(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')
    
admin.site.register(homePageForm, homePageFormToDisplay)
admin.site.register(blogPost, BlogPostAdmin)
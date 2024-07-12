from django.contrib import admin
from .models import homePageForm, blogPost

# Register your models here.

#home page data
class homePageFormToDisplay(admin.ModelAdmin):
    list_display = ('name', 'date', 'time')

class blogPageFormToDisplay(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')
    
admin.site.register(homePageForm, homePageFormToDisplay)
admin.site.register(blogPost, blogPageFormToDisplay)
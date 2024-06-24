from django.contrib import admin
from .models import homePageForm

# Register your models here.

#home page data
class homePageFormToDisplay(admin.ModelAdmin):
    list_display = ('name', 'date', 'time')
    
admin.site.register(homePageForm, homePageFormToDisplay)
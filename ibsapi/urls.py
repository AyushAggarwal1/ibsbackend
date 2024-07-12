from django.urls import path
from . import views
from .views import main, homeContactListCreate, blogPostlist, postdetail

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', main),
    path('api/contact', homeContactListCreate.as_view(), name="api/contact"),
    path('api/blogs', views.blogPostlist.as_view(), name="api/blogs"),
    path('', main)
]

from django.urls import path
from . import views
from .views import main, homeContactListCreate, blogPostlist, previewBlog

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', main),
    path('api/contact', homeContactListCreate.as_view(), name="api/contact"),
    path('api/blogs', blogPostlist.as_view(), name="api/blogs"),
    path('preview/<int:blog_id>/', views.previewBlog, name='previewBlog'),
    path('', main)
]

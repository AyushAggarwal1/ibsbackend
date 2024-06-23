from django.urls import path
from .views import main, homeContactListCreate

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', main),
    path('contact', homeContactListCreate.as_view(), name="contact"),
    path('', main)
]

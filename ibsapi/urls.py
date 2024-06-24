from django.urls import path
from .views import main, homeContactListCreate

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', main),
    path('api/contact', homeContactListCreate.as_view(), name="api/contact"),
    path('', main)
]

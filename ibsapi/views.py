from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import homePageForm
from .serializers import homePageFormSerializer

# homePageForm kust creater
class homeContactListCreate(generics.ListCreateAPIView):
    queryset = homePageForm.objects.all()   #homepage form attributes
    serializer_class = homePageFormSerializer   #homePage serializer


# Create your views here.
def main(request):
    return render(request, 'index.html')
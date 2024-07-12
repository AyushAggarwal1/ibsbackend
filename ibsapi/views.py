from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.views.decorators.http import require_GET
from django.views import generic

from .models import homePageForm, blogPost
from .serializers import homePageFormSerializer, blogPageFormSerializer

# homePageForm kust creater
class homeContactListCreate(generics.ListCreateAPIView):
    queryset = homePageForm.objects.all()   #homepage form attributes
    serializer_class = homePageFormSerializer   #homePage serializer

# blogs creator
class blogPostlist(generic.ListView):
    queryset = blogPost.objects.filter(status=1).order_by('-created_on')
    serializer_class = blogPageFormSerializer
    template_name = 'blogTemplate.html'
    paginate_by = 4

# class based view for each post
class postdetail(generic.DetailView):
    model = blogPost
    template_name = "blogTemplate.html"

# Create your views here.
def main(request):
    return render(request, 'index.html')
from rest_framework import serializers
from .models import homePageForm, blogPost

# serializer for homePageForm
class homePageFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = homePageForm
        fields = '__all__'

class blogPageFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogPost
        fields = '__all__'
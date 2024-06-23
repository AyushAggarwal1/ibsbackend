from rest_framework import serializers
from .models import homePageForm

# serializer for homePageForm
class homePageFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = homePageForm
        fields = '__all__'
from rest_framework import serializers
from .models import Project

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['id','title','description','link'] 

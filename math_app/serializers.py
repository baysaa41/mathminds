from rest_framework import serializers
from .models import Problems

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        depth = 1
        fields = ['id','type','statement','choices']
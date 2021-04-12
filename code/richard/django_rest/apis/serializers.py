# apis/serializers.py
from rest_framework import serializers
from students import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name',
            'last_name', 
            'cohort',
            'favorite_topic',
            'favorite_teacher',
            'capstone',
        )
        model = models.Student
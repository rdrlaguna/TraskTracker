from rest_framework import serializers
from core.models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "uuid", "name"
        )
        read_only_fields = (
            "uuid",
        )
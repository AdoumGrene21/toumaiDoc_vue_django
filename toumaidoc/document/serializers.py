from rest_framework import serializers

from .models import Type, Document


class TypeSerializer(serializers.ModelSerializer):
                                                                                            
    class Meta:
        model = Type
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url"
        )

class DocumentSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    class Meta:
        model = Document
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "get_file",
            "type" 
        )


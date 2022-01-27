from rest_framework import serializers

from .models import Type, Document, Enseignant

class EnseignantSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Enseignant
        fields = (
            "id",
            "name",
                  
        )


class DocumentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Document
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "get_image",   
            "get_thumbnail",        
        )
        
class TypeSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True)                                                                            
    class Meta:
        model = Type
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "documents",
        )

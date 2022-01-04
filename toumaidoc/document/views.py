from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Document, Type
from .serializers import DocumentSerializer


class LastDocumentsList(APIView):
    def get(self, request, format=None):
        document = Document.objects.all()[0:4]
        serializer = DocumentSerializer(document , many=True)
        return Response(serializer.data)
        
class DocumentDetail(APIView):
    def get_object(self, type_slug, document_slug):
        try:
            return Document.objects.filter(type__slug=type_slug).get(slug=document_slug)
        except Document.DoesNotExist:
            raise Http404
           
    
    def get(self, request, type_slug, document_slug, format=None):
        document = self.get_object(type_slug, document_slug)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

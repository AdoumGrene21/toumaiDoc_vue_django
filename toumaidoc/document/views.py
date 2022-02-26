from asyncore import file_wrapper
import os
from unicodedata import name
from django.conf import settings
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Document, Type, Enseignant
from .serializers import DocumentSerializer, TypeSerializer, EnseignantSerializer

# telechargement de fichier
from django.core.servers.basehttp import *
import mimetypes



@api_view(['POST'])
def modelCreate(request):
    data=request.data
    enseignant = Enseignant.objects.create(
        name = data['name']
    )
    serializer = EnseignantSerializer(enseignant, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def LastDocumentsList(request):
        document = Document.objects.all()[0:4]
        serializer = DocumentSerializer(document , many=True)
        return Response(serializer.data)
  
        
@api_view(['GET'])
def DocumentDetail(request, type_slug, document_slug):
        try:
            document = Document.objects.filter(type__slug=type_slug).get(slug=document_slug)
            serializer = DocumentSerializer(document)
            return Response(serializer.data)


        except Document.DoesNotExist:
            raise Http404
           
   

@api_view(['GET'])
def TypeDetail(request, type_slug):
    try:
        type = Type.objects.get(slug=type_slug)
        serializer = TypeSerializer(type)
        return Response(serializer.data)
    except Type.DoesNotExist:
        raise Http404



def download_image(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='toumaidoc/media')
            response['Content-Disposition']= 'inline'; filename=+os.path.basename(file_path)
            return response
    raise Http404
    








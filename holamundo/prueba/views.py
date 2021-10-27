from enum import auto
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status


@api_view(['GET'])
def homePageView(request,id):
    try:
        autor = Autor.objects.get(id=id)
        autorserialiser = AutorSerializer(autor, many=False)
        return Response({'user': autorserialiser.data} , status=status.HTTP_200_OK)
    except Autor.DoesNotExist:
        return Response({'message': 'autor not found'} , status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def aboutPageView(request):
    autorserializer = AutorSerializer(data=request.data)
    if autorserializer.is_valid():
        autorserializer.save()
        return Response('create')
    else:
        return Response('not created')

    """
 @api_view(['GET'])
    def getTipo(request, id):
        try:
            autor = AutorSer.objects.get(id=id)
            tiposerializer = TipoSerializer(tipo, many=False)
            return Response({'data': tiposerializer.data}, status=status.HTTP_200_OK)
        except Tipo.DoesNotExist:
            return Response({'message': 'Tipo not found'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def createTipo(requet):
        tiposerializer = TipoSerializer(data=requet.data)
        if tiposerializer.is_valid():
            tiposerializer.save()
            return Response({'tipo': tiposerializer.data ,'message': 'tipo created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'tipo not created'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    @api_view(['POST'])
    def updateTipo(request, id):
        try:
            tipo = Tipo.objects.get(id=id)
            tiposerializer = TipoSerializer(instance=tipo , data=request.data)
            if tiposerializer.is_valid():
                tiposerializer.save()
                return Response({'tipo ': tiposerializer.data, 'message': 'tipo update'}, status=status.HTTP_200_OK)
        except Tipo.DoesNotExist:
            return Response({'message': 'tipo not found'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    def deleteTipo(request, id):
        try:
            tipo = Tipo.objects.get(id=id)
            #tiposerializer = TipoSerializer
            tipo.delete()
            return Response({'message': 'tipo delete'}, status=status.HTTP_200_OK)
        except Tipo.DoesNotExist:
            return Response({'message': 'tipo not found'}, status=status.HTTP_404_NOT_FOUND)
    """
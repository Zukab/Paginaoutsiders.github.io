from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer


class ContactView():

            
    @api_view(['POST'])
    def createUser(request):
        contact = ContactSerializer(data=request.data)
        if contact.is_valid():
            contact.save()
            return Response({'message': 'created'})
        else:
            return Response({'message': 'not created'})
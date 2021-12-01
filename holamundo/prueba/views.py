from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Turistic
from .serializers import ContactSerializer, TuristicSerializer
import base64


class ContactView():

            
    @api_view(['POST'])
    def createUser(request):
        contact = ContactSerializer(data=request.data)
        if contact.is_valid():
            contact.save()
            return Response({'message': 'created'})
        else:
            return Response({'message': 'not created'})

    @api_view(['GET'])
    def getTuristic(request):
        try:
            turistic = Turistic.objects.filter()
            turisticSerializer = TuristicSerializer(turistic,many=True)
            print(turisticSerializer.data)
            turisticindex = 0
            for turistic in turisticSerializer.data:
                print(turistic['image'][0])
                image_path = ''
                item = 0;
                for a in turistic['image']:
                    if item != 0:
                        image_path+=a
                    item+=1

                image = open( image_path , 'rb')
                image_read = image.read()
                imagen_base64 = base64.encodebytes(image_read);
                turisticSerializer.data[turisticindex]['image'] = imagen_base64
                turisticindex+=1
            return Response({'data': turisticSerializer.data})
        except Turistic.DoesNotExist:
            return Response({'message': 'Turistic not found'})
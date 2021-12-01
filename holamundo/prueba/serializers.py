from rest_framework import serializers
from .models import *




class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [ 'name','email','phone', 'message']


class TuristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turistic
        fields = [ 'name','ubication','description', 'image']
from rest_framework import serializers
from .models import Bloque1, Bloque2, Bloque3

class Bloque1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bloque1
        fields = ['id', 'presion', 'temperatura', 'calor', 'potencia', 'fecha']

class Bloque2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bloque2
        fields = ['id', 'presion', 'temperatura', 'calor', 'potencia', 'fecha']

class Bloque3_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bloque3
        fields = ['id', 'presion', 'temperatura', 'calor', 'potencia', 'fecha']

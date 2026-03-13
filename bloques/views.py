from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bloque1, Bloque2, Bloque3
from .serializers import Bloque1_Serializer, Bloque2_Serializer, Bloque3_Serializer

class Bloques_All(APIView):
    def get(self, request):
        bloque1 = Bloque1.objects.using('bbddt').all()
        bloque2 = Bloque2.objects.using('bbddt').all()
        bloque3 = Bloque3.objects.using('bbddt').all()

        data = {
            "Bloque1": Bloque1_Serializer(bloque1, many=True).data,
            "Bloque2": Bloque2_Serializer(bloque2, many=True).data,
            "Bloque3": Bloque3_Serializer(bloque3, many=True).data,
        }
        return Response(data)

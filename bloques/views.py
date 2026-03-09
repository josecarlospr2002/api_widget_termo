from django.http import JsonResponse
from .models import Bloque1, Bloque2, Bloque3

def ultimos_registros(request):
    bloque1 = Bloque1.objects.using('bbddt').latest('id')
    bloque2 = Bloque2.objects.using('bbddt').latest('id')
    bloque3 = Bloque3.objects.using('bbddt').latest('id')

    data = {
        "Resultados en Pantalla": {
            "Bloque 1": {
                "id": bloque1.id,
                "presion": bloque1.presion,
                "temperatura": bloque1.temperatura,
                "calor": bloque1.calor,
                "potencia": bloque1.potencia,
                "potencia_calor": bloque1.potencia_calor,
                "fecha": bloque1.fecha,
            },
            "Bloque 2": {
                "id": bloque2.id,
                "presion": bloque2.presion,
                "temperatura": bloque2.temperatura,
                "calor": bloque2.calor,
                "potencia": bloque2.potencia,
                "potencia_calor": bloque2.potencia_calor,
                "fecha": bloque2.fecha,
            },
            "Bloque 3": {
                "id": bloque3.id,
                "presion": bloque3.presion,
                "temperatura": bloque3.temperatura,
                "calor": bloque3.calor,
                "potencia": bloque3.potencia,
                "potencia_calor": bloque3.potencia_calor,
                "fecha": bloque3.fecha,
            },
        }
    }
    return JsonResponse(data)
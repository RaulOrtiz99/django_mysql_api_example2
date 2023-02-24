from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *
import json



# Create your views here.
#esto es para procesar las respuestas
class CompanyView(View):
    
    #este metodo es para procesar las respuestas
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        companies = list(Company.objects.values())

        if len(companies)>0:
            datos = {'message':"Success",'companies':companies}
        else:
            datos = {'message':"Companies not found..."}
        
        return JsonResponse(datos)


        
    
    def post(self,request):
        print(request.body)
        #esto es para convertir el json en un diccionario
        jasondata= json.loads(request.body)
        print("ACA ESTA EL JSON DATA")
        print(jasondata)
        #Este es el proceso de la insercion de datos
        Company.objects.create(name=jasondata['name'],website=jasondata['website'],foundation=jasondata['foundation'])
        print(jasondata['foundation'])
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    
    
    
    
    def put(self,request):
        pass
    
    def delete(self,request):
        pass
    
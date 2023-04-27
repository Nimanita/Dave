from rest_framework.decorators import api_view , permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from measure.database.measureService import measureService


@api_view(['GET', 'POST'])
def handleMeasureOperation(request):
   
    if request.method == 'POST':
        requestBody = JSONParser().parse(request)
        print(requestBody)
        return measureService.addMeasure(requestBody["data"])
    
    if request.method == 'GET':
     
        height = request.GET.get('height')
        weight = request.GET.get('weight')
        age = request.GET.get('age')
        
        measure = {
            "height" : height,
            "weight" : weight,
            "age" : age
        }
        return measureService.getMeasures(measure , True)
       
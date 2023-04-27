from datetime import date
from django.http import JsonResponse
from rest_framework import status
import re
from bson import ObjectId

class Validator:

   
    @classmethod
    def validateMeasure(cls, measure , newMeasure=False):
        
        
        keys = ["age" , "height" , "age" , "waist"]
        if not(isinstance(measure, dict)):
            return False , "Invalid Measure type"
        
        if newMeasure:
            keys.pop()
            
        for key in keys:
            if key not in measure:
                return False , "Incomplete Measure info"
            if not(isinstance(measure[key], str)):
                return False , f"Invalid measure {key}"
                    
        return True , None
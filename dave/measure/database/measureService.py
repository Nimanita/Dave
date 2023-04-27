from measure.database.measureDB import measureDB
import json
import traceback
from dave.utils.ResponseFormatter import ResponseFormatter
from dave.utils.Validator import Validator
import logging
from rest_framework import status
from bson.json_util import dumps
log = logging.getLogger(__name__)

class measureService:

    measuredb = measureDB()
    SEARCHABLE_KEYS = []

    @classmethod
    def addMeasure(cls, measure, isUI=False):
        try:
            
            result , message = Validator.validateMeasure(measure)
          
            if not result:
                return ResponseFormatter.formatAndReturnResponse({"message" : message}, status.HTTP_400_BAD_REQUEST, isUI)
            result = cls.measuredb.addMeasure(measure)
            if result:
                return ResponseFormatter.formatAndReturnResponse({"message" : f"New waist size added successfully"}, status.HTTP_200_OK, isUI)
        except Exception as e:
            exceptionTrace = traceback.format_exc()
            message = f"Failure while adding user" \
                      f"exceptionTrace: {exceptionTrace}" \
                      f" Exception: {str(e)}"
            print(message)
        return ResponseFormatter.formatAndReturnResponse({"message" : " Failed to add waist size"}, status.HTTP_500_INTERNAL_SERVER_ERROR, isUI)

    @classmethod
    def getMeasures(cls, measure , isUI=False):
        try:
           
            result , message = Validator.validateMeasure(measure , True)
            
          
            if not result:
                return ResponseFormatter.formatAndReturnResponse({"message" : message}, status.HTTP_400_BAD_REQUEST, isUI)
       
            result = cls.measuredb.getMeasures(measure)
            if not isUI:
                return result
            else:
                if result:
                    measures = json.loads(dumps(result))
                    return ResponseFormatter.formatAndReturnResponse(measures, status.HTTP_200_OK, isUI)

        except Exception as e:
            exceptionTrace = traceback.format_exc()
            message = f"Failure while getting measures" \
                      f"exceptionTrace: {exceptionTrace}" \
                      f" Exception: {str(e)}"
            print(message , exceptionTrace)
            return None

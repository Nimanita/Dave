import os,sys

import json

from measure.database.measureDB import measureDB
from pathlib import Path
parentFolder = str(Path(__file__).resolve().parent)
print("parentFolder" , parentFolder)
measuresDB =  measureDB()       
with open(parentFolder + '/measurements.json', 'r') as file:
    measures = json.loads(file.read())
  
    for measure in measures:
        measuresDB.collection.update_one({
          "height"  : measure["Height"] , "weight" : measure["Weight"] , "age" : measure["Age"]
        },
        {"$push" : {"waist" : measure["Waist"]
                    }},
         upsert = True
        )                            
       

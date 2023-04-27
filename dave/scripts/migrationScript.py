import os,sys

import json

from measure.database.measureDB import measureDB
from pathlib import Path
parentFolder = str(Path(__file__).resolve().parent)
print("parentFolder" , parentFolder)
measuresDB =  measureDB()       
with open(parentFolder + '/measurements.json', 'r') as file:
    measures = json.loads(file.read())
    print(measures)
    

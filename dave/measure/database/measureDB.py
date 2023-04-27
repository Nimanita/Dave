from bson import ObjectId
from measure.database.MongoConnection import MongoConnection

class measureDB(MongoConnection):

    def __init__(self):
        super(measureDB, self).__init__()
        self.get_collection("measures")
    
    def addMeasure(self, measure):
        result = self.collection.update_one({
          "height"  : measure["height"] , "weight" : measure["weight"] , "age" : measure["age"]
        },
        {"$push" : {"waist" : measure["waist"]
                    }},
         upsert = True
        )                            
        return result.acknowledged 
    
    def getMeasures(self , measure):
        result = self.collection.find_one({"height"  : measure["height"] , "weight" : measure["weight"] , "age" : measure["age"]})
        return result
    
   
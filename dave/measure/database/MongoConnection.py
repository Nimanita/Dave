from pymongo import MongoClient
from django.conf import settings


class MongoConnection(object):
    def __init__(self):
        DATABASES = {'MONGO': {
        'HOST': f"mongodb://127.0.0.1:27017",
        'USERNAME': 'davetestuser',
        'PASSWORD': 'password',
        'DATABASE': 'dave',
        'AUTH_DATABASE': 'dave',
    }}
        
        self.client = MongoClient(host=[DATABASES['MONGO']['HOST']],
                                  username=DATABASES['MONGO']['USERNAME'],
                                  password=DATABASES['MONGO']['PASSWORD']
                                ,
                                 connect=False)
        self.db = self.client[DATABASES['MONGO']['DATABASE']]

    def get_collection(self, name):
        self.collection = self.db[name]
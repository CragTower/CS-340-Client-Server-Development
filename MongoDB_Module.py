import numpy
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username = None, password = None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:47632' % (username, password))
        self.database = self.client["AAC"]

# Creates data entry into mongodb database
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary           
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Reads data from database based on user request
    def read(self, request = None):
        if request:
            data = self.database.animals.find(request, {"_id":False})  # finds user request
        else:
            data = self.database.animals.find({}, {"_id":False})       # finds whole collection
        return data
    
# Updates value at request with user entered new value
    def update(self, request, newValue):
        
        # If user entered a request
        if request is not None:
            # Sets variable to found request
            data = self.database.animals.find(request)
            
            # If request was found
            if data:
                # Updates value of requested document
                self.database.animals.update(request, newValue)
        else:
            print("Criteria not found")
        
# Deletes entry from database
    def delete(self, request = None):
        
        # If user entered a request
        if request is not None:
            # Sets variable to found request
            data = self.database.animals.find(request)
            
            # If request was found
            if data:
                # Deletes entry from database
                self.database.animals.delete_one(data)
        else:
            print("Criteria not found")
        
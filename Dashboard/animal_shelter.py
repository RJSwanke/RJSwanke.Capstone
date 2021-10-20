from pymongo import MongoClient
from bson.objectid import ObjectId

#Connect to AAC database
class AnimalShelter(object):
    def __init__(self, username, password):
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:52079/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:52079')
            self.database = self.client['AAC']
    
    #Create
    def create(self, data):
        if data is not None:
            #self.database.animals.insert(data)  # data should be dictionary            
            insert = self.database.animals.insert(data)  

            #If insert was successful, return True, else, return False
            if insert!=0:
                return True
            else:
                return False           
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    #Read         
    def read(self, data):
        if data is not None:
            try:
                x = self.database.animals.find(data)
                return x
            except Exception as e:
                print("An exception occurred :", e)
                return [e]
                                  
    #Update       
    def update(self, data, new_data):
        if data is not None:
            try:
                a = self.database.animals.update(data, {"$set": new_data}, upsert=True, multi=True)
                return a
            except Exception as e:
                print("An exception occurred :", e)
                return [e]
    
    #Delete
    def delete(self, data):
        if data is not None:
            try: 
                i = self.database.animals.remove(data)
                return i
            except Exception as e:
                print("An exception occurred :", e)
                return [e]
          
        else:
            raise Exception("input search parameter")
            
                

import os
import sys
import json
import pymongo

from dotenv import load_dotenv
load_dotenv()

MongoDbUrl=os.getenv("MONGODB_URL")
print(MongoDbUrl)

import certifi
ca=certifi.where()

import numpy as np
import pandas as pd

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records= list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def pushing_data_to_mongo(self,records, database, collection):
        try:
            self.database=database
            self.records=records
            self.collection=collection

            self.mongo_client=pymongo.MongoClient(MongoDbUrl)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    FILE_PATH='Network_data/NetworkData.csv'
    DATABASE='mlcluster'
    COLLECTION='NetworkData'

    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_converter(FILE_PATH)
    noofrecords=networkobj.pushing_data_to_mongo(records,DATABASE,COLLECTION)
    print(noofrecords)
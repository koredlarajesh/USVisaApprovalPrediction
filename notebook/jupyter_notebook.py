#mongodb+srv://koredla25:koredla25@cluster0.syj7ocj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
import pandas as pd
df=pd.read_csv("notebook/EasyVisa.csv")
print(df.size)
pd.set_option("display.max_rows", None)  # This will display all rows without truncation
pd.set_option("display.max_columns", None)  # This will display all columns without truncation
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())
print(df.shape)
data = df.to_dict(orient="records")
print(data)

DB_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"
CONNECTION_URL = "mongodb+srv://koredla25:koredla25@cluster0.syj7ocj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

import pymongo
from pymongo import MongoClient

# Corrected method name
client = MongoClient(CONNECTION_URL)
database = client[DB_NAME]
collection = database[COLLECTION_NAME]

# Assuming 'data' is the list of dictionaries you want to insert
collection.insert_many(data)

records=collection.find()
print(records)

counter=0
for record in records:
    print(record)
    counter+=1
    if counter==5:
        break

counter=0
for i,j in enumerate(records):
    print(f"{i},{j}")
    counter+=1
    if counter==5:
        break

record_list=list(records)
df=pd.DataFrame(record_list)
print(df.shape)
print(df.head(2))

if "_id" in df.columns.to_list():
    df=df.drop(columns=["_id"],axis=1)

print(df.head(2))
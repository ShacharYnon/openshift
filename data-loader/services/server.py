import os
from fastapi import FastAPI ,HTTPException
from mongoDAL import MongoDal


app = FastAPI(title="MONGO API" ,version="1.0.0")
MONGO_URI = os.getenv("MONGO_URI" ,"mongodb://mongo:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME" ,"testdb")

dal = MongoDal(connection=MONGO_URI ,database_name=MONGO_DB_NAME)

@app.get("/health")
def check_health():
    if dal.get_server_health():
        return {"status":"OK"}
    raise HTTPException(status_code=500 ,detail="db not available")

@app.get("/items/{collection}")
def get_items(collection:str):
    try:
        return dal.show_collection(collection)
    except Exception as e:
        raise HTTPException(status_code=500 ,detail=str(e))


from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get("/")
def getAPI():
    return {"data": "This is first get API"}

@app.get("/post")
def query_param(limit=12,published:bool=True, sort:Optional[str]=None):
    if published:
        return {"data": f"The limit of query parameter is {limit} and Published parameter is {published}"}
    else:
        return {"data": f"The limit of query parameter is {limit}"}

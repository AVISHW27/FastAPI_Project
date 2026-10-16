from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

class Blog(BaseModel):
    title : str
    body : str
    published_at: Optional[str] = None

@app.get("/")
def getAPI():
    return {"data": "This is first get API"}

@app.post("/blog")
def postAPI(blog:Blog):
    return f" the title is {blog.title} and body is {blog.body}"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)

# run this file using the command python main.py command
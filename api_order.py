from fastapi import FastAPI

app = FastAPI()

# CORRECT ORDER: Specific static route PEHLE aayega
@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


# Dynamic route BAAD MEIN aayega
@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}
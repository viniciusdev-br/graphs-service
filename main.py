from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def HomePage():
    return {"Hello": "World"}

class Components(BaseModel):
    start : str
    end : str
    weight : int

class Graph(BaseModel):
    oriented : bool
    weighted : bool
    size : int
    selected_vertex : str
    selected_vertex2 : str
    edges : list[Components]
    
@app.post("/teste")
def Soma(obj : Graph):
    return {"result" : obj.edges, "status" : True}
        
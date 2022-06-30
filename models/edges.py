from pydantic import BaseModel

class Edges(BaseModel):
    start : str 
    end : str 
    weight : int
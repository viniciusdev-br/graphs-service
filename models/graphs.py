from pydantic import BaseModel
from typing import List
from models.edges import Edges

class Graph(BaseModel):
    oriented : bool
    weighted : bool
    size : int
    requirement: int
    selected_vertex : str
    selected_vertex2 : str
    edges : List[Edges]
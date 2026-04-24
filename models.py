from pydantic import BaseModel
from typing import List, Dict

class LogRequest(BaseModel):
    log_text: str

class Node(BaseModel):
    id: str
    type: str

class Edge(BaseModel):
    source: str
    target: str

class AnalysisResponse(BaseModel):
    signals: Dict
    root_causes: List[str]
    repro_steps: List[str]
    nodes: List[Node]
    edges: List[Edge]

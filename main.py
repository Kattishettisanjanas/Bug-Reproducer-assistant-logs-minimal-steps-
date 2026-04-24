from fastapi import FastAPI
from models import LogRequest, AnalysisResponse
from parser import parse_logs
from extractor import extract_signals
from rule_engine import match_rules
from graph_builder import build_graph

app = FastAPI()

@app.post("/analyze", response_model=AnalysisResponse)
def analyze_logs(request: LogRequest):
    parsed = parse_logs(request.log_text)
    signals = extract_signals(parsed)

    root_causes, repro_steps = match_rules(signals)
    nodes, edges = build_graph(signals)

    return {
        "signals": signals,
        "root_causes": root_causes,
        "repro_steps": repro_steps,
        "nodes": nodes,
        "edges": edges
    }

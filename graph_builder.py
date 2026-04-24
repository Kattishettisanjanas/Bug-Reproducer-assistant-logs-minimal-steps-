def build_graph(signals):
    nodes = []
    edges = []

    for m in signals["modules"]:
        nodes.append({"id": m, "type": "module"})

    for e in signals["error_types"]:
        nodes.append({"id": e, "type": "error"})

    modules = signals["modules"]
    for i in range(len(modules) - 1):
        edges.append({
            "source": modules[i],
            "target": modules[i + 1]
        })

    return nodes, edges

import json

def load_rules():
    with open("backend/rules.json") as f:
        return json.load(f)

def match_rules(signals):
    rules = load_rules()
    matches = []

    for rule in rules:
        if rule["error_type"] in signals["error_types"]:
            if any(m in signals["modules"] for m in rule["modules"]):
                matches.append(rule)

    root_causes = []
    repro_steps = []

    for m in matches:
        root_causes.append(m["root_cause"])
        repro_steps.extend(m["repro_steps"])

    return root_causes, repro_steps

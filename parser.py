import re

def parse_logs(log_text: str):
    error_pattern = r'([A-Za-z]+Exception|Error)'
    module_pattern = r'at ([\w\.]+)'

    errors = re.findall(error_pattern, log_text)
    modules = re.findall(module_pattern, log_text)

    return {
        "errors": list(set(errors)),
        "modules": list(set(modules)),
        "raw": log_text
    }

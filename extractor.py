def extract_signals(parsed):
    keywords = []
    text = parsed["raw"].lower()

    if "timeout" in text:
        keywords.append("timeout")
    if "connection refused" in text:
        keywords.append("connection_refused")

    return {
        "error_types": parsed["errors"],
        "modules": parsed["modules"],
        "keywords": keywords
    }

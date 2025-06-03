def analyze_headers(headers):
    issues = []
    from_header = headers.get("From", "")
    reply_to = headers.get("Reply-To", "")
    return_path = headers.get("Return-Path", "")

    if reply_to and reply_to != from_header:
        issues.append("Reply-To address differs from From address.")
    if return_path and return_path != from_header:
        issues.append("Return-Path differs from From address.")

    return {"header_issues": issues}

import re

def detect_phishing_language(body):
    phishing_keywords = ["urgent", "verify", "click here", "reset your password", "login", "account suspended"]
    found = [kw for kw in phishing_keywords if re.search(rf"\b{kw}\b", body, re.IGNORECASE)]
    return {"phishing_keywords": found, "phishing_score": len(found)}

from utils.secure_parser import parse_eml
from detectors import spf_check, dkim_check, dmarc_check, header_check, nlp_analyzer
import email.utils
import os

def run_detection(file_path):
    parsed = parse_eml(file_path)
    headers = parsed["headers"]
    body = parsed["body"]
    raw_bytes = open(file_path, "rb").read()

    domain = headers.get("From", "").split("@")[-1].replace(">", "").strip()
    sender_ip = "127.0.0.1"  # placeholder

    result = {
        "spf": spf_check.check_spf(domain, sender_ip),
        "dkim": dkim_check.check_dkim(raw_bytes),
        "dmarc": dmarc_check.check_dmarc(domain),
        "headers": header_check.analyze_headers(headers),
        "nlp": nlp_analyzer.detect_phishing_language(body),
    }
    return result

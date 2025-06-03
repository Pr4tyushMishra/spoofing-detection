import email
import os

def parse_eml(file_path):
    if not file_path.endswith(".eml") or not os.path.exists(file_path):
        raise ValueError("Invalid or non-existent file.")

    with open(file_path, "rb") as f:
        msg = email.message_from_binary_file(f)

    headers = dict(msg.items())
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and not part.get_filename():
                body += part.get_payload(decode=True).decode(errors="ignore")
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")

    return {"headers": headers, "body": body}

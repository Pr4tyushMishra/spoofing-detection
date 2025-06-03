import dkim

def check_dkim(raw_email_bytes):
    try:
        result = dkim.verify(raw_email_bytes)
        return {"dkim_pass": result}
    except Exception as e:
        return {"dkim_pass": False, "error": str(e)}

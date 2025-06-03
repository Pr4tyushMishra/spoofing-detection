import dns.resolver

def check_dmarc(domain):
    try:
        dmarc_domain = f"_dmarc.{domain}"
        answers = dns.resolver.resolve(dmarc_domain, "TXT")
        for rdata in answers:
            if rdata.to_text().startswith('"v=DMARC1'):
                return {"dmarc_pass": True, "record": rdata.to_text()}
        return {"dmarc_pass": False, "record": None}
    except Exception as e:
        return {"dmarc_pass": False, "error": str(e)}

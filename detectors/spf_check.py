import dns.resolver
import re

def check_spf(domain, sender_ip):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            if rdata.to_text().startswith('"v=spf1'):
                spf_record = rdata.to_text().strip('"')
                if f"ip4:{sender_ip}" in spf_record or f"include:{domain}" in spf_record:
                    return {"spf_pass": True, "record": spf_record}
                return {"spf_pass": False, "record": spf_record}
    except Exception as e:
        return {"spf_pass": False, "error": str(e)}

import re

MALAWI_REGEX = re.compile(r"^\+265(88|99|98)\d{7}$")

def validate_msisdn(phone: str) -> bool:
    """Validate Malawi number: +26588/99/98"""
    return bool(MALAWI_REGEX.match(phone))

def detect_network(phone: str) -> str:
    if not validate_msisdn(phone):
        raise ValueError(f"Invalid MW number: {phone}")
    return "airtel" if phone[4:6] in ("99", "98") else "tnm"

def format_amount(amount: int) -> int:
    if amount < 100:
        raise ValueError("Min 100 MWK")
    return int(amount)

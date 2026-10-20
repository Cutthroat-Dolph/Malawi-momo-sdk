from .utils import validate_msisdn, detect_network, format_amount

class MoMoClient:
    """Unified client for Airtel Malawi + TNM Mpamba"""
    def __init__(self, airtel_id=None, airtel_secret=None, tnm_api_key=None):
        self.airtel_id = airtel_id
        self.airtel_secret = airtel_secret
        self.tnm_api_key = tnm_api_key

    def charge(self, phone: str, amount: int, reference: str) -> dict:
        """Charge a Malawi number - auto detects network"""
        validate_msisdn(phone)
        network = detect_network(phone)
        amount = format_amount(amount)
        
        return {
            "status": "initiated",
            "phone": phone,
            "network": network,
            "amount": amount,
            "reference": reference
        }

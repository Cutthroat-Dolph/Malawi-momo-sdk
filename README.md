# Malawi MoMo SDK
Unified Python SDK for Airtel Money Malawi and TNM Mpamba.

Built for Malawian developers.

## Installation
pip install malawi-momo-sdk

## Usage
from malawi_momo import MoMoClient
client = MoMoClient(airtel_id="xxx", airtel_secret="xxx")
client.charge(phone="+265991234567", amount=5000, reference="order-123")

## Features
- Validates +265 88/99 numbers
- Auto-detects network
- Handles Malawi-specific errors

## Why I built this
No good SDK exists for TNM Mpamba. Airtel Malawi uses different endpoints.
---
### 💼 Hire Me for Integrations

I'm available for Airtel Money & TNM Mpamba integrations for Malawi businesses.

**Payment:** TNM Mpamba - 0896251020 (Elizabeth Edwin Kachale)
**Location:** Blantyre, Malawi
**Contact:** WhatsApp me on this number

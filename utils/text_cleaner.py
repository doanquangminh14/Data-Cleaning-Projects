"""
Text and String Cleaning Utilities
"""

import re
from typing import Optional


def clean_text_field(text: Optional[str], strip_chars: str = "1234567890/_.- ") -> Optional[str]:
    """Strip unwanted numerical and special characters from text fields."""
    if not isinstance(text, str) or text.lower() in {"nan", "none", "n/a", "null", ""}:
        return None
    cleaned = text.strip(strip_chars)
    return cleaned if cleaned else None


def standardize_phone_number(phone_str: Optional[str]) -> Optional[str]:
    """Extract standard 10 digits and return format XXX-XXX-XXXX."""
    if not phone_str:
        return None
    digits = re.sub(r"\D", "", str(phone_str))
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits.startswith("1"):
        return f"{digits[1:4]}-{digits[4:7]}-{digits[7:]}"
    return None


def normalize_boolean_flag(val: Optional[str]) -> Optional[str]:
    """Map ambiguous boolean variants (Y, Yes, True, N, No, False) to 'Yes' / 'No'."""
    if val is None:
        return None
    s = str(val).strip().lower()
    if s in {"y", "yes", "true", "1"}:
        return "Yes"
    elif s in {"n", "no", "false", "0"}:
        return "No"
    return None

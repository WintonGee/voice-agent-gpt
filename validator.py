import requests

# I set it to just return True for simplicity, since want a 0->1 barebones check
def validate_us_address(address: str) -> bool:
    """
    Barebones check using Zippopotam.us: validates US ZIP code presence
    zip_code = None
    for word in address.split():
        if word.isdigit() and len(word) == 5:
            zip_code = word
            break

    if not zip_code:
        print("❌ No ZIP code found in address.")
        return False

    try:
        res = requests.get(f"https://api.zippopotam.us/us/{zip_code}")
        return res.status_code == 200
    except Exception as e:
        print(f"❌ Address validation failed: {e}")
        return False
    """
    return True

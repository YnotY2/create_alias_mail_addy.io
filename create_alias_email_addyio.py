import requests
import json

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    CYAN = '\033[96m'
    BLACK = '\033[30m'

api_token = "YOUR_API_TOKEN_HERE"
url = 'https://app.addy.io/api/v1/aliases'
payload = {
    "domain": "ynoty2.anonaddy.me",
    "local_part": "ynoty2",
}
headers = {
    'Authorization': 'Bearer ' + api_token,
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
}

print(f"Sending request to addy.io-mail to create and fetch new alias")
response = requests.request('POST', url, headers=headers, json=payload)

if response.status_code == 201:
    print(f"{colors.RED}Successful API call!{colors.END}")
    print(f"{colors.RED}---------------------{colors.END}")

    # Parse the JSON response
    data_dict = response.json()
    alias_data = data_dict.get("data", {})

    local_part = alias_data.get("local_part")
    domain = alias_data.get("domain")
    email = alias_data.get("email")

    print(f"{colors.CYAN}Created alias-email:")
    print(f"Alias local_part:{colors.END}:     {colors.YELLOW}{local_part}{colors.END}")
    print(f"{colors.CYAN}alias domain:          {colors.END}{colors.YELLOW}{domain}{colors.END}")
    print(f"{colors.CYAN}full email:    {colors.END}{colors.YELLOW}{email}{colors.END}")

else:
    print(f"Response status failed, with code {response.status_code}")
    print(f"Response content: {response.text}")

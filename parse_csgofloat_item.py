import requests
from src.csfloat_api.models.history_sale_info import ItemSale
from src.utils.logger_setup import logger


payload = {}
headers = {
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
  'Accept': 'application/json, text/plain, */*',
  'Referer': 'https://csfloat.com/item/763582989648135025',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"'
}


errors_amount = 0

def parse_item_by_name(name: str) -> list[ItemSale]:
    global errors_amount

    if errors_amount >= 10:
        raise Exception("Too many errors")

    url = f"https://csfloat.com/api/v1/history/{name}/sales"
    # proxies = {
    #     'http': 'http://arytraxr:sdmlndcd3ckb@45.192.150.180:6363/',
    #     'https': 'http://arytraxr:sdmlndcd3ckb@45.192.150.180:6363/'
    # }
    proxies = {
        'http': 'http://arytraxr:sdmlndcd3ckb@64.137.18.164:6358/',
        'https': 'http://arytraxr:sdmlndcd3ckb@64.137.18.164:6358/'
    }

    response = requests.request("GET", url, data=payload)
    #response = requests.request("GET", url, data=payload, proxies=proxies)
    response.raise_for_status()

    rate_limit_remaining = int(response.headers.get('X-Ratelimit-Remaining'))
    logger.info(f"{name} - Remaining rate limit: {rate_limit_remaining}, "
                f"X-Ratelimit-Limit: {response.headers.get('X-Ratelimit-Limit')}, "
                f"X-Ratelimit-Reset: {response.headers.get('X-Ratelimit-Reset:')}")

    if rate_limit_remaining < 5:
        errors_amount += 1

    return [ItemSale(**sale) for sale in response.json()]

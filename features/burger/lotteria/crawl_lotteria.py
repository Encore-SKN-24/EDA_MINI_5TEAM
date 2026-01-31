import json
import html

import requests

from transform_lotteria import transform_store_data

# 상수
URL = "https://www.lotteeatz.com/searchStore/getStoresListAjax"
JSON_FILE = "lotteria.json"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ko,en;q=0.9,en-US;q=0.8",
    "Origin": "https://www.lotteeatz.com",
    "Referer": "https://www.lotteeatz.com/searchStore",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

PAYLOAD = {
    "query": None,
    "queryType": "NAME",
    "orderType": None,
    "data": {
        "division": {"divcd": ""},
        "adres": {"adres": None, "detailAdres": None},
        "geo": {"point": {"lat": None, "lng": None}},
        "svc": {}
    },
    "radius": 2000,
    "query2_str": "[가-힣]",
    "divcdList": ["10"],
    "page": 1,
    "limit": 2000
}


def fetch_store_data():
    response = requests.post(URL, json=PAYLOAD, headers=HEADERS)
    response.raise_for_status()
    return response.text


def extract_store_info(response_text):
    try:
        hidden_input = response_text.split('<input type="hidden" name="storeList_JSON" value="')[1]
        raw_json = hidden_input.split('" />')[0]
        decoded_json = html.unescape(raw_json)
        return json.loads(decoded_json)
    except (IndexError, json.JSONDecodeError) as e:
        raise Exception('[Lotteria]: Failed to extract or decode JSON') from e


def save_to_json(data, filepath):
    with open(filepath, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    response_text = fetch_store_data()
    raw_store_data = extract_store_info(response_text)
    transformed_data = transform_store_data(raw_store_data)
    save_to_json(transformed_data, JSON_FILE)
    print(f'[Lotteria] Data saved to {JSON_FILE}')

if __name__ == "__main__":
    main()
def transform_store_data(store_data):
    return [
        {
            'storeNm': store.get('storeNm'),
            'adres': store.get('adres', {}).get('adres'),
            'detailAdres': store.get('adres', {}).get('detailAdes'),
            'storecd': store.get('storecd'),
            'lat': store.get('geo', {}).get('point', {}).get('lat'),
            'lng': store.get('geo', {}).get('point', {}).get('lng'),
        }
        for store in store_data
    ]

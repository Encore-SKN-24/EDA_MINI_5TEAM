from region import normalize_sido, normalize_sigungu

def transform_store_data(records):
    out = []
    for store in records:
        out.append({
            "sido": normalize_sido(store.get("sido")),
            "sigungu": normalize_sigungu(store.get("sigungu")),
            "store_name": store.get("store_name"),
            "address": store.get("address"),
            "business_hours": store.get("business_hours"),
        })
    return out

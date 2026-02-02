# count_all.py

import json
from collections import defaultdict

from region import normalize_sido, normalize_sigungu


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 안전장치
# ensure_metrics: 지역에 필요한 지표가 반드시 존재하도록 보장한다는 의미
# 있으면 유지, 없으면 만듦 (없다면 0으로 표기)
# 모든 지역이 같은 dic 객체 공유해서 함수로 뻬둠
def ensure_metrics():
    return {
        "population": 0,
        "crime": 0,
        "violence": 0,
        "burgerking": 0,
        "lotteria": 0,
        "mcdonalds": 0,
        "kfc": 0,
    }


# 매장 리스트(list[dict]) -> {sido: {sigungu: count}}
def count_store_by_region(store_records):
    out = defaultdict(lambda: defaultdict(int))

    for r in store_records:
        sido = normalize_sido(r.get("sido"))
        sigungu = normalize_sigungu(r.get("sigungu"))

        if not sido or not sigungu:
            continue

        out[sido][sigungu] += 1

    return out

# merged[sido][sigungu][key] = value 형태 주입
def upsert_metric(merged, sido, sigungu, key, value):
    merged[sido][sigungu].setdefault("population", 0)
    merged[sido][sigungu].setdefault("crime", 0)
    merged[sido][sigungu].setdefault("violence", 0)
    merged[sido][sigungu].setdefault("burgerking", 0)
    merged[sido][sigungu].setdefault("lotteria", 0)
    merged[sido][sigungu].setdefault("mcdonalds", 0)
    merged[sido][sigungu].setdefault("kfc", 0)

    merged[sido][sigungu][key] = value


def main():
    # count_stores.py에 있던 경로 스타일
    store_files = {
        "kfc": "../burger/kfc/data/kfc.json",
        "burgerking": "../burger/burgerking/data/burgerking.json",
        "lotteria": "../burger/lotteria/data/lotteria.json",
        "mcdonalds": "../burger/mcdonalds/data/mcdonalds.json",
    }

    population_path = "../population/data/population.json"  
    crime_path = "../crime/data/crime.json"                

    # 최종: {sido: {sigungu: {metrics...}}}
    merged = defaultdict(lambda: defaultdict(ensure_metrics))

    #  매장 수 병합 (count)
    for brand, path in store_files.items():
        records = load_json(path)
        if not isinstance(records, list):
            raise ValueError(f"{path}는 list 형태. 현재: {type(records)}")

        counts = count_store_by_region(records)
        for sido, sigungu_map in counts.items():
            for sigungu, cnt in sigungu_map.items():
                upsert_metric(merged, sido, sigungu, brand, merged[sido][sigungu][brand] + cnt)

    # 2) 인구 병합 
    pop_records = load_json(population_path)
    for r in pop_records:
        sido = normalize_sido(r.get("sido"))
        sigungu = normalize_sigungu(r.get("sigungu"))

        # "전국/소계", "서울특별시/소계" 같은 합계행은 제외 
        if not sido or not sigungu or sigungu == "소계" or sido == "전국":
            continue

        # population이 문자열 int로 변환
        try:
            pop_val = int(str(r.get("population")).replace(",", "").strip())
        except Exception:
            continue

        upsert_metric(merged, sido, sigungu, "population", pop_val)

    # 3) 범죄 병합 
    crime_records = load_json(crime_path)
    for r in crime_records:
        sido = normalize_sido(r.get("sido"))
        sigungu = normalize_sigungu(r.get("sigungu"))

        if not sido or not sigungu:
            continue

        # crime / violence
        crime_val = int(r.get("crime", 0) or 0)
        violence_val = int(r.get("violence", 0) or 0)

        upsert_metric(merged, sido, sigungu, "crime", crime_val)
        upsert_metric(merged, sido, sigungu, "violence", violence_val)

    # defaultdict -> dict 변환
    final = {
        sido: {sigungu: dict(metrics) for sigungu, metrics in sigungu_map.items()}
        for sido, sigungu_map in merged.items()
    }

    save_json(final, "../../data.json")
    print("data.json saved")


if __name__ == "__main__":
    main()

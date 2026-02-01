# utils/count_stores.py
import json
from collections import defaultdict

from region import normalize_sido, normalize_sigungu

# json 파일 읽기 -> 파이선 객체(list/dict)으로 반환
# 그냥 json하니까 이름 충돌남
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# 파이선 객체에서 다시 json 파일로 저장
def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 매장 리스트(records)를 지역별로 카운트 -> 반환
# memo: def count_by_region(records: list[dict]) -> dict:
# records: list[dict]-> records 딕셔너리들의 리스트임 
def count_by_region(records)
    out = defaultdict(lambda: defaultdict(int))

    for r in records:
        sido = normalize_sido(r.get("sido"))
        sigungu = normalize_sigungu(r.get("sigungu"))

        if not sido or not sigungu:
            continue

        out[sido][sigungu] += 1

    return out


def brand_counts(merged, counts, brand):
    for sido, sigungu_map in counts.items():
        for sigungu, cnt in sigungu_map.items():
            merged[sido][sigungu][brand] += cnt


def to_plain_dict(nested_defaultdict):
    return {
        sido: {
            sigungu: dict(metrics)
            for sigungu, metrics in sigungu_map.items()
        }
        for sido, sigungu_map in nested_defaultdict.items()
    }


def main():
    files = {
        "kfc": "../burger/kfc/data/kfc.json",
        "burgerking": "../burger/burgerking/data/burgerking.json",
        "lotteria": "../burger/lotteria/data/lotteria.json",
        "mcdonalds": "../burger/mcdonalds/data/mcdonalds.json"
    }

    # 최종 결과: {sido: {sigungu: {brand: count}}}
    merged = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    for brand, path in files.items():
        records = load_json(path)

        # records가 list인지 체크
        if not isinstance(records, list):
            raise ValueError(f"{path}는 매장 리스트(list) 형태. 현재 타입: {type(records)}")

        counts = count_by_region(records)
        brand_counts(merged, counts, brand)

    final = to_plain_dict(merged)
    save_json(final, "../../data.json")

    print("data.json saved")


if __name__ == "__main__":
    main()

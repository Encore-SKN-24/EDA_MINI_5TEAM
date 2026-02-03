# count_all.py

import json
from pathlib import Path
from collections import defaultdict

from region import normalize_sido, normalize_sigungu

_SCRIPT_DIR = Path(__file__).resolve().parent
_FEATURES_DIR = _SCRIPT_DIR.parent
_PROJECT_ROOT = _FEATURES_DIR.parent


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
        sigungu = normalize_sigungu(r.get("sigungu"), sido=sido)

        if not sido or not sigungu or sigungu == "소계" or sido == "소계":
            continue

        # 세종의 경우 모든 하위 행정구역을 "세종시"로 통일
        if sido == "세종":
            sigungu = "세종시"

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


def _collapse_sigungu_into_one(sigungu_map, single_sigungu_name="세종시"):
    """시군구가 없는 세종: 여러 행(도로명 등)을 하나의 시군구 행으로 합침."""
    out = ensure_metrics()
    for _sigungu, metrics in sigungu_map.items():
        for key in out:
            val = metrics.get(key, 0)
            if isinstance(val, (int, float)):
                out[key] += val
    return {single_sigungu_name: out}


def main():
    # 스크립트 위치 기준 절대 경로 (프로젝트 루트/features/utils 어디서 실행해도 동일 동작)
    store_files = {
        "kfc": _FEATURES_DIR / "burger" / "kfc" / "data" / "kfc.json",
        "burgerking": _FEATURES_DIR / "burger" / "burgerking" / "data" / "burgerking.json",
        "lotteria": _FEATURES_DIR / "burger" / "lotteria" / "data" / "lotteria.json",
        "mcdonalds": _FEATURES_DIR / "burger" / "mcdonalds" / "data" / "mcdonalds.json",
    }

    population_path = _FEATURES_DIR / "population" / "data" / "population.json"
    crime_path = _FEATURES_DIR / "crime" / "data" / "crime.json"                

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
        sido_raw = r.get("sido")
        sigungu_raw = r.get("sigungu")

        sido = normalize_sido(sido_raw)
        sigungu = normalize_sigungu(sigungu_raw, sido=sido)

        # 소계 및 전국 제외 (세종 제외)
        if sido != "세종" and (sigungu == "소계" or sido == "소계" or sido == "전국"):
            continue

        if not sido or not sigungu:
            continue

        # 세종의 경우 모든 하위 행정구역을 "세종시"로 통일
        if sido == "세종":
            sigungu = "세종시"

        # population이 문자열 int로 변환
        try:
            pop_val = int(str(r.get("population")).replace(",", "").strip())
        except Exception:
            continue

        # 세종시는 누적 합산
        if sido == "세종":
            current_pop = merged[sido][sigungu].get("population", 0)
            upsert_metric(merged, sido, sigungu, "population", current_pop + pop_val)
        else:
            upsert_metric(merged, sido, sigungu, "population", pop_val)

    # 3) 범죄 병합 (crime.json 기준으로 지역 구조 생성)
    crime_records = load_json(crime_path)
    for r in crime_records:
        sido_raw = r.get("sido")
        sigungu_raw = r.get("sigungu")

        sido = normalize_sido(sido_raw)
        sigungu = normalize_sigungu(sigungu_raw, sido=sido)

        # 소계 제외 (세종 제외)
        if sido != "세종" and (sigungu == "소계" or sido == "소계"):
            continue

        if not sido or not sigungu:
            continue

        # 세종의 경우 모든 하위 행정구역을 "세종시"로 통일
        if sido == "세종":
            sigungu = "세종시"

        # crime / violence
        crime_val = int(r.get("crime", 0) or 0)
        violence_val = int(r.get("violence", 0) or 0)

        # 세종시는 누적 합산
        if sido == "세종":
            current_crime = merged[sido][sigungu].get("crime", 0)
            current_violence = merged[sido][sigungu].get("violence", 0)
            upsert_metric(merged, sido, sigungu, "crime", current_crime + crime_val)
            upsert_metric(merged, sido, sigungu, "violence", current_violence + violence_val)
        else:
            upsert_metric(merged, sido, sigungu, "crime", crime_val)
            upsert_metric(merged, sido, sigungu, "violence", violence_val)

    # defaultdict -> dict 변환
    final = {
        sido: {sigungu: dict(metrics) for sigungu, metrics in sigungu_map.items()}
        for sido, sigungu_map in merged.items()
    }

    save_json(final, _PROJECT_ROOT / "data.json")
    print("data.json saved")


if __name__ == "__main__":
    main()

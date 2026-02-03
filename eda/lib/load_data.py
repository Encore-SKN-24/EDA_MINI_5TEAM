import json
from pathlib import Path

import pandas as pd

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
_DEFAULT_JSON_PATH = _PROJECT_ROOT / "data.json"


def load_data(json_path=None):
    if json_path is None:
        json_path = _DEFAULT_JSON_PATH
    json_path = Path(json_path)

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = []
    for sido, districts in data.items():
        for sigungu, metrics in districts.items():
            record = { 
                'sido': sido,
                'sigungu': sigungu,
                **metrics  # 중첩 데이터 flat
            }
            records.append(record)

    df = pd.json_normalize(records)

    # df 열
    cols = ['sido', 'sigungu', 'population', 'crime', 'violence',
                    'burgerking', 'lotteria', 'mcdonalds', 'kfc']
    df = df[cols]

    return df

if __name__ == '__main__':
    df = load_data()
    print('[load_data] data.json 로드 완료')
    print('[load_data] df.head()')
    print(df.head())
    
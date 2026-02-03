# load_data 사용 가이드

- `data.json` 을 1차원의 데이터프레임 형태로 만들어 데이터 분석에 용이하도록 만든 함수 `load_data.py` 사용 가이드입니다.

## 1. 사전 준비

### 1.1 가상환경 및 의존성 설치

```bash
# 프로젝트 루트
python -m venv .venv
source .venv/bin/activate

# 패키지 설치 (editable로 eda 모듈 인식)
pip install -e .
pip install -r requirements.txt
```

- `pip install -e .` 로 `eda` 패키지가 설치되어 `from eda.lib import load_data` 가 동작합니다.
- `requirements.txt` 에 pandas, jupyter 등 분석에 필요한 패키지가 정의되어 있습니다.

### 1.2 data.json 준비

`load_data()` 는 **프로젝트 루트의 `data.json`** 을 기본으로 읽습니다.  
저장소에 `data.json` 이 없거나 최신으로 갱신하려면 아래 순서로 생성합니다.

1. **버거 프랜차이즈 데이터**: 각 브랜드 크롤러 실행
   - `features/burger/kfc`, `mcdonalds`, `burgerking`, `lotteria` 내 `crawl_*.py`
2. **인구·범죄 데이터**:
   - `features/population/crawl_population.ipynb`, `features/crime/crawl_crime.ipynb` 실행 후
   - `features/population/data/population.json`, `features/crime/data/crime.json` 생성
3. **집계 실행**
   ```bash
   cd features/utils
   python count_all.py
   ```
   → 프로젝트 루트에 `data.json` 이 생성됩니다.

- 이는 추후 통합된 파이프라인으로 확장 예정입니다.

## 2. load_data 사용법

### 2.1 기본 사용 (프로젝트 루트의 data.json)

```python
from eda.lib import load_data

df = load_data()
# df: columns = ['sido', 'sigungu', 'population', 'crime', 'violence',
#                'burgerking', 'lotteria', 'mcdonalds', 'kfc']
```

### 2.2 다른 경로의 JSON 사용

```python
from eda.lib import load_data

df = load_data(json_path="/path/to/other/data.json")
```

### 2.3 노트북에서 실행 위치

- Jupyter를 **프로젝트 루트**에서 실행하면 `load_data()` 만으로 루트의 `data.json` 을 찾습니다.  
  예: `jupyter lab` 또는 `jupyter notebook` 을 프로젝트 루트에서 실행.
- 루트가 아닌 다른 디렉터리에서 실행하는 경우, `load_data(json_path="절대/상대경로/data.json")` 처럼 경로를 넘겨주면 됩니다.

## 3. 반환 데이터 형식

| 컬럼                                         | 설명                  |
| -------------------------------------------- | --------------------- |
| `sido`                                       | 시도(광역)            |
| `sigungu`                                    | 시군구                |
| `population`                                 | 인구                  |
| `crime`                                      | 범죄 총건수           |
| `violence`                                   | 폭력 + 강력 범죄 건수 |
| `burgerking`, `lotteria`, `mcdonalds`, `kfc` | 브랜드별 매장 수      |

# Burger Index & Crime Analysis

# 📊 생활환경의 상대적 여건과 범죄 양상 분석

## 버거지수에 따른 범죄 발생 지역 치안 현황

---

## 📅 프로젝트 기간

- 2026.01.28(수) ~ 2026.02.04(수)

---

# 1. 팀 소개

## 1-1. 팀명

햄스터

## 1-2. 팀원 구성 및 GitHub

| 이름 | 역할 | GitHub |
| --- | --- | --- |
| 김민준 | • Choropleth map, folium 툴을 이용한 시각화 | https://github.com/miin-jun |
| 김유진 | • selenium 활용한 데이터 크롤링<br> • matplotlib, seaborn 활용한 시각화 | https://github.com/shortcut-2 |
| 김지원 | • selenium 활용한 KFC 매장 수 크롤링<br> • JSON 기반 데이터 스키마 통일, 분석용 데이터 정리 및 가공 | https://github.com/edu-ai-jiwon |
| 박세현 | • selenium을 활용하여 burgerking 매장 수 크롤링<br> • 버거지수와 범죄율 데이터로 시각화 히스토그램 그래프 작성 | https://github.com/parksay |
| 임정희 | • 롯데리아 매장찾기 엔드포인트로 POST 요청을 보내 온 HTML의 JSON 추출<br> • 버거지수 데이터를 folium 패키지를 활용해 단계구분도로 시각화 | https://github.com/bigmoooon |

---

# 2. 프로젝트 개요

## 2-1. 프로젝트명

**버거지수에 따른 범죄 발생 지역 치안 현황**

## 2-2. 배경

본 프로젝트 아이디어는 “도시의 발전 수준은 글로벌 패스트푸드 프랜차이즈의 입점 수로 가늠할 수 있다”는 대중적인 인식에서 출발하였다.  

이러한 인식은 흔히 밈(meme)의 형태로 소비되지만, 실제로 The Economist가 1986년부터 발표해 온 빅맥지수(Big Max Index)와 버거 지수는 국내 특정 프랜차이즈의 입점지/상품 가격 등을 통해 사회적 지표를 탐색할 수 있다는 점에서 맞닿아 있다. 

<img width="1084" height="946" alt="big max index" src="https://github.com/user-attachments/assets/038c5b17-9d9a-48ba-9116-0cad460b872b" />

빅맥지수는 동일한 상품(빅맥)의 국가별 가격을 비교하여 구매력 평가(PPP)와 경제 수준을 직관적으로 설명하기 위해 고안된 지표이다. 이는 경제 교과서와 다수의 학술 연구에서도 활용되어 왔다.

이를 통해 우리는 패스트푸드 프랜차이즈가 단순한 소비재가 아니라 다음과 같은 조건을 전제로 입점한다는 점에 주목하였다.

- 일정 수준 이상의 인구 규모와 소비력  
- 상업 인프라 및 유동 인구  
- 지역 생활환경의 밀집도  

즉, 버거 프랜차이즈의 분포는 지역의 사회·경제적 특성과 사람의 활동이 집중되는 공간적 특성을 간접적으로 반영하는 지표로 활용될 수 있다.

<img width="1514" height="1158" alt="busan_news" src="https://github.com/user-attachments/assets/526c4eb3-5dbd-468f-a3d1-bc660fca7358" />

전문가들은 이러한 현상의 원인으로 상업지역 비율, 인프라의 상대적 부족 등 환경 요인의 복합적 작용을 지적한다. 이는 범죄 발생을 인구 활동이 집중되는 공간적 조건과 함께 해석할 필요가 있음을 시사한다.

이에 본 프로젝트는 대중적 인식을 분석 가능한 연구 주제로 확장하여, **버거 프랜차이즈 매장 분포(버거지수)** 와 **범죄 발생 데이터**를 결합·분석하고자 하였다.

---

## 2-3. 프로젝트 소개 및 목표

본 프로젝트는  
**생활환경의 상대적 여건이 사회적 긴장과 범죄 양상에 어떻게 대응하는가**라는 질문에서 출발한 EDA 미니 프로젝트이다.

지역 내 상업·생활 밀집도를 간접적으로 나타내는 지표로 **버거지수(Burger Index)** 를 정의하고, 이를 지역별 범죄 발생 데이터와 결합하여 지역 간 치안 수준의 상대적 차이를 분석하였다.

본 분석은 단순 범죄 건수 비교가 아닌 다음 요소를 고려한다.

1. 인구 대비 범죄율  
2. 범죄 지표 재정의  
3. 지역 단위 데이터 통합  

이를 통해 보다 현실적인 지역 비교를 목표로 한다.

---

# 3. 기술 스택

## 🛠 Tech Stack

| Category | Stack |
|----------|--------|
| **Language** | ![Python](https://img.shields.io/badge/python-blue?style=for-the-badge&logo=python&logoColor=white) |
| **Web Crawling** | ![Selenium](https://img.shields.io/badge/selenium-green?style=for-the-badge&logo=selenium&logoColor=white) |
| **Data Processing** | ![Pandas](https://img.shields.io/badge/pandas-yellow?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-lightblue?style=for-the-badge&logo=numpy&logoColor=white) |
| **Data Visualization** | ![Matplotlib](https://img.shields.io/badge/matplotlib-black?style=for-the-badge&logo=matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/seaborn-darkblue?style=for-the-badge&logo=seaborn&logoColor=white) ![Folium](https://img.shields.io/badge/folium-white?style=for-the-badge&logo=folium&logoColor=black) |


---

# 4. WBS 및 폴더 구조

<img width="1300" height="642" alt="wbs2" src="https://github.com/user-attachments/assets/d21fa293-f402-4ffa-b282-4ceebf95c478" />

```text
burger-crime-eda/
├── features/
│   ├── burger/
│   │   ├── lotteria/
│   │   │   ├── crawl_lotteria.py
│   │   │   ├── transform_lotteria.py
│   │   │   └── lotteria.json
│   │   │
│   │   ├── burgerking/
│   │   │   ├── crawl_burgerking.py
│   │   │   ├── transform_burgerking.py
│   │   │   └── burgerking.json
│   │   │
│   │   ├── mcdonalds/
│   │   │   ├── crawl_mcdonalds.py
│   │   │   ├── transform_mcdonalds.py
│   │   │   └── mcdonalds.json
│   │   │
│   │   └── kfc/
│   │       ├── crawl_kfc.py
│   │       ├── transform_kfc.py
│   │       └── kfc.json
│   │
│   ├── population/
│   │   ├── crawl_population.py
│   │   │── transform_population.py
│   │   └── population.json
│   │
│   └── crime/
│       ├── crawl_crime.py
│       │── transform_crime.py
│       └── crime.json
│
├── docs/
│   └── git_strategy.md
├── main.py
├── data.json                    # 최종 통합 파일
├── requirements.txt
├── .gitignore
└── README.md
```


# 5. 데이터 수집

## 5-1. 범죄 데이터

- 출처: KOSIS(국가통계포털) 공개 통계 자료
- 수집 방식
  - 2024년 연간 전국 시군구 범죄 건수 데이터 활용
- 수집 항목
  - 시·도
  - 시·군·구
  - 범죄 유형: 강력 / 폭력 / 지능 / 풍속 범죄

## 5-2. 버거지수 데이터

- 대상 프랜차이즈: 버거킹 / 롯데리아 / 맥도날드 / KFC
- 전국 매장 대상 수집
- 수집 방식
  - 각 프랜차이즈 공식 홈페이지를 대상으로 웹 크롤링
  - 전국 매장 위치 및 매장 수 직접 수집
  - 사이트 구조에 따라 크롤링 방식 차별화
    - 동적 페이지 및 UI 상호작용이 필요한 경우: Selenium 활용
    - Ajax 요청 기반 사이트의 경우: HTTP 요청 방식 활용
- 수집 항목
  - 매장명
  - 시·도
  - 시·군·구
  - 영업 시간 (영업 중인 매장 여부 확인용)

## 5-3. 인구 데이터

- 출처: KOSIS(국가통계포털) 공개 통계 자료
- 전국 대상 총 248건
- 수집 방식
  - 2024년 연간 전국 시군구 인구수 데이터 활용
  - 범죄 건수를 인구 대비 지표로 환산

---

# 6. 주요 지표 정의

## 6-1. 버거지수 (Burger Index)

- 정의: 특정 지역 내 주요 버거 프랜차이즈 매장 수의 총합  
  → 지역의 생활 밀집도 및 상업 환경 수준을 간접적으로 나타내는 대리 변수

```text
Burger Index = burgerking + lotteria + mcdonalds + kfc
```
## 6-2. Crime 지표

- 구성: 강력 / 폭력 / 지능 / 풍속 범죄
- 정의: `crime`은 특정 범죄 유형에 한정하지 않고, 지역 내 전체 범죄 발생 규모를 포괄적으로 파악하기 위한 집계 지표이다.
- 목적: 지역별 전반적인 범죄 발생 수준 비교

## 6-3. Violence 지표

- 구성: 강력범죄 / 폭력범죄
- 정의: `violence`는 강력범죄와 폭력범죄를 합산한 지표이다.
- 목적: 지역별 체감 치안 수준을 설명하기 위한 범죄 유형 분석
- 강력 범죄 단독 지표 사용 시 발생하는 데이터 공백 문제 보완

<img width="2880" height="1378" alt="범죄율" src="https://github.com/user-attachments/assets/8e585c61-8c42-4962-aef8-ddbe84c60db0" />
<img width="1512" height="262" alt="범죄율 계산" src="https://github.com/user-attachments/assets/357b1d17-f5f1-41a7-99c1-5ad7bf0302d9" />

---

# 7. 데이터 전처리 및 통합

데이터 출처와 수집 방식이 상이하여, 동일한 분석 단위로 결합하기 위해 전처리 과정을 수행하였다.

### 인구·범죄 데이터

- KOSIS 공개 통계(CSV) 활용
- `pandas`, `numpy`를 활용하여 DataFrame 생성 및 전처리
- 불필요한 컬럼 제거 및 컬럼 정리  
  (예: `sido`, `sigungu`, `population` 등)
- 세종시의 경우, 시 하위 단위로 '구'가 없어 세종시 데이터 통합 처리
<img width="1336" height="664" alt="세종시" src="https://github.com/user-attachments/assets/97be7620-e4ae-4aca-91b9-1b3157bc4e52" />

### 버거 프랜차이즈 데이터

- 브랜드별 수집 방식이 상이함
- 주소 체계를 시·도 / 시·군·구 기준으로 통일
- 전처리 후 JSON 구조로 변환
<img width="2166" height="1276" alt="json" src="https://github.com/user-attachments/assets/b136343c-a64a-4823-a284-3b583f8288e7" />

### 데이터 통합

- 모든 데이터를 공통 Key 기준으로 통합
- 이후 지역별 집계, 범죄율 계산, 버거지수 산출에 활용

---

# 8. 분석 인사이트

# 🍔 버거 지수 히트맵
<img width="2426" height="1304" alt="버거지수 히트맵1" src="https://github.com/user-attachments/assets/95bba4ac-feb2-404e-a666-dc829122267c" />
<img width="2370" height="1356" alt="버거지수 히트맵" src="https://github.com/user-attachments/assets/088e8bf1-ad52-4d01-8d10-81109e6fd18f" />

- 위는 버거지수를 나타낸 단계 구분도이다.  
- IQR 기준 이상치는 강남구, 서초구, 중구였으나, 이들은 단순 이상치가 아닌 유동인구가 많은 동시에 업무 지구의 역할을 하는 장소라는 점에서 의미를 가진다.  
- 또한 인구와 버거지수의 상관계수는 **0.511**로, 중간 정도의 상관관계를 가진다.  
- 인구가 많으면 버거지수가 또한 높을 것임을 예상하였으나, 이는 절대적인 인과관계가 아니라는 것을 알 수 있다.  

---

# 🚨 범죄율 등급화 바그래프

<img width="1002" height="718" alt="범죄율 등급화 바그래프" src="https://github.com/user-attachments/assets/ec2cf90f-e4fa-47de-a8be-733c47f96b32" />

- 범죄율을 구간별로 나누어 보니, 범죄율이 높은 구간일수록 대체로 버거지수도 함께 증가하는 경향을 보인다.  
- 버거지수가 높을수록 도시화된 지역이고 인구 밀도도 높을 것이므로 범죄율도 증가하는 것으로 추측된다.  
- 단, 범죄율이 높은 구간에서는 오히려 버거지수가 급격히 낮아지는 구간이 존재한다.  
- 이러한 구간은 인구수가 적고 치안 수준이나 도시 인프라가 부족한 지역에서 오히려 범죄율이 높게 측정되는 현상으로 추측된다.  

---

# 📊 범죄율 등급별 버거지수 분포 (Violin Plot)

<img width="552" height="453" alt="범죄율 등급별 버거지수 분포" src="https://github.com/user-attachments/assets/4707c9c5-5bef-4478-9a2a-21d65987e3a6" />

- 위 그래프는 범죄율 등급별 버거지수 분포를 바이올린 차트로 시각화한 것이다.  
- 이전 그래프는 **5등급 분할**, 본 그래프는 **4분위 값 기준 분할**을 사용하였다.  
- 범죄율은 1등급(낮은 범죄율)부터 4등급(높은 범죄율)까지 정의하였다.  
- 각 등급별 흰 막대는 중앙값을 의미하며, 등급별 차이를 확인할 수 있다.  

- 1등급의 중앙값은 버거지수 0이 가장 많이 분포한다. 이는 범죄율이 낮고 버거지수 또한 낮은 지역이 다수이며, 인구 밀도 자체가 낮은 지역이 많음을 의미한다.  

- 4등급의 경우 버거지수가 1인 지역이 다수 분포하고 있고, 버거지수가 0인 지역의 분포는 적다. 이는 대체로 발달된 지역이며 인구 밀도가 높은 지역이므로 범죄율 또한 높은 등급에 속함을 보여준다. 

- 중앙값이 등급별로 점차 상승하는 경향은  
  **버거지수 증가 → 인구 밀도 증가 → 범죄율 증가**라는 구조적 관계를 시사한다.  

---

# 📈 버거지수별 범죄율 평균 바그래프

<img width="567" height="452" alt="버거지수별 범죄율 평균 바그래프" src="https://github.com/user-attachments/assets/a51920b7-bc04-4dc8-a151-339f280777c5" />

- 버거지수를 반올림하여 지수별 범죄율 평균을 산출한 그래프이다.  
- 버거지수가 높을수록 범죄율이 높아지는 경향은, 인구 밀도가 높아짐에 따라 범죄율이 증가하는 이전 그래프와 동일한 흐름을 보인다.  

- 다만, 버거지수 2-3 구간 사이에서 급격한 증가가 관찰된다.  
- 이는 버거지수 0-2에 속하는 지역이 비수도권 위주이며, 3-4 구간은 수도권에 해당하는 지역이 많기 때문으로 추측된다.  
- 즉, 수도권과 비수도권 간 인구 밀도 차이가 반영된 결과일 가능성이 있다.  

---

# 🗺 주요 도시의 버거지수 단계 구분도

- 경기도, 서울, 강원도, 경상북도  
<img width="1637" height="1035" alt="주요 도시(경기도 외)" src="https://github.com/user-attachments/assets/d29d3949-48ec-4177-9c5e-c05aaa88b74f" />

- 경상남도, 세종특별시, 전라남도, 충청북도
<img width="1478" height="1037" alt="주요도시(경삼남도 외)2" src="https://github.com/user-attachments/assets/bfc54f1b-ce05-41de-9a3c-c7ce22611994" />

- 전라남도, 충청남도, 광주광역시, 대전광역시, 대구광역시, 부산광역시
<img width="1641" height="507" alt="주요도시(전라남도 외) 3" src="https://github.com/user-attachments/assets/d4e1b4aa-a079-440b-8577-e29f0a76ce1a" />
<img width="1538" height="983" alt="주요도시(광주광역시 외)3" src="https://github.com/user-attachments/assets/273c7c50-980e-409c-9062-ac672ca708fc" />

- 울산광역시, 인천광역시  
<img width="1639" height="519" alt="주요도시(울산광역시 외)4" src="https://github.com/user-attachments/assets/8598ae69-30a8-48c8-af7d-905fdb5a4701" />

버거지수와 범죄율의 관계를 지도 시각화 결과를 종합하면 다음과 같은 해석이 가능하다.

> **버거지수가 높은 지역은 대체로 도심·상권·역세권처럼 물가와 수요가 집중된 지역일 가능성이 크다.**  
> 또한 **범죄율이 높은 지역 역시 유동인구가 많고 활동량이 많은 도심·상권·역세권과 겹칠 가능성이 높다.**

따라서,

> “버거지수가 범죄에 직접적인 영향을 준다”는 인과관계라기보다는,  
> **도시성(상권 규모·유동인구)이라는 공통 요인**으로 인해 두 지표가 함께 높게 나타난 것으로 해석할 수 있다.


---

# 9. 한 줄 회고

- 김민준: 범죄 종류 데이터와 범죄율을 folium으로 나타내는 과정에서 결측치가 여러개 발생해서 골치가 아팠지만 이 과정에서 folium이라는 시각화 툴을 다뤄봤다는 점에서 만족을 하지만 다음에는 이 결측치들을 해결하고 안정적으로 시각화를 완성해보고 싶다.
- 김유진: 프로젝트 주제 선정 이후, 팀원들과 디렉토리 구조와 수집해야 할 데이터의 구조를 먼저 설정함으로써 이후 데이터 통합과 가공에 용이하도록 힘썼다. 특히 이전 프로젝트와 다르게 csv 파일이 아닌 json 파일을 선택해 데이터 취합, 데이터 프레임을 만들어 이후 파일 형식이 다르더라도 당황하지 않을 수 있게 되었다. 이후 시각화에 사용하기 위해 계산한 데이터를 추가하는 과정에서 버거지수와 범죄율에서 예상치 못한 결측치가 발생해 난항을 겪었으나, 팀원들과 협의해 결측치를 보완하고 제거할 수 있었다. 향후 프로젝트에서는 프로젝트 기획/수집 단계에서 수집해야 할 데이터 자체에 대한 이해도를 높이는 것이 필요하리라는 것을 다시금 느꼈다.
- 김지원: 전처리 단계에서 데이터 구조를 이해하는 데 많은 시간이 필요했다. 팀 내 정해진 규칙을 바탕으로 JSON 취합과 스키마 통일 과정을 차근히 수행했다. 단순 구현이 아니라 분석을 위한 데이터 구조가 왜 중요한지 고민하는 계기가 되었다. 이번 경험을 통해 데이터 전처리에 대한 기초 역량을 쌓을 수 있었다. 
- 박세현: 만들려던 것과 만들어진 것이 다르다. 아직 머신러닝까지 가지도 않았는데 결측치와 이상치 데이터들을 어떻게 처리해야 할지 골치가 아팠다. 
- 임정희: 시도/시군구를 기준으로 데이터를 병합하는 과정에서 행정 구역의 통합, 개편 또는 크롤링 데이터 자체의 오타 등을 고려하지 않아 정규화 과정에서 매칭 이슈가 생겼다. 결국 하나의 데이터셋을 기준으로 비교하며 통합하였지만 다음부터는 사전 조사를 더 철저히 한 뒤에 정규화 규칙을 작성해야함을 인지해야겠다. 

---

# 참고

- 버거지수 관련 자료: The Economist, *Big Mac Index* (2017)
- 범죄 관련 자료: KBS 뉴스, 「부산 ‘5개 구’에 5대 범죄 집중…원인은?」 (2023.09.13)
- 범죄율 계산법: 지표누리  
  https://www.index.go.kr/unify/idx-info.do?idxCd=4262
- KOSIS: 전국 시군구 인구수 데이터, 전국 시군구 범죄 건수 데이터 (2024)

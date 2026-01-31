import numpy as np
import pandas as pd

crime_df = pd.read_csv('../../범죄발생지_20260131175659.csv')
crime_df = crime_df.T
crime_df.columns = crime_df.iloc[0]


## 불필요한 컬럼제거
crime_df = crime_df.drop(columns='지능범죄')
crime_df = crime_df.drop(columns='풍속범죄')


# 상세한 범죄 데이터는 제거
crime_df = crime_df.iloc[2:,:]

## 컬럼명 중복 돼 있는거 수정
cols = crime_df.columns.tolist()
cols[0] = '나라'
cols[1] = '행정구역'
cols[2] = '도시'
crime_df.columns = cols


# 행정구역/도시 먼저 따로 보관
meta = crime_df[['행정구역', '도시']]

# 숫자 컬럼만 따로 떼서 숫자로 변환
nums = crime_df.drop(columns=['나라', '행정구역', '도시'], errors='ignore')
nums = nums.replace('-', 0)
nums = nums.apply(pd.to_numeric, errors='coerce').fillna(0)

# 같은 이름 컬럼(강력범죄, 폭력범죄 등) 합치기
nums = nums.T.groupby(level=0).sum().T

# 합친 후 meta 다시 붙이기
crime_df = pd.concat([meta, nums], axis=1)


# 컬럼명을 '행정구역','도시','강력범죄','폭력범죄' 순으로
crime_df = crime_df[['행정구역','도시','강력범죄','폭력범죄']]


# 새로운 csv 파일로 저장. transform에서 json 형태로 바꾸기 위해서?
# 이건 좀 gpt 한테 도움 받았음 ㅎㅎ;;
crime_df.to_csv('crime_clean.csv', index=False, encoding='utf-8-sig')


# json 형태로 바꾸기
# 얘도 좀 gpt 한테 도움 받았음 ㅎㅎ;;
crime_df.to_json('crime.json', orient='records', force_ascii=False, indent=2)
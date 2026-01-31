import numpy as np
import pandas as pd


population_df = pd.read_csv('../../도시지역_인구현황_시군구__20260131175637.csv')

# 불필요한 컬럼들 지우기
population_df = population_df.drop(columns=['2024.1','2024.2','2024.3','2024.4','2024.5','2024.6'])


# 불필요해 보이는 행들(맨 위에 두줄) 지우기
population_df = population_df.iloc[2:].reset_index(drop=True)


# 컬럼이름 바꾸기
population_df= population_df.rename(columns={'소재지(시군구)별(1)' :'행정구역',
                              '소재지(시군구)별(2)' : '도시',
                              '2024' : '인구수'
                              })


# 
population_df = population_df.set_index('행정구역')

# json으로 만들기전에 전처리된 csv.
population_df.to_csv('population_clean.csv', index=False, encoding='utf-8-sig')

# json으로 바꾸기
population_df.to_json('population.json', orient='records', force_ascii=False, indent=2)
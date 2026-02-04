SIDO_CODE_TO_NAME = {
    '11': '서울',
    '26': '부산',
    '27': '대구',
    '28': '인천',
    '29': '광주',
    '30': '대전',
    '31': '울산',
    '36': '세종',
    '41': '경기',
    '42': '강원',
    '43': '충북',
    '44': '충남',
    '45': '전북',
    '46': '전남',
    '47': '경북',
    '48': '경남',
    '50': '제주',
    '51': '강원', 
}

SIDO_NAME_TO_CODE = {v: k for k, v in SIDO_CODE_TO_NAME.items()}

# 시도 전체 목록
SIDO_LIST = list(SIDO_CODE_TO_NAME.values())

# 지도 설정
INIT_POS = [36.35, 127.95]
INIT_ZOOM = 7

# 색상 설정
CHOROPLETH_COLOR_SCHEME = 'YlOrRd'

def normalize_sigungu(sido, sigungu):
    """
    시군구명 정규화 - 알려진 불일치 케이스 처리

    Args:
        sido: 시도
        sigungu: 시군구

    Returns:
        정규화된 시군구명
    """
    if not sigungu:
        return sigungu

    # (sido, sigungu) 튜플을 키로 사용한 정규화 매핑
    normalization_map = {
        ('부산', '진구'): '부산진구',
        ('부산광역시', '진구'): '부산진구',
        ('서울', '구로'): '구로구',
        ('전북', '임실군임실읍'): '임실군',
        ('전남', '고흥군고흥읍'): '고흥군',
        ('전남', '장성군장성읍'): '장성군',
        ('경남', '창녕군남지읍'): '창녕군',
        ('충남', '논산시연무읍'): '논산시',
        ('경기', '남양주시화도읍'): '남양주시',

    }

    return normalization_map.get((sido, sigungu), sigungu)


def parse_adress(address):
    """
    주소를 약속된 형식에 맞게
    sido와 sigungu로 분리

    Args:
        address: 주소

    Returns:
        sido: 시도
        sigungu: 시군구
    """

    # 주소 없을 경우 대비
    if not address:
        return None, None

    # 주소를 공백으로 분리
    parts = address.split()
    sido = parts[0] if len(parts) >= 1 else None
    sigungu = parts[1] if len(parts) >= 2 else None

    # 시군구명 정규화
    sigungu = normalize_sigungu(sido, sigungu)

    return sido, sigungu


def transform_store_data(store_data):
    """
    약속된 형식에 맞게 주소를 분리 및 저장
    Args:
        store_data: 주소 데이터
    Returns:
        result[]: 약속된 형식에 맞게 주소를 분리 및 저장
    """
    # 특정 매장명에 대한 sigungu 매핑 (광역시로 들어오는 경우 처리)
    store_name_exceptions = {
        '광주금남로': ('광주', '동구'),
        '광주동림': ('광주', '서구'),
    }

    result = []

    for store in store_data:
        store_name = store.get('storeNm')
        address = store.get('adres', {}).get('adres')
        sido, sigungu = parse_adress(address)

        # 예외 처리: 특정 매장명에 대해 sido/sigungu 오버라이드
        if store_name in store_name_exceptions:
            sido, sigungu = store_name_exceptions[store_name]

        result.append({
            'StoreName': store_name,
            'sido': sido,
            'sigungu': sigungu,
            'storecd': store.get('storecd'),
        })

    return result
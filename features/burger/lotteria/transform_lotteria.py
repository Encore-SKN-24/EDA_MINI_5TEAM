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
    result = []

    for store in store_data:
        address = store.get('adres', {}).get('adres')
        sido, sigungu = parse_adress(address)

        result.append({
            'StoreName': store.get('storeNm'),
            'sido': sido,
            'sigungu': sigungu,
            'storecd': store.get('storecd'),
        })

    return result
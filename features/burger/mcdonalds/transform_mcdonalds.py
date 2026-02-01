import csv
import json

data = []

with open('./data/mcdonalds.csv', encoding='utf-8') as mcdonalds_csv:
    reader = csv.DictReader(mcdonalds_csv)

    # 주소 분할(전체 -> 시군구)
    for row in reader:

        full_address = row.get('address', '')
        
        # 시,군,구까지만 분할(서울은 동까지 수집)
        part_address = full_address.split(' ', 3)
        row['sido'] = part_address[0]
        row['sigungu'] = part_address[1]
        row['dong'] = part_address[2]
        row['else'] = part_address[3]

        data.append(row)

# json 파일 변환
with open('./data/mcdonalds.json', 'w', encoding='utf-8') as mcdonalds_json:
    json.dump(data, mcdonalds_json, indent=4, ensure_ascii=False)

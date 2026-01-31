import csv
import json

data = []

with open('./mcdonalds.csv', encoding='utf-8') as mcdonalds_csv:
    reader = csv.DictReader(mcdonalds_csv)

    # 주소 분할(전체 -> 시군구)
    for row in reader:
        full_address = row.get('주소', '')
        
        # 시,군,구까지만 분할(서울은 동까지 수집)
        part_address = full_address.split(' ', 3)
        row['시/도'] = part_address[0]
        row['군/구'] = part_address[1]
        row['동'] = part_address[2]
        row['기타'] = part_address[3]

        data.append(row)

# json 파일 변환
with open('mcdonalds.json', 'w', encoding='utf-8') as mcdonalds_json:
    json.dump(data, mcdonalds_json, indent=4, ensure_ascii=False)

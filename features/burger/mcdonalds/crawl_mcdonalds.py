from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

path = "chromedriver.exe"
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

# 크롤링 순서
# 필요한 정보 값: 매장명, 주소

store_list = []
last_page = 50

# 1. 페이지 접속

try: 
    url = 'https://www.mcdonalds.co.kr/kor/store/main'
    driver.get(url)
    time.sleep(3)

# 2. 매장명, 주소 수집
    for idx in range(1, last_page + 1):
        time.sleep(2)

        stores = driver.find_elements(By.CSS_SELECTOR, 'ul.border-t.border-t-gray > li')
        for store in stores:
            try:
                name = store.find_element(By.CSS_SELECTOR, 'button.store_links').text
                address = store.find_element(By.CSS_SELECTOR, 'p.text-15.text-gray-text').text
                store_list.append([name, address])
            except:
                continue

    # 3. 다음 페이지 접속
        if idx < last_page:   
            try:
                if idx % 5 == 0:
                    next_list = driver.find_element(By.CSS_SELECTOR, 'button.page_next')
                    next_list.click()
                else:
                    list_page_click = driver.find_elements(By.CSS_SELECTOR, 'div.pagination > ul > li > button')
                    for page_btn in list_page_click:
                        if page_btn.text == str(idx + 1):
                            page_btn.click()
                            break
                time.sleep(2)
            except Exception as e:
                print(f'실패: {e}')

# 4. csv 저장
finally:
    with open('./data/mcdonalds.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['store_name', 'address'])
        writer.writerows(store_list)

print(len(store_list))
driver.quit()
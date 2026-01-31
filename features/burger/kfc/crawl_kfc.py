from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import json

# ip 차단 방지
def create_driver():
    options = Options()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

# 1. 데이터 저장용 리스트 준비 
kfc_list = []

driver = create_driver()
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://www.kfckorea.com/store/findStore")
    time.sleep(5)

    # 지역검색 탭 클릭
    region_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "지역검색")))
    region_tab.click()
    time.sleep(2)

    sido_el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[select-box]")))
    sido_list = [opt.text for opt in Select(sido_el).options if "시,도" not in opt.text]

    for city in sido_list:
        # 시,도 선택 
        sido_select = driver.find_element(By.CSS_SELECTOR, "select[select-box]")
        driver.execute_script("arguments[0].click();", sido_select)
        time.sleep(1)
        driver.find_element(By.XPATH, f"//select[@select-box]//option[text()='{city}']").click()
        time.sleep(2)

        gugun_el = driver.find_element(By.CLASS_NAME, "town")
        gugun_list = [opt.text for opt in Select(gugun_el).options if "구,군" not in opt.text]

        for district in gugun_list:
            # 구,군 선택 
            town_select = driver.find_element(By.CLASS_NAME, "town")
            driver.execute_script("arguments[0].click();", town_select)
            time.sleep(1)
            driver.find_element(By.XPATH, f"//select[contains(@class, 'town')]//option[text()='{district}']").click()
            time.sleep(3)

            stores = driver.find_elements(By.CSS_SELECTOR, "ul.store-item")
            
            for i in range(len(stores)):
                try:
                    current_stores = driver.find_elements(By.CSS_SELECTOR, "ul.store-item")
                    target_store = current_stores[i]
                    
                    # 매장명 클릭하여 상세 팝업 열기
                    name_link = target_store.find_element(By.CSS_SELECTOR, "li.top > a:not(.btn-share)")
                    store_name = name_link.text
                    
                    driver.execute_script("arguments[0].click();", name_link)
                    time.sleep(2)

                    # 상세 정보 추출
                    road_addr = driver.find_element(By.XPATH, "//strong[contains(text(), '도로명')]/following-sibling::span").text
                    full_hours = driver.find_element(By.CSS_SELECTOR, "div.store-info ul li span.txt p").text
                    shop_hours = full_hours.split('\n')[0] 

                    print(f"[{city} {district}] 매장: {store_name} | 위치: {road_addr} | 영업: {shop_hours}")

                    # 2. 데이터 리스트에 추가 (딕셔너리 형태)
                    kfc_list.append({
                        "city": city,
                        "district": district,
                        "store_name": store_name,
                        "address": road_addr,
                        "business_hours": shop_hours
                    })

                    # 팝업 닫기
                    try:
                        close_btn = driver.find_element(By.CSS_SELECTOR, "a.btn-close, button.btn-close")
                        driver.execute_script("arguments[0].click();", close_btn)
                    except:
                        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    
                    time.sleep(1.5)

                except Exception:
                    continue

except Exception as e:
    print(f"전체 오류 발생: {e}")

finally:
    # 3. 모든 루프가 끝난 뒤 파일 저장 실행
    if kfc_list:
        # CSV 저장
        df = pd.DataFrame(kfc_list)
        df.to_csv("kfc_stores_2026.csv", index=False, encoding='utf-8-sig')
        print(f"\nCSV 파일 저장 완료! (총 {len(kfc_list)}개 매장)")

        # JSON 저장
        with open("kfc_stores_2026.json", "w", encoding="utf-8") as f:
            json.dump(kfc_list, f, indent=4, ensure_ascii=False)
        print("JSON 파일 저장 완료!")
    else:
        print("수집된 데이터가 없어 파일을 저장하지 않았습니다.")
    
    # driver.quit() # 확인을 위해 브라우저를 열어두려면 주석 처리
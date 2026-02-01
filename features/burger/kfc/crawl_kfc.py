from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time
import json

from transform_kfc import transform_store_data

# 상수
URL = "https://www.kfckorea.com/store/findStore"
JSON_FILE = "kfc.json"

# selenium으로 kfc 전국 매장 정보 크롤링
def fetch_store_data():
    kfc_list = []

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get(URL)
        time.sleep(5)

        # 지역검색 탭 클릭
        region_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "지역검색")))
        region_btn.click()
        time.sleep(2)

        sido_el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[select-box]")))
        sido_list = [opt.text for opt in Select(sido_el).options if "시,도" not in opt.text]

        for sido in sido_list:
            # 시,도 선택
            sido_select = driver.find_element(By.CSS_SELECTOR, "select[select-box]")
            driver.execute_script("arguments[0].click();", sido_select)
            time.sleep(1)
            driver.find_element(By.XPATH, f"//select[@select-box]//option[text()='{sido}']").click()
            time.sleep(2)

            gugun_el = driver.find_element(By.CLASS_NAME, "town")
            gugun_list = [opt.text for opt in Select(gugun_el).options if "구,군" not in opt.text]

            for sigungu in gugun_list:
                # 구,군 선택
                town_select = driver.find_element(By.CLASS_NAME, "town")
                driver.execute_script("arguments[0].click();", town_select)
                time.sleep(1)
                driver.find_element(By.XPATH, f"//select[contains(@class, 'town')]//option[text()='{sigungu}']").click()
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

                        print(f"[{sido} {sigungu}] 매장: {store_name} | 위치: {road_addr} | 영업: {shop_hours}")

                        kfc_list.append({
                            "sido": sido,
                            "sigungu": sigungu,
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
        # driver.quit()  # 확인을 위해 브라우저를 열어두려면 주석 처리
        pass

    return kfc_list

# 데이터 -> json 파일 저장
def save_to_json(data, filepath):
    with open(filepath, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    raw_store_data = fetch_store_data()
    transformed_data = transform_store_data(raw_store_data)

    if transformed_data:
        save_to_json(transformed_data, JSON_FILE)
        print(f'[KFC] Data saved to {JSON_FILE}')
    else:
        print("수집된 데이터 X")


if __name__ == "__main__":
    main()
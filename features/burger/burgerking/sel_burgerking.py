from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json
from geopy.geocoders import Nominatim



### 문자열 주소를 좌표로
geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
def geocoding(address):
    geo = geolocoder.geocode(address)
    lat = str(geo.latitude) if geo else ""
    lng = str(geo.longitude) if geo else ""
    return {"lat": lat, "lng": lng}

### 함수로 묶기
path = "chromedriver.exe"
options = Options()
options.add_argument("--headless")
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.burgerking.co.kr/store/all"
driver.get(url)
sleep_time = 1
time.sleep(sleep_time)


### 더보기 버튼 클릭
# body = driver.find_element(by=By.CSS_SELECTOR, value="body")
#     body.send_keys(Keys.END)
for _ in range (0, 14) :
    btn_more = driver.find_element(by=By.CSS_SELECTOR, value="button.btn_more02")
    btn_more.click()
    time.sleep(sleep_time)


### 매장 데이터 수집
burgerking_list = []
store_list = driver.find_elements(by=By.CSS_SELECTOR, value="ul.store_list li")
for item in store_list :
    store_name = item.find_element(by=By.CSS_SELECTOR, value="div.tit_store span").text # 사업장명
    store_status = "영업"# 영업상태명
    store_status_detail = "영업 중" # 상세영업상태명
    addr_full = item.find_element(by=By.CSS_SELECTOR, value="p.txt_addr span").text # 도로명주소
    addr_do = addr_full.split()[0] # 시도명 / 개방자치단체명
    addr_si = addr_full.split()[1] # 시군구명
    addr_old = "" # 지번주소
    crd = geocoding(addr_full)
    lat = crd['lat'] # 좌표정보(X) 
    lng = crd['lng'] # 좌표정보(Y)
    burgerking_item = {
        "store_name": store_name,
        "store_status": store_status,
        "store_status_detail": store_status_detail,
        "addr_full": addr_full,
        "addr_do": addr_do,
        "addr_si": addr_si,
        "addr_old": addr_old,
        "lat": lat,
        "lng": lng,
    }
    burgerking_list.append(burgerking_item)
    print(burgerking_item["store_name"], burgerking_item["addr_full"], burgerking_item["addr_do"], burgerking_item["addr_si"], burgerking_item["lat"], burgerking_item["lng"])


### data
# 사업장명
# 영업상태명
# 상세영업상태명
# 시도명 / 개방자치단체명
# 시군구명
# 도로명주소
# 지번주소
# 좌표정보(X) 
# 좌표정보(Y)


### 끝내기
driver.quit()


with open("burgerking.json","w",encoding="utf-8") as f :
    json.dump(burgerking_list, f, ensure_ascii=False, indent=4)
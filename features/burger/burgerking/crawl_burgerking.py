from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json
from geopy.geocoders import Nominatim


### 상수 선언
GEO_CODER = Nominatim(user_agent = 'South Korea', timeout=None)
DRIVER_PATH = "chromedriver.exe"
CRAWLING_URL = "https://www.burgerking.co.kr/store/all"
SLEEP_TIME = 1


### 문자열 주소를 좌표로 변환
def convert_coord(address):
    geo = GEO_CODER.geocode(address)
    lat = str(geo.latitude) if geo else ""
    lng = str(geo.longitude) if geo else ""
    return {"lat": lat, "lng": lng}

### selenium chrome driver 생성
def make_driver():
    options = Options()
    options.add_argument("--headless")
    service = webdriver.chrome.service.Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


### 스크롤 가장 아래까지 탐색
def scroll_down(driver) :
    max_scroll = 14
    for _ in range (0, max_scroll) :
        ### 더보기 버튼 선택
        btn_more = driver.find_element(by=By.CSS_SELECTOR, value="button.btn_more02")
        ### 더보기 버튼 클릭
        btn_more.click()
        ### 추가 데이터 로드까지 대기
        time.sleep(SLEEP_TIME)
        ### 화면 맨 아래로 이동
        # body = driver.find_element(by=By.CSS_SELECTOR, value="body")
        #     body.send_keys(Keys.END)


### burgerking 아이템에 좌표 정보 넣기
def put_coord(item):
    coord = convert_coord(item['addr_full'])
    item['lat'] = coord['lat'] # 좌표정보(X) 
    item['lng'] = coord['lng'] # 좌표정보(Y)


### 매장 데이터 수집
def extract_store(driver) :
    ### 스크롤 내리기
    scroll_down(driver)
    burgerking_list = [] # 저장할 데이터
    store_list = driver.find_elements(by=By.CSS_SELECTOR, value="ul.store_list li") # list container 요소 선택
    for item in store_list :
        store_name = item.find_element(by=By.CSS_SELECTOR, value="div.tit_store span").text # 사업장명
        store_status = "영업"# 영업상태명
        store_status_detail = "영업 중" # 상세영업상태명
        addr_full = item.find_element(by=By.CSS_SELECTOR, value="p.txt_addr span").text # 도로명주소
        sido = addr_full.split()[0] # 시도명 / 개방자치단체명
        sigungu = addr_full.split()[1] # 시군구명
        addr_old = "" # 지번주소
        burgerking_item = {
            "store_name": store_name,
            "store_status": store_status,
            "store_status_detail": store_status_detail,
            "addr_full": addr_full,
            "sido": sido,
            "sigungu": sigungu,
            "addr_old": addr_old,
        }
        put_coord(burgerking_item)### burgerking 아이템에 좌표 정보 넣기
        burgerking_list.append(burgerking_item)
        print(burgerking_item["store_name"], burgerking_item["addr_full"], burgerking_item["sido"], burgerking_item["sigungu"], burgerking_item["lat"], burgerking_item["lng"])
    return burgerking_list


### python 데이터를 json 파일로 dump
def dump_to_json(dump_data, file_name) :
    with open(file_name,"w",encoding="utf-8") as f :
        json.dump(dump_data, f, ensure_ascii=False, indent=4)


### 크롤링 실행
def run_crawling() :
    ### chrome driver 생성
    driver = make_driver()
    ### 크롤링할 사이트 접속
    driver.get(CRAWLING_URL)
    time.sleep(SLEEP_TIME)
    ### 매장 정보 추출
    store_list = extract_store(driver)
    ### json 파일로 저장
    dump_to_json(store_list, "./data/burgerking.json")
    ### 끝내기
    driver.quit()


run_crawling()
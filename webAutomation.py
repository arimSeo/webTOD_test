from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# 1.웹 열
# dr = webdriver.Chrome() 
# wait = WebDriverWait(dr, 5)
# # dr.set_window_size(414, 800)
# dr.implicitly_wait(5)
# #

options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())  
#원하는 위치에 크롬드라이버설치파일 저장할경우 변경 ➡️ ChromeDriverManager(path="원하는 경로")

driver = webdriver.Chrome(service=service, options=options)

#html 봇으로 인식했는지 확인
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url ='https://map.naver.com/v5/'
html = requests.get(url, headers = headers).text
# print(html)


driver.implicitly_wait(10)
driver.get('https://map.naver.com/v5/')


#자동화 시작~~!!
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver.implicitly_wait(10)
print("대기끝1")
driver.implicitly_wait(40)

# act = ActionChains(driver)

#(네이버지도)식당 검색
# search_box = switch_to.frame(driver.find_element(By.CLASS_NAME, 'input_search.ng-pristine.ng-valid.ng-touched'))

   #id값은 계속 바뀜-크롤링방지??

wait = WebDriverWait(driver, 20)
try:
    search_box = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "input_search.ng-pristine.ng-valid.ng-touched"))
    ) #입력창이 뜰 때까지 대기
finally:
    pass


driver.implicitly_wait(10)
print("대기끝2")

search_box.send_keys("리츠다이너")
search_box.send_keys(Keys.RETURN) # 엔터 혹은 RETURN

print("검색완료")
driver.implicitly_wait(40)


##????검색창에 커서 눌러져있음. -> 그럴때 밑에 팝업화면 내 요소들을 못찾음!!!
#1. 주문하기 버튼으로 주문
order_btn = driver.find_element(By.XPATH, '/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div/div/input').click()
print("주문버튼 찾았다")
# ActionChains(driver).click(order_btn).perform()
order_btn.click()
print("주문버튼 눌렀다")

# /html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div/div/input
# //*[@id="app-root"]/div/div/div/div[2]/div[4]/div/span/a

#2. 


# #####chatGPT
# #주문할 메뉴를 선택하고 주문서 페이지로 이동합니다.
# menu = driver.find_element_by_xpath('//a[@class="name" and contains(text(),"' + menu1 + '")]')
# menu.click()

# menu = driver.find_element_by_xpath('//a[@class="name" and contains(text(),"' + menu2 + '")]')
# menu.click()

# order_button = driver.find_element_by_xpath('//button[@class="btn_order"]')
# order_button.click()

# time.sleep(1)


# # 주문 정보를 입력하고 결제를 진행합니다.

# order_name_box = driver.find_element_by_name('order_name')
# order_name_box.send_keys(order_name)

# order_phone_box = driver.find_element_by_name('order_phone')
# order_phone_box.send_keys(order_phone)

# order_email_box = driver.find_element_by_name('order_email')
# order_email_box.send_keys(order_email)

# order_button = driver.find_element_by_xpath('//button[@class="btn_payment"]')
# order_button.click()

# time.sleep(1)



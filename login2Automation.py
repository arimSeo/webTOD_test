################ 로그인 젤 처음에 먼저하고 시작 ################
####### 최종 성공 버전 코드파일 (login2Automation.py) #########

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())  
#원하는 위치에 크롬드라이버설치파일 저장할경우 변경 ➡️ ChromeDriverManager(path="원하는 경로")

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.naver.com')
driver.implicitly_wait(10)


#자동화 시작~~!!
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#######~~~~~로그인부터~~~~~######
###chatGPT
### 1) 대화로 아이디,비번 받기 -보안문제,,   2) terminal에서 입력하기?

# 1. 로그인 (캡챠우회 필요)
#pip3 install pyperclip
import pyperclip

user_id='아이디입력'
user_pw='비밀번호입력'

#0)'NAVER로그인' 버튼 클릭
driver.find_element(By.CLASS_NAME, 'link_login').click()

#1) id 복사 붙여넣기
elem_id = driver.find_element(By.ID, 'id')
elem_id.click()
pyperclip.copy(user_id)
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(
        Keys.CONTROL).perform()
# elem_id.send_keys(Keys.COMMAND, 'v')  #ctrl+v (맥OS는 Keys.COMMAND)

print("아이디 완")
time.sleep(1)

#2) pw 복사 붙여넣기
elem_pw = driver.find_element(By.ID,'pw')
elem_pw.click()
pyperclip.copy(user_pw)
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(
        Keys.CONTROL).perform()
# elem_pw.send_keys(Keys.COMMAND, 'v')   #ctrl+v

print("비번 완")
time.sleep(1)

#3) 로그인 버튼 클릭
wait = WebDriverWait(driver, 10)
login = wait.until(EC.element_to_be_clickable((By.ID, "log.login"))).click()
# driver.find_element(By.ID, 'log.login').click()
print("로그인 완")


#2. 새로운 브라우저(기기)등록
driver.find_element(By.ID, 'new.save').click()


###################

#3. (네이버포탈) 식당명 검색
search_box = driver.find_element(By.CLASS_NAME, 'input_text')

driver.implicitly_wait(10)
print("대기끝2")

### chatGPT 
###가게명 입력하도록!!!!! 변경 /  키보드입력: ActionChains(driver).send_keys(keys) 
search_box.send_keys("리츠다이너")  # c1)리츠다이너  c2)치타샌드위치 정자본점 / c3)루트스테이
search_box.send_keys(Keys.RETURN) # 엔터 혹은 RETURN
print("검색완료")
driver.implicitly_wait(10)


#4. 주문하기 버튼 클릭
# /html/body/div[3]/div[2]/div/div[1]/div[2]/div[3]/section/div/div[1]/div[5]/div/span/a   *리츠다이너 주문 (로그인시!! 맛집저장 때문에 경로 달라짐)
order_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[2]/div[3]/section/div/div[1]/div[4]/div/span/a') #리츠다이너
# order_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[2]/div[3]/div/section/div/div[2]/div[3]/div/span/a') #루트스테이

print("주문버튼 찾았다")
order_btn.click()
print("주문버튼 눌렀다")
driver.implicitly_wait(20)

## 탭 전환 필요
# print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
print('탭전환')

#######################

###chatGPT
###user의 주문을 챗으로 받아서 web에 입력값으로 전송
### 1.바로 메뉴 선택하는 경우   2.메뉴상세보기 후에 선택하는경우(현재상태)  ++2개이상 메뉴담을때


#여기서부터 iframe 하위태그로 들어있음
###########

#2. 주문하기 버튼 >> 메뉴선택 이전
# 2-1) 포장/매장 선택 팝업 뜨는 경우

#iframe
iframe = driver.find_element(By.XPATH, '//*[@id="entryIframe"]')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[2]/a[1]/div/i').click()  #포장하기 버튼

driver.execute_script("location.reload(true);")   #새로고침
print("포장선택버튼 눌렀다")
driver.implicitly_wait(20)



#3. 메뉴선택
## driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/ul/li[1]/div/a[1]').click()   #메뉴선택1
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/ul/li[3]/div/a[1]').click()    #메뉴선택2

# driver.execute_script("location.reload(true);")  #새로고침
print("메뉴 하나 눌러")
driver.implicitly_wait(10)


#메뉴담기 버튼
# 화면 창 크기를 조절하여 화면에 안보이는 버튼 보이게
element = driver.find_element(By.TAG_NAME , "body")
driver.set_window_size(1200, 2200)
print("화면크기조절")

food = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[2]/a').click()  #장바구니
print("장바구니담기")

#최종 주문하기 버튼
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[2]/div/div/a').click()  #최종 주문하기
print("주문해!!")

driver.switch_to.default_content()    #iframe 탈출
# driver.implicitly_wait(30)
time.sleep(5)



#############################

#iframe 재입장
iframe = driver.find_element(By.XPATH, '//*[@id="entryIframe"]')
driver.switch_to.frame(iframe)
# driver.implicitly_wait(10)

#6. 주문서 >> 최종 주문버튼 클릭
req_message = driver.find_element(By.ID, 'message')
req_message.send_keys("파이팅TOD해야지!")
driver.implicitly_wait(5)

driver.find_element(By.CLASS_NAME, 'button_pay').click()   #이거 누르면 네이버페이로감
# driver.switch_to.default_content()    #iframe 탈출

print('쫜쨘쨘 성공')


# print("다와간다..이럴수가 브레잌타임되따 또,,,")



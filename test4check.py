########## html 정보 출력
print(browser.page_source)

########### 현재 창닫기
# close()는 현재 selenium webdriver가 활성화되어 있는 화면만을 종료합니다.
# 2개 이상의 webdriver 탭이 열려있다면 현재 활성화되어 있는 webdriver만 종료되고 나머지 webdriver는 종료되지 않습니다.


########### 스크롤
# JavaScript를 사용하여 스크롤을 내립니다.
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 스크롤을 내린 후, HTML 요소를 찾습니다.
element = driver.find_element_by_id("example-id")


############ 화면크기조절
# 화면 창 크기를 조절하여 모든 요소를 보이게 합니다.
element = driver.find_element_by_tag_name("body")
# driver.set_window_size(1024, element.size["height"])  #높이만
# driver.set_window_size(700, 300)  #weight, height 둘다
driver.minimize_window()
# HTML 요소를 찾습니다.
element = driver.find_element_by_id("example-id")


###########
# html 봇으로 인식했는지 확인
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url ='https://www.naver.com'
html = requests.get(url, headers = headers).text
print(html)

###########
#터미널에서 입력
# driver.find_element(By.ID, 'id').click()
# word = input("아이디를 입력하세요 : ")
# word = str(word)


# ###########1) 검색창에 커서때문에 안되는건가???
# # 캐시를 지우는 새로고침 (이거 해야지 '내위치버튼'으로 검색창커서out가능)
# #앞에창 새로고침함.. ->핸들러 새창으로 이동해서 새로고침하는 코드
new_window_handle = driver.window_handles[-1]
driver.switch_to.window(new_window_handle)
driver.execute_script("location.reload(true);")   
print("캐시지웠닭!") 

driver.implicitly_wait(20)

# #'캐시지우기 새로고침'해도 계속 검색창 커서 뜸 -> 다른 영향없는 버튼 눌러서 커서 아웃시키자
driver.find_element(By.XPATH,'/html/body/app/layout/div[3]/div[2]/div[1]/maps-controller/dynamic-content-outlet[1]/control-widget/control-bottom-widget-holder/div/control-location/button').click() 
print("내위치 버튼 눌러서 검색창 커서 아웃")  #검색창 커서 아웃(o)
driver.implicitly_wait(20)
# ##############


###########
# ## XXXXX - <canvas> 덮여있어서 안되나????

# # # 파이썬 파일내에서 JavaScript 코드 실행
# # driver.execute_script("""
# # var canvas = document.querySelector("#baseMap > div:nth-child(1) > div > div.mapboxgl-canvas-container.mapboxgl-interactive > canvas");
# # var ctx = canvas.getContext("2d");
# # """)
# # print("jsjsjsjsjs")  *성공


# # canvas 요소 찾기
# canvas = driver.find_element(By.CLASS_NAME, 'mapboxgl-canvas')

# # canvas 요소 내부에서 클릭할 좌표를 계산
# # (x, y) 좌표는 canvas의 왼쪽 상단 모서리를 기준으로 합니다.
# # x = 100
# # y = 100

# # # ActionChains를 사용하여 좌표를 클릭
# # action = ActionChains(driver)
# # action.move_to_element_with_offset(canvas, x, y)
# # action.click()
# # action.perform()

# # # JavaScript를 사용하여 canvas 요소 내부에서 좌표를 클릭
# # # driver.execute_script("var canvas = arguments[0]; var x = arguments[1]; var y = arguments[2]; var evt = new MouseEvent('click', { bubbles: true, cancelable: true, view: window, clientX: x, clientY: y }); canvas.dispatchEvent(evt);", canvas, x, y)


# # print("canvas 내부")
# # driver.implicitly_wait(20)

# # canvas 요소에서 포커스를 빼서 다른 요소에 접근할 수 있도록 함
# # driver.switch_to.default_content() #상위로 빠져나옴
# # print("canvas 나가")
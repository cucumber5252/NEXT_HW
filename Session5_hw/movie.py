from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'C:/Users/kdhyeok/Desktop/NEXT_hw/Session5/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (영화 차트)
driver.get("https://movie.naver.com/")

# 엑스 버튼 클릭
btn_1 = driver.find_element(By.XPATH, '//*[@id="noti_popup"]/div[1]/button')
btn_1.click()

# 랭킹 버튼 클릭
btn_2 = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
btn_2.click()


file=open('movie.csv', mode='w', newline='')
writer=csv.writer(file)
writer.writerow(["rank","title","singer"])


rank_list = list(range(2, 12)) + list(range(13, 19)) + list(range(20,22))

for i in rank_list:
    rank_btn = driver.find_element(By.XPATH,f'//*[@id="old_content"]/table/tbody/tr[{i}]/td[2]/div/a')
    rank_btn.click()

    outline = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
    director = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    
    find_grade = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[2]/em').text
    
    grade = ''

    if find_grade == "상영중":
        for i in range(1,5):
            grade += driver.find_element(By.XPATH,f'//*[@id="actualPointPersentBasic"]/div/em[{i}]').text
    else:
        grade = "개봉예정작이라 평점이 없음"

    
    print(outline, director, grade)
    writer.writerow([outline, director, grade])
    
    btn_3 = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
    btn_3.click()
    time.sleep(1)

file.close()

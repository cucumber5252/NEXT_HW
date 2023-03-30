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

# 검색하기
best_movie = "기생충"
btn_2 = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
btn_2.send_keys(best_movie)

btn_3 = driver.find_element(By.XPATH, '//*[@id="jSearchArea"]/div/button')
btn_3.click()

btn_4 = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li[1]/dl/dt/a')
btn_4.click()



#파일 오픈
file=open('movie2.csv', mode='w', newline='')
writer=csv.writer(file)
writer.writerow(["제목","감독","평점","리뷰 개수"])

title = best_movie

director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

rating = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text

comments = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/span/em').text

writer.writerow([title, director, rating, comments])

file.close()

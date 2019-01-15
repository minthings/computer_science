from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as b
import time

path = "C:/crawling/chromedriver.exe"

#조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다.
driver = webdriver.Chrome(path)

#webdriver가 google 페이지에 접속하도록 명령
driver.get('주소')

id = driver.find_element_by_id("아이디 입력 id")
pw = driver.find_element_by_id("password 입력 id")

id.send_keys("id key")
pw.send_keys("password key")


pw.send_keys(Keys.ENTER)
time.sleep(5)


b.encoding = 'utf-8'
read = driver.page_source
soup=b(read, "html.parser")
titles = soup.select(".container_name")
print(titles)
#print(soup.text)

#do something useful
#prints all the links with corresponding text


'''
information_list = soup.select("#intro_container_id")
for information in information_list:
	print(information.text)
'''
driver.close()

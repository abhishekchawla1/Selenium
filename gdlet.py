from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options=Options()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
driver.get('https://blog.gdeltproject.org/generative-ai-experiments-summarizing-a-day-of-global-climate-change-headlines-using-gdelt-gpt-4o-gemini-pro-gemini-flash/')

title_element=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div/div[1]/div/div[2]/article/header/h1/a')
title=title_element.text
print(title)

date_element=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div/div[1]/div/div[2]/article/header/div/span')
date=date_element.text
print(date)

elements=driver.find_elements(By.CSS_SELECTOR,'p,blockquote')
blog_content=''
for element in elements:
    blog_content=blog_content+element.text+'\n'

print(blog_content)

filename='blog.txt'
with open(filename,'w',encoding='utf-8') as file:
    file.write(blog_content)

driver.quit()





/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[9] 3
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[10] 4
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[10]
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[10]
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[10]
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[10]
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[10] 10
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[10]11
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[10] 13
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[10] 14
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[11] 15
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[11] 16
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[11] 20
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[11] 24
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[12] 25
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[12] 34
/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/nav/div/a[13] 35


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options=Options()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.maximize_window()
driver.get('https://www.analyticsvidhya.com/')

driver.find_element(By.XPATH,'/html/body/div/main/section[1]/div/div/div/button').click()
driver.find_element(By.XPATH,'/html/body/div/main/div[3]/div/div/div[2]/button[2]').click()

email='****'
email_element=driver.find_element(By.XPATH,'/html/body/div/main/div[4]/div/div/div[2]/div[2]/input')
email_element.send_keys(email)

driver.find_element(By.XPATH,'/html/body/div/main/div[4]/div/div/div[3]/button').click()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options=Options()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()

driver.get('https://www.flipkart.com/wearable-smart-devices/smart-watches/pr?sid=ajy,buh')

watch_name_element=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[1]')
watch_name=watch_name_element.text

watch_price_element=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div/div[1]')
watch_price=watch_price_element.text

mrp_price_element=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div/div[2]')
mrp=mrp_price_element.text

discount_element=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div/div[3]/span')
discount=discount_element.text

print(watch_name)
print(watch_price)
print(mrp)
print(discount)
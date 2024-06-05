from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options=Options()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.maximize_window()
driver.get('https://www.flipkart.com/wearable-smart-devices/smart-watches/pr?sid=ajy,buh')

c=1
for i in range(2,12):
    for j in range(1,5):
        try:
            watch_name_element=driver.find_element(By.XPATH,f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[1]')
            watch_name=watch_name_element.text
        except:
            watch_name=''

        try:
            watch_price_element=driver.find_element(By.XPATH,f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[1]')
            watch_price=watch_price_element.text
        except:
            watch_price=''

        try:
            description_element=driver.find_element(By.XPATH,f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/div[1]')
            description=description_element.text
        except:
            description_element=''

        try:
            mrp_element=driver.find_element(By.XPATH,f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[2]')
            mrp=mrp_element.text
        except:
            mrp=''

        try:
            discount_element=driver.find_element(By.XPATH,f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[3]/span')
            discount=discount_element.text
        except:
            discount=''

        print(f'S.No: {c}')
        print('--------------')
        print(f'Watch Name: {watch_name}')
        print(f'Watch Description: {description}')
        print(f'Price: {watch_price}')
        print(f'MRP: {mrp}')
        print(f'Discount: {discount}')
        print('--------------')
        print('\n')
        c+=1











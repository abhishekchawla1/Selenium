from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options=Options()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()

driver.get('https://www.gdeltproject.org/')
driver.find_element(By.XPATH,'/html/body/div/header/div/div/ul/li[2]/a').click()

titles=[]
dates=[]
contents=[]

for i in range(1, 25):
    blog = driver.find_element(By.XPATH,
                               f'/html/body/div[2]/div/div[5]/div/div/div/div[3]/div/div/div[1]/div[{i}]/div[1]/a/img').click()

    try:
        title_element = driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div/div[4]/div/div[1]/div/div[2]/article/header/h1/a')
        title = title_element.text
    except:
        title = ''

    try:
        date_element = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div[4]/div/div[1]/div/div[2]/article/header/div/span')
        date = date_element.text
    except:
        date = ('')

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, 'p,blockquote')
        blog_content = ''
        for element in elements:
            blog_content = blog_content + element.text + '\n'
    except:
        blog_content = ''

    titles.append(title)
    dates.append(date)
    contents.append(blog_content)

    print(title)

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/nav/div/ul/li[1]/a').click()

for i in range(2,21):
    driver.get(f'https://blog.gdeltproject.org/page/{i}/')

    for j in range(1, 25):
        blog = driver.find_element(By.XPATH,
                                   f'/html/body/div[2]/div/div[4]/div/div/div/div[2]/div/div/div[1]/div[{j}]/div[1]/a/img').click()

        try:
            title_element = driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div/div[4]/div/div[1]/div/div[2]/article/header/h1/a')
            title = title_element.text
        except:
            title = ''

        try:
            date_element = driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div/div[4]/div/div[1]/div/div[2]/article/header/div/span')
            date = date_element.text
        except:
            date = ('')

        try:
            elements = driver.find_elements(By.CSS_SELECTOR, 'p,blockquote')
            blog_content = ''
            for element in elements:
                blog_content = blog_content + element.text + '\n'
        except:
            blog_content = ''

        titles.append(title)
        dates.append(date)
        contents.append(blog_content)

        print(title)

        driver.get(f'https://blog.gdeltproject.org/page/{i}/')


data={'Title':titles,'Date':dates,'Blog':contents}
print(len(titles))

import pandas as pd
df=pd.DataFrame(data)
df.to_csv('GDLETblog.csv')



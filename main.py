from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


website = 'https://intake.steerhealth.io/doctor-search/aa1f8845b2eb62a957004eb491bb8ba70a'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(website)


button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="viewMore"]/button'))
)


button.click()


for _ in range(9):
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.END)
    time.sleep(2)


users = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "NewProviderCard__Wrapper-sc-12vowct-0.iysCTA"))
)
names=[]
links=[]
for user in users:
    link_name=user.find_element(By.XPATH,'.//a[@href]')
    name_element = user.find_element(By.XPATH, './/div[@class="inner"]/b')
    name_text = name_element.get_attribute("textContent")
    names.append(name_text)
    links.append(link_name.get_attribute('href'))
print(len(names))
title=[name.split(',')[-1].lstrip() for name in names]

expert = []
phone_number=[]
address=[]



for link in links:
    try:
        driver.get(link)

        try:
            user_detail = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@class="speciality"]/span | //div[@class="AboutCard__Tag-sc-1w30kh-1 fmQuPE"]'))
            )
            special = user_detail.text
            expert.append(special)
        except  Exception as e:
            expert.append("no data")

        try:
            phone = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,'//div[@style="display: flex;"]/span | //*[@id="__next"]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/div[3]/div/span'))
            )
            tel = phone.text
            phone_number.append(tel)

        except Exception as e:
            phone_number.append("no data")

        try:
            address1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div/div[1]/div[2]/div[3]/div/div[2]/h5 | //*[@id="__next"]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/span | //*[@id="__next"]/div/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/h5'))
            )
            address.append(address1.text)

        except Exception as e:
            address.append("no data")
    except Exception as e:
        pass


import pandas as pd


data = {'Name': names, 'Title': title, 'Expert': expert, 'Phone Number': phone_number, 'Address': address}
df = pd.DataFrame(data)


df.to_excel('providers_data.xlsx', index=False)


class Animal:
    def __init__(self,color,breed):
        self.color=color
        self.breed=breed

    def methods(self):
        pass

obj1=Animal("red","dog")
obj1.methods()




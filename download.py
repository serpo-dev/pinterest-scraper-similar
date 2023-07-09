import os
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By

err_cnt = 0
os.makedirs("./images", exist_ok=True)


with open("output_all.txt", "r") as file:
    lines = [line.strip() for line in file]

    driver = webdriver.Chrome()

    for index, line in enumerate(lines):
        try:
            driver.get(line)
            driver.implicitly_wait(0)
            img_url = (
                driver.find_element(By.XPATH, "//img[@class='hCL kVc L4E MIw']")
                .get_attribute("src")
                .replace("/564x/", "/originals/")
            )
           
            filepath = "./images/" + img_url.split("/")[-1]
            if not os.path.exists(filepath):
                urllib.request.urlretrieve(img_url, filepath)
           
        except:
            err_cnt += 1
        finally:
            print(str(index) + " / " + str(len(lines)) + " | " + str(err_cnt) + " errors")

    driver.close()
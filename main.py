import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


limit_per_page = int(input("Limit items per page [default: 100]:") or 100)
loops_count = int(input("Loops count [default: 3 (100 + 100^2 + 100^3 ~=~ 1M images )]:") or 3)

# start_search_input = input("Start search input [default: 'аниме ирл']: ") or "аниме ирл"
# start_search_url = "https://ru.pinterest.com/search/pins/?q=" + "%20".join(start_search_input.split(" ")) + "&rs=typed"
start_search_url = str(input("Enter a link to the pin that will be the starting point for searching for similar images [default: https://ru.pinterest.com/pin/2d--44895327524408511/]: ") or "https://ru.pinterest.com/pin/2d--44895327524408511/")

url = "https://ru.pinterest.com/pin/142637513191543994/"

driver = webdriver.Chrome()

error_counter = 0
counter = 0

def get_similar_urls( url: str, limit: int, driver):
    global counter, error_counter
    counter += 1

    links = []

    try:
        driver.get(url)

        while len(links) <= limit:
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[@aria-label][@href]"))
            )
            
            def get_attribute_safety(element, attribute_name):
                try:
                    attribute_value = element.get_attribute(attribute_name)
                except StaleElementReferenceException:
                    attribute_value = None

                return attribute_value

            links += [get_attribute_safety(element=e, attribute_name="href") for e in elements]
            links = list(filter(None, links))

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(0.5)

        with open("output_all.txt", "a") as file:
            file.write("\n".join(links))
    except:
        error_counter += 1
    finally:
        return links

def recursion(urls, loop=0):
    if loop >= loops_count:
        return urls
    new_urls = []
    for u in urls:
        new_urls += get_similar_urls(url=u, limit=limit_per_page, driver=driver )
        print("URL list length is " + str(len(new_urls)) + ". Errors: " + str(error_counter) + " / " + str(counter) + ".")
    return recursion(urls=new_urls, loop=loop + 1)

urls = recursion([start_search_url])
with open("output.txt", "a") as file:
    file.write("\n".join(urls))

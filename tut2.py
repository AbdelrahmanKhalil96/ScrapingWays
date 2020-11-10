from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "E:\Sel\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://techwithtim.net")
# driver.close()
link = driver.find_element_by_link_text("Python Programming")
link.click()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "sow-button-19310003"))
    )
    element.click()
    time.sleep(10)
    driver.back()
    driver.back()
    time.sleep(10)
finally:
    driver.quit()

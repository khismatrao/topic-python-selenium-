from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\Ishwari.Khismatrao\PycharmProjects\demo1\practice\browserdriver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get(r"https://www.amazon.in/")
login_element = driver.find_element_by_name(By.ID ,'nav-link-accountList-nav-line-1')
action_chains= ActionChains(driver)
action_chains.move_to_element(login_element).perform()
time.sleep(4)
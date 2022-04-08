from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\Ishwari.Khismatrao\PycharmProjects\demo1\practice\browserdriver\chromedriver.exe")
driver.maximize_window()
# driver.implicitly_wait(10)

driver.get(r"https://jqueryui.com/resources/demos/droppable/default.html")

drag = driver.find_element(By.ID, 'draggable')
drop = driver.find_element(By.ID, 'droppable')

action_chains = ActionChains(driver)
# action_chains.drag_and_drop(drag, drop).perform()

action_chains.click_and_hold(drag).move_to_element(drop).release().perform()

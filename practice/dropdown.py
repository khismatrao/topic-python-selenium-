

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"C:\Users\Ishwari.Khismatrao\PycharmProjects\demo1\practice\browserdriver\chromedriver.exe")
driver.maximize_window()
driver.get(r"https://demo.guru99.com/test/newtours/register.php")


element = driver.find_element_by_name("country")
drp = Select(element)
drp.select_by_visible_text('ANGOLA')
time.sleep(3)
drp.select_by_value('ALGERIA')
time.sleep(5)
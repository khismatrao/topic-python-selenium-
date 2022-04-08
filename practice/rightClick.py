from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\Ishwari.Khismatrao\PycharmProjects\demo1\practice\browserdriver\chromedriver.exe")
driver.maximize_window()
# driver.implicitly_wait(10)

driver.get(r"https://swisnl.github.io/jQuery-contextMenu/demo.html")
right_clickElements = driver.find_element(By.XPATH, "//span[text()='right click me']")
action_elements = ActionChains(driver)
action_elements.context_click(right_clickElements).perform()

right_click_options = driver.find_elements(By.CSS_SELECTOR , "li.context-menu-icon span")
for elements in right_click_options:
    print(elements.text)

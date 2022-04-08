from selenium import webdriver
# from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(r"C:\Users\Ishwari.Khismatrao\PycharmProjects\demo1\practice\browserdriver\chromedriver.exe")
driver.maximize_window()
driver.get(r"https://www.zomato.com/")

# For register
time.sleep(3)

driver.find_element_by_xpath("//li[@class='sc-3o0n99-4 kAUthO'][3]").click()
time.sleep(3)
driver.find_element_by_xpath("//section[@class='sc-1yzxt5f-6 bfympp'][1]").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@class='sc-MYvYT ezFTzD']").send_keys("Ishwari Khismatrao")

time.sleep(4)
#driver.find_element_by_link_text("Full Name").send_keys("ishwari khismtaro")
# @id='id-87']/section[2]/section/div[1]/section/section/input").send_keys("Ishwari khismtaro")

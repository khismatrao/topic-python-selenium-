from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\Ishwari.Khismatrao\PycharmProjects\demo1\practice\browserdriver\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.goibibo.com/")
driver.find_element_by_link_text("Flights").click()


time.sleep(2)
driver.find_element_by_css_selector(".sc-GEbAx.kenSRj").click()
time.sleep(2)


driver.find_element_by_css_selector(".sc-iJKOTD.iipKRx.fswWidgetPlaceholder").click()

time.sleep(2)


driver.find_element_by_xpath("//input[@type='text']").send_keys("Mumbai")
time.sleep(2)

driver.find_element_by_xpath("//div[@class='sc-iAKWXU iyyKqe'][1]").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@type='text']").send_keys("pune")
time.sleep(2)

driver.find_element_by_xpath("//div[@class='sc-iAKWXU iyyKqe'][1]").click()
time.sleep(3)


allDates = driver.find_elements_by_xpath("//div[@class='DayPicker-Month']//p")

for element in allDates:

      date = element.text
      print(date)
      if date == "11":
             element.click()
             break

time.sleep(4)
#driver.find_element_by_xpath("//div[@class='gr_fswFld']").click()
#driver.find_element_by_xpath("//div[@aria-label='Thu May 12 2022").click()

#driver.find_element_by_xpath("//p[@class='gr_fswFld__info']").click()
driver.find_element_by_xpath("//span[@class='fswTrvl__done").click()
#time.sleep(3)

#driver.find_element_by_xpath("//div[@class='sc-jJoQJp iPfLQ'][4]']").click()


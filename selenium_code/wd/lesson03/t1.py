
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson03/abc.html')

driver.switch_to.parent_frame()

print(driver.find_element_by_tag_name('p').text)

# raw_input('press any key to quit...')
driver.quit()
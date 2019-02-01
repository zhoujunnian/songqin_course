from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = r"d:\Program Files (x86)\360se6\Application\360se.exe"
browser = webdriver.Chrome(chrome_options=chromeOptions)

browser.get('http://www.baidu.com')
raw_input('press to exit')
browser.quit()
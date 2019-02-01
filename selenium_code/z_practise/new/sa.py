from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://mail.qq.com/cgi-bin/loginpage?autologin=n&errtype=1&clientuin=747593101&param=&sp=&tfcont=22%20serialization%3A%3Aarchive%205%200%200%204%200%200%200%208%20authtype%201%204%209%20clientuin%209%20747593101%206%20domain%206%20qq.com%202%20vm%203%20wsk&r=68888f71e4066748f0c2b048a4e5680f')

driver.switch_to.frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('xxxx')
driver.find_element_by_id('p').send_keys('xxxx')

time.sleep(1)
driver.find_element_by_id('login_button').click()


beforeTime = time.time()
while True:
    text = driver.find_element_by_id('err_m').text
    if text:
         break
    currentTime = time.time()
    if currentTime-beforeTime > 10:
        break

print("err:%s" % text)

input()
driver.quit()

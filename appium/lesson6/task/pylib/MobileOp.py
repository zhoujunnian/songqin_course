# coding:utf8
from appium import webdriver
from cfg import desired_caps

class MobileOp:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    shared_wd = None


    def createSession(self):

        MobileOp.shared_wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        MobileOp.shared_wd.implicitly_wait(10)



    def closeSession(self):
        MobileOp.shared_wd.quit()


    def openFirstArticle(self):
        code = u'new UiSelector().resourceId("io.manong.developerdaily:id/tv_title").instance(0)'

        ele1 = MobileOp.shared_wd.find_element_by_android_uiautomator(code)

        text1 = ele1.text
        print text1

        ele1.click()
        return text1

    def getOpenedArticleTitle(self):
        ele2 = MobileOp.shared_wd.find_element_by_id('io.manong.developerdaily:id/tv_title')
        text2 = ele2.text
        return text2

    #  key is : back, home
    def pressKey(self,key):
        keycode = None
        if key == 'back':
            keycode = 4
        elif key == 'home':
            keycode = 3

        MobileOp.shared_wd.press_keycode(keycode)

    def isInMainActivity(self):

        eles = MobileOp.shared_wd.find_elements_by_id('io.manong.developerdaily:id/tab_bar_plus')

        if eles:
            return  True
        else:
            return False
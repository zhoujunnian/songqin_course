# coding:utf8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from cfg import *
import time
from robot.api import logger
from pylib.WebOp import WebOp

class WebOpAdmin(WebOp):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'




    def loginWebSite(self,username,passwd):
        WebOp.shared_wd.get(MgrLoginUrl)

        WebOp.shared_wd.find_element_by_id('username').send_keys(username)
        WebOp.shared_wd.find_element_by_id('password').send_keys(passwd)
    
        WebOp.shared_wd.find_element_by_tag_name('button').click()


    def EnterTab(self,name):
        tabLinkCss =  u'ul.nav a[ui-sref={}]'.format(name)
        WebOp.shared_wd.find_element_by_css_selector(tabLinkCss).click()
        time.sleep(0.5)



    def DeleteAll(self,objName):
        self.EnterTab(objName)

        while True:
            delButtons = WebOp.shared_wd.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            WebOp.shared_wd.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(0.5)


    def  AddTeacher(self,realname,username,desc,idx,lesson):
        self.EnterTab('teacher')

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addEditData.realname']")
        ele.clear()
        ele.send_keys(realname)

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(username)

        ele = WebOp.shared_wd.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(WebOp.shared_wd.find_element_by_css_selector('select[ng-model*=courseSelected]'))
        select.select_by_visible_text(lesson)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)


    def  AddTraining(self,name,desc,idx,course):
        self.EnterTab('training')

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addEditData.name']")
        ele.clear()
        ele.send_keys(name)


        ele = WebOp.shared_wd.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(WebOp.shared_wd.find_element_by_css_selector('select[ng-model*=courseSelected]'))
        select.select_by_visible_text(course)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)


    def  AddTrainingGrade(self,name,desc,idx,tranning):

        self.EnterTab('traininggrade')

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addEditData.name']")
        ele.clear()
        ele.send_keys(name)


        ele = WebOp.shared_wd.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(WebOp.shared_wd.find_element_by_css_selector('select[ng-model*=training_id]'))
        select.select_by_visible_text(tranning)


        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)


    def  AddStudent(self,realname,username,desc,training,tranninggrade):
        self.EnterTab("student")

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addEditData.realname']")
        ele.clear()
        ele.send_keys(realname)

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(username)

        ele = WebOp.shared_wd.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)



        select = Select(WebOp.shared_wd.find_element_by_css_selector('select[ng-model*="addEditData.training_id"]'))
        select.select_by_visible_text(training)
        select = Select(WebOp.shared_wd.find_element_by_css_selector('select[ng-model*="addEditData.traininggrade_id"]'))
        select.select_by_visible_text(tranninggrade)


        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)



    def  GetTeacherList(self):
        self.EnterTab('teacher')

        # 试试 //tr/td[2]/span/text()
        eles = WebOp.shared_wd.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]


    def GetStudentList(self):
        self.EnterTab('student')

        # 试试 //tr/td[2]/span/text()
        eles = WebOp.shared_wd.find_elements_by_css_selector('tr>td:nth-child(2)')
        for ele in eles:
            print ele.text

        return  [ele.text for ele in eles]



    def GetCourseList(self):
        self.EnterTab('course')

        # 试试 //tr/td[2]/span/text()
        eles = WebOp.shared_wd.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]


    def AddCourse(self, name,desc,idx):
        self.EnterTab('course')

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addData.name']")
        ele.clear()
        ele.send_keys(name)

        ele = WebOp.shared_wd.find_element_by_tag_name("textarea")
        ele.clear()
        ele.send_keys(desc)

        ele = WebOp.shared_wd.find_element_by_css_selector("input[ng-model='addData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)

    def AddLesson(self, name,desc):
        self.EnterTab('lesson')

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()


        select = Select(WebOp.shared_wd.find_element_by_css_selector('select[ng-model*="addEditData.course_id"]'))
        select.select_by_visible_text(name)



        ele = WebOp.shared_wd.find_element_by_tag_name("textarea")
        ele.clear()
        ele.send_keys(desc)



        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)

def test():
    wo = WebOpAdmin()
    # 打开浏览器，创建webdrier
    wo.setupWebTest()
    wo.loginWebSite('auto','sdfsdfsdf')

    wo.DeleteAll('student')
    wo.DeleteAll('traininggrade')
    wo.DeleteAll('training')
    wo.DeleteAll('teacher')
    wo.DeleteAll('course')

    wo.AddCourse(u'初中化学',u'...','3')
    wo.AddTraining(u'初中班','...','1',u'初中化学')
    wo.AddTrainingGrade(u'初中班1期','...','1',u'初中班')
    wo.AddStudent(u'关羽',u'guanyu','...',u'初中班',u'初中班1期')
    wo.GetStudentList()

    wo.DeleteAll('student')
    wo.DeleteAll('traininggrade')
    wo.DeleteAll('training')
    wo.DeleteAll('teacher')
    wo.DeleteAll('course')




if __name__ == '__main__':
    test()
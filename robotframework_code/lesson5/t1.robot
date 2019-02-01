*** Settings ***
Library  Selenium2Library
Library  st
Resource   rc1.robot



*** Test Cases ***
测试1
    [Setup]  DeleteAllCourse


    Login Web Site

    Add Course    初中数学    初中数学   1

    ${lessons}=  GetCourseList


    Should Be True   $lessons==[u'初中数学']

    Close Browser

    [Teardown]     DeleteAllCourse



测试2
    [Setup]  DeleteAllCourse


    Login Web Site

    addCourse    初中语文    初中语文   2

    ${lessons}=  GetCourseList

    Should Be True   $lessons==[u'初中语文']

    Close Browser

    [Teardown]     DeleteAllCourse
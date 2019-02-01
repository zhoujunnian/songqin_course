*** Settings ***
Library    Collections
Library    pylib.WebOpAdmin


*** Test Cases ***

添加课程
    [Setup]  DeleteAll    course

    addCourse    初中语文    初中语文   2

    ${lessons}=  GetCourseList

    Should Be True   $lessons==[u'初中语文']


    addCourse    初中数学    初中数学   1

    ${lessons}=  GetCourseList

    Should Be True   $lessons==[u'初中数学',u'初中语文']


    [Teardown]     DeleteAll   course
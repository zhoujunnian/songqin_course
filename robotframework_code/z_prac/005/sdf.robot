*** Settings ***
Library           Selenium2Library
Library           Collections
Resource          rc.robot
Suite Setup        Setup WebTest
Suite Teardown     TearDown WebTest

*** Test Cases ***
测试1
    [Setup]    DeleteAllLesson
    LoginWebsite      &{adminuser}[name]    &{adminuser}[pw]

    AddLesson         初中化学    初中化学描述    2
    ${lessons}=       GetLessonList
    Should Be True    $lessons==[u'初中化学']

    AddLesson         初中语文    初中语文描述    1
    ${lessons}=       GetLessonList
    Should Be True    $lessons==[u'初中语文',u'初中化学']


    [Teardown]    DeleteAllLesson



*** Settings ***
Library           Selenium2Library
Library           Collections
Library           st
Resource          rc.robot

*** Test Cases ***
测试1
    [Setup]    deleteAllLesson
    loginwebsite    auto    sdfsdfsdf
    addlesson    初中化学    初中化学描述    1
    ${lessons}=    GetLessonList
    Should Be True    $lessons==[u'初中化学']
    Close Browser
    [Teardown]    deletealllesson

测试2
    [Setup]    deleteAllLesson
    loginwebsite    auto    sdfsdfsdf
    addlesson    初中语文    初中语文描述    3
    ${lessons}=    GetLessonList
    Should Be True    $lessons==[u'初中语文']
    Close Browser
    [Teardown]    deletealllesson

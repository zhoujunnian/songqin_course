*** Settings ***
Library           SeleniumLibrary
Library           Collections

*** Test Cases ***
检查课程
    [Documentation]    检查课程是否包含 [selenium   java]
    Login    auto   sdfsdf

    ${lessons}=    get lessons


    ${expected}=    Create List    python语言   selenium
    Lists Should Be Equal   ${lessons}    ${expected}
    Should Be True    $lessons==$expected


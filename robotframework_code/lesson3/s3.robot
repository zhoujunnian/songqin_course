*** Settings ***
Library           SeleniumLibrary
Library           Collections

*** Test Cases ***
检查课程
    [Documentation]    检查课程是否包含 [selenium   java]
    Open Browser   http://localhost/mgr/login/login.html   chrome
    Set Selenium Implicit Wait    4

    Input Text    id=username    auto
    Input Text    id=password    sdfsdfsdf
    Click Element  tag=button
    Sleep   2

    #  这里面是包含webelement 的list
    ${eles}=    Get Webelements    css=tr>td:nth-child(2)


    ${lessons}=     Create List

    :FOR    ${ele}    IN    @{eles}
       \    Append To List   ${lessons}    ${ele.text}

    Log To Console   ${lessons}

    ${expected}=    Create List    selenium    java

    #Close Browser

    Lists Should Be Equal   ${lessons}    ${expected}
    Should Be True    $lessons==$expected


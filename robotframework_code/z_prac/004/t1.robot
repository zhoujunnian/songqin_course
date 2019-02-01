*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    st

*** Test Cases ***
测试1
    [Setup]     DeleteAllLesson
    Open Browser    http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   10

    Input Text   id=username    auto
    Input Text   id=password    sdfsdfsdf
    Click Element   tag=button


    Click Element   css=button[ng-click^=showAddOne]


    input text      css=input[ng-model='addData.name']    初中化学
    input text      css=textarea[ng-model='addData.desc']    初中化学描述
    input text      css=input[ng-model='addData.display_idx']    3

    Click Element   css=button[ng-click^=addOne]

    sleep   1

    ${eles}=    Get Webelements    css=tr>td:nth-child(2)

    ${lessons}=    create list
    :FOR   ${ele}   IN   @{eles}
       \   log to console    ${ele.text}
       \   Append To List   ${lessons}   ${ele.text}


    ${expected}=   create list   初中化学
    Lists Should Be Equal    ${expected}    ${lessons}

    Close Browser

    [Teardown]   Deletealllesson

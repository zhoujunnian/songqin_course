*** Settings ***
Library    Selenium2Library
Library    Collections




*** Keywords ***
Setup WebTest
    Open Browser   http://localhost    chrome
    Set Selenium Implicit Wait   10

TearDown WebTest
    Close Browser

DeleteAllLesson

    LoginWebsite   &{adminuser}[name]    &{adminuser}[pw]
    :For   ${one}  IN RANGE  9999
       \   ${html}=  Get Webelement  tag=html
       \   ${eles}=  Evaluate   $html.find_elements_by_css_selector("button[ng-click^='delOne']")
       \   Exit For Loop If   $eles==[]
       \   Click Element   @{eles}[0]
       \   Click Element   css=button.btn-primary
       \   sleep  1



LoginWebsite
    [Arguments]   ${username}    ${password}

    Go To    http://localhost/mgr/login/login.html

    Input Text   id=username    ${username}
    Input Text   id=password    ${password}
    Click Element   tag=button


    Click Element   css=button[ng-click^=showAddOne]


AddLesson
    [Arguments]   ${name}    ${desc}    ${idx}

    input text      css=input[ng-model='addData.name']    ${name}
    input text      css=textarea[ng-model='addData.desc']    ${desc}
    input text      css=input[ng-model='addData.display_idx']    ${idx}

    Click Element   css=button[ng-click^=addOne]

    sleep   1

GetLessonList

    ${eles}=    Get Webelements    css=tr>td:nth-child(2)

    ${lessons}=    create list
    :FOR   ${ele}   IN   @{eles}
       \   log to console    ${ele.text}
       \   Append To List   ${lessons}   ${ele.text}

    [Return]   ${lessons}
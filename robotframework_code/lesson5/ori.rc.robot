*** Settings ***
Library    Selenium2Library
Library    Collections




*** Keywords ***

loginWebsite
    [Arguments]   ${username}    ${password}

    Open Browser    http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   10

    Input Text   id=username    ${username}
    Input Text   id=password    ${password}
    Click Element   tag=button


    Click Element   css=button[ng-click^=showAddOne]


addLesson
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
*** Settings ***
Library    Selenium2Library
Library    Collections


*** Keywords ***
Login Web Site
    Open Browser   http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   10

    Input Text   id=username   auto
    Input Text   id=password   sdfsdfsdf
    Click Button    tag=button


Add Lesson
    [Arguments]     ${name}      ${desc}    ${displayidx}
    Click Element   css=button[ng-click^=showAddOne]

    input text      css=input[ng-model='addData.name']    ${name}
    input text      css=textarea[ng-model='addData.desc']    ${desc}
    input text      css=input[ng-model='addData.display_idx']    ${displayidx}

    Click Element   css=button[ng-click^=addOne]

    sleep  2


Get Course List

    ${lessons}=   Create List
    ${eles}=   get webelements  css=tr>td:nth-child(2)
    :FOR   ${ele}   IN   @{eles}
    \      Append To List   ${lessons}    ${ele.text}

    [Return]   ${lessons}


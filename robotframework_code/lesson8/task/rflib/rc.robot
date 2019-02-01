*** Settings ***
Library    SeleniumLibrary
Library    Collections
Variables  cfg.py


*** Keywords ***

Setup WebTest
    Open Browser   http://localhost    chrome
    Set Selenium Implicit Wait   10

Teardown WebTest
    Close Browser

Login Web Site
    Go To   ${MgrLoginUrl}

    Input Text   id=username   &{adminuser}[name]
    Input Text   id=password   &{adminuser}[pw]
    Click Button    tag=button


Add Course
    [Arguments]     ${name}      ${desc}    ${displayidx}

    Click Element   css=a[ui-sref='course']
    Sleep  1

    Click Element   css=button[ng-click^=showAddOne]

    input text      css=input[ng-model='addData.name']    ${name}
    input text      css=textarea[ng-model='addData.desc']    ${desc}
    input text      css=input[ng-model='addData.display_idx']    ${displayidx}

    Click Element   css=button[ng-click^=addOne]

    sleep  2


Get Course List

    Click Element   css=a[ui-sref='course']
    Sleep  1

    ${lessons}=   Create List
    ${eles}=   get webelements  css=tr>td:nth-child(2)
    :FOR   ${ele}   IN   @{eles}
    \      Append To List   ${lessons}    ${ele.text}

    [Return]   ${lessons}

DeleteAllCourse

    Click Element   css=a[ui-sref='course']
    Sleep  1

    Set Selenium Implicit Wait    2

    :For   ${one}    IN RANGE   9999
     \    ${eles}=   Get WebElements   css=button[ng-click^='delOne']
     \    exit for loop if    $eles==[]
     \    Click Element     @{eles}[0]
     \    Click Element     css=button.btn-primary
     \    Sleep   1


    Set Selenium Implicit Wait    10



Add Teacher
    [Arguments]     ${realname}    ${username}    ${desc}   ${idx}    ${course}


    Click Element   css=a[href='#/teacher']
    Sleep  1

    Click Element   css=button[ng-click^=showAddOne]

    input text      css=input[ng-model='addEditData.realname']    ${realname}
    input text      css=input[ng-model='addEditData.username']    ${username}
    input text      css=textarea[ng-model='addEditData.desc']         ${desc}
    input text      css=input[ng-model='addEditData.display_idx']     ${idx}

    Select From List By Label   css=select[ng-model*=courseSelected]  ${course}

    Click Element    css=button[ng-click*='addTeachCourse']

    Click Element   css=button[ng-click^=addOne]

    sleep  2


Get Teacher List

    Click Element   css=a[href='#/teacher']
    Sleep  1

    ${teachers}=   Create List
    ${eles}=   get webelements  css=tr>td:nth-child(2)
    :FOR   ${ele}   IN   @{eles}
    \      Append To List   ${teachers}    ${ele.text}

    [Return]   ${teachers}

DeleteAllTeacher

    Click Element   css=a[href='#/teacher']
    Sleep  1

    Set Selenium Implicit Wait    2

    :For   ${one}    IN RANGE   9999
     \    ${eles}=   Get WebElements   css=button[ng-click^='delOne']
     \    exit for loop if    $eles==[]
     \    Click Element     @{eles}[0]
     \    Click Element     css=button.btn-primary
     \    Sleep   1


    Set Selenium Implicit Wait    10

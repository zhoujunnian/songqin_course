*** Settings ***
Library    Selenium2Library
Library    Collections
Variables    cfg.py


*** Keywords ***

Setup WebTest
    Open Browser   http://localhost    chrome
    Set Selenium Implicit Wait   2

TearDown WebTest
    Close Browser


LoginWebSite
    [Arguments]    ${username}   ${password}
    Go To   ${MgrLoginUrl}

    Input Text   id=username    ${username}
    Input Text   id=password    ${password}
    Click Element   tag=button


DeleteAllTeacher


    Click Element   css=ul.nav a[href*=teacher]
    Sleep  1  # wait for teacher info displayed


    :For   ${one}  IN RANGE  20
       \   sleep  1
       \   ${html}=  Get Webelement  tag=html
       \   ${eles}=  Evaluate   $html.find_elements_by_css_selector("*[ng-click^='delOne']")

       \   Exit For Loop If   $eles==[]
       \   Click Element   @{eles}[0]
       \   Click Element   css=.modal-footer .btn-primary



DeleteAllCourse

    Click Element   css=ul.nav a[ui-sref=course]
    Sleep  1  # wait for Course info displayed

    :For   ${one}  IN RANGE  20
       \   sleep  1
       \   ${html}=  Get Webelement  tag=html
       \   ${eles}=  Evaluate   $html.find_elements_by_css_selector("*[ng-click^='delOne']")

       \   Exit For Loop If   $eles==[]
       \   Click Element   @{eles}[0]
       \   Click Element   css=.modal-footer .btn-primary





AddTeacher
    [Arguments]   ${realname}  ${username}   ${desc}    ${idx}  ${lesson}

    Log To Console   添加老师...

    Click Element   css=ul.nav a[href*=teacher]
    Sleep  1  # wait for lesson info displayed


    Click Element   css=button[ng-click^=showAddOne]

    input text      css=input[ng-model='addEditData.realname']    ${realname}
    input text      css=input[ng-model='addEditData.username']    ${username}
    input text      css=textarea[ng-model='addEditData.desc']    ${desc}
    input text      css=input[ng-model='addEditData.display_idx']    ${idx}

    Select From List By Label   css=select[ng-model*=courseSelected]    ${lesson}
    Click Element    css=button[ng-click*=addTeachCourse]

    Click Element   css=button[ng-click^=addOne]

    sleep   1


GetTeacherList

    Click Element   css=ul.nav a[href*=teacher]
    Sleep  1


    ${eles}=    Get Webelements    css=tr>td:nth-child(2)

    ${teachers}=    create list
    :FOR   ${ele}   IN   @{eles}
       \   log to console    ${ele.text}
       \   Append To List   ${teachers}   ${ele.text}

    [Return]   ${teachers}





AddCourse
    [Arguments]   ${name}    ${desc}    ${idx}
    Click Element   css=ul.nav a[ui-sref=course]
    Sleep  1  # wait for Course info displayed

    Click Element   css=button[ng-click^=showAddOne]

    Input Text  css=input[ng-model='addData.name']     ${name}
    Input Text  tag=textarea     ${desc}
    Input Text  css=input[ng-model='addData.display_idx']     ${idx}

    Click Element   css=button[ng-click^=addOne]

    sleep   1

GetCourseList

    Click Element   css=ul.nav a[ui-sref=course]
    Sleep  1  # wait for Course info displayed
    ${eles}=    Get Webelements    css=tr>td:nth-child(2)

    ${courses}=    create list
    :FOR   ${ele}   IN   @{eles}
       \   log to console    ${ele.text}
       \   Append To List   ${courses}   ${ele.text}

    [Return]   ${courses}
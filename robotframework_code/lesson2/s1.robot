*** Settings ***
Library           SeleniumLibrary    10    20
Library           Collections
Library           Dialogs



*** Test Cases ***
百度搜索1
    [Documentation]    测试百度搜索 松勤
    Open Browser    http://www.baidu.com    chrome
    Input Text    id=kw    松勤\n
    Set Selenium Implicit Wait    4
    ${firstRet}=    Get Text    css=div.result:first-of-type>h3
    Should Be Equal    ${firstRet}    松勤
    Close Browser

百度搜索2
    [Documentation]    测试百度搜索 松勤测试
    Open Browser    http://www.baidu.com    chrome
    Input Text    id=kw    松勤测试\n
    Set Selenium Implicit Wait    4
    ${firstRet}=    Get Text    css=div.result:first-of-type>h3
    Should Be Equal    ${firstRet}    松勤软件测试
    Close Browser

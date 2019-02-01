*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
搜索 python
    ${var}    set variable   hello
    Should Be Equal   ${var}   helle    变量不是hello    values=False

    Should Be Equal As Integers   10   010
    Should Be Equal   10    010

    ${var2}    convert to integer   10
    ${var3}    convert to number    10.3
    should be true  RF_VAR_var == 3


#    'hello'.startswith('he33')


#    Open Browser    http://www.baidu.com    chrome
#    Set Selenium Implicit Wait    3
#    Input Text    id=kw    Python\n
#    sleep  1
#    ${title}=    Get Title
#    Should Be Equal    ${title}    Python    标题和预期不同    values=False
#    Close Browser



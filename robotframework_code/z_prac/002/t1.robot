*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
#测试1
#    Open Browser    http://www.baidu.com/    chrome
#    Set Selenium Implicit Wait    5
#    Input Text    id=kw    北京时间\n
#    ${date}=    Get Text    css=.op-beijingtime-date
#    log to console   ${date}
#    Should Be True    $date.startswith('2017年')
#    Close Browser


测试2
    ${var1}   convert to integer   100
    ${var2}   set variable    5
    should be true  ($var1*int($var2)) == 500




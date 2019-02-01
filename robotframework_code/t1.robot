*** Settings ***
Library  SubLibrary

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
    ${var1}   evaluate  (1,2,3)
    Log To Console  @{var1}[0]




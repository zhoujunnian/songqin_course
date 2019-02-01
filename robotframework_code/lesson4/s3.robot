*** Settings ***
Library  mylib4

*** Test Cases ***
测试1
    ${html}=    getwebinfo
    run keyword if    '2016' in $html and 'UTC' in $html
    ...               log to console   \n2016年的,UTC时间
    ...   ELSE IF    '2016' in $html   log to console   \n2016年的
    ...   ELSE IF    'UTC' in $html    log to console   \nUTC时间
    ...   ELSE                         log to console   \n以上都不是
















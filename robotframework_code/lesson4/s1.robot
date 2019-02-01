*** Settings ***
Library  mylib4

*** Test Cases ***
测试1
    ${html}=    getwebinfo
    run keyword if    '2018' in $html and 'UTC' in $html
    ...               log to console   \n2018年的,UTC时间















*** Settings ***
Library           lib1    2    3

*** Test Cases ***
随便测试
    ${firstRet}    set variable    hellow world
    log to console    ${firstRet}
    Should Contain    ${firstRet}    hello

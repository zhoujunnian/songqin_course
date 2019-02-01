#*** Settings ***
#Library  mylib1



*** Test Cases ***
测试1
    ${var}    set variable   hello
#    Should Be Equal   ${var}   helle
    Should Be Equal   ${var}   helle    变量不是hello    values=False








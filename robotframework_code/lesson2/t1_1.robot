#*** Settings ***
#Library  mylib1



*** Test Cases ***
测试1
    ${var}    set variable   这是日志里面要记录的内容
    Log   ${var}








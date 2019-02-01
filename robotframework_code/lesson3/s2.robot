*** Settings ***
Library  OperatingSystem
Library  Collections

*** Test Cases ***
测试1111
    ${files}=   list files in directory  e:\
    log    ${files}
    Log List    ${files}
    set list value   ${files}   0   hello
    Log List    ${files}






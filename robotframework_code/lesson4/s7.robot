*** Settings ***
Library  Dialogs

*** Test Cases ***
测试1
    ${var1}=   Create List    Hello   world
    ${var2}=   Evaluate    ['Hello', 'world']

    Log To Console    ${var1}
    Log To Console    ${var2}















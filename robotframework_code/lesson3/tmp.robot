*** Settings ***
Library           Collections

*** Test Cases ***
Start and end用法
    [Documentation]  Loops over values from 1 to 10
    :FOR    ${index}    IN RANGE    1    11   2
    \    Log To Console    ${index}






















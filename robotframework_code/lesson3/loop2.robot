*** Settings ***
Library  mylib3

*** Test Cases ***

遍历list变量
    ${list}=     returnlist
    :FOR    ${index}    IN   @{list}
    \    Log To Console    ${index}




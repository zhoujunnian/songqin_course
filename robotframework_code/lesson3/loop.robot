*** Settings ***
Library  mylib3

*** Test Cases ***

Example 1
    :FOR    ${animal}  IN   猫   狗  猪
    \    Log To Console    ${animal}
    \    Log To Console    第二行
    Log To Console   循环外面

#step 用法
#    ${var}=   returndict
#    :FOR    ${index}    IN   ${var}
#    \    printarg    ${index}



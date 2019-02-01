*** Settings ***
Library  mylib3

*** Test Cases ***
测试
    ${var1}=     set variable   abc
    printarg  ${var1}

    ${var2}=     convert to integer   23
    printarg  ${var2}

    ${var2}=     convert to integer   23
    printarg  ${var2}    Hello





*** Settings ***
Library    tlib1

*** Test Cases ***
case1
    ${a}=       returnlist
    log to console    ${a}
    ${b}=       _returnlist2
    log to console    ${b}





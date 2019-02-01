*** Settings ***
Library    tlib2.SubLibrary

*** Test Cases ***
case1
    ${a}=       returnint
    log to console    ${a}
    ${b}=       _returnint2
    log to console    ${b}

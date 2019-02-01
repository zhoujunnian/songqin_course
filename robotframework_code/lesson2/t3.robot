#*** Settings ***
#Library  mylib1


*** Test Cases ***
验证
    ${num}=  convert to integer  20
    should be true    ${num}>19










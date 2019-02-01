*** Settings ***
Library  Dialogs


*** Test Cases ***
测试1
    ${weight}=   get value from user    请输入你的体重    60
    Log To Console   体重为${weight}
    run keyword if   int($weight)>60    log to console   太重了
















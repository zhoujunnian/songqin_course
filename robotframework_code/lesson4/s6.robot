*** Settings ***
Library  Dialogs

*** Test Cases ***
测试1
    :for   ${one}   in range   99999
       \   ${weight}=   get value from user    请输入你的体重    60
       \   run keyword if    $weight=='continue'   Continue For Loop
       \   run keyword if    $weight=='over'   Exit For Loop
       \   run keyword if    int($weight)>60   log to console   太重了       ELSE  log to console   太轻了















#*** Settings ***
#Library  mylib1


*** Test Cases ***
验证
    ${str1}=  set variable  hello
#    should be true   ${str1}==hello


    should be true   ${str1}=='hello'

    should be true   $str1=='hello'












#*** Settings ***
#Library  mylib1



*** Test Cases ***
测试1
#    Should Be Equal   10    010           #字符串对象比较，结果是False
    Should Be Equal As Integers  10  010  #转换成数字对象比较，结果是true









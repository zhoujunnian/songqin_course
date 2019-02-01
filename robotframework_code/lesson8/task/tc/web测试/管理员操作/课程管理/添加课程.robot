*** Settings ***
Library    SeleniumLibrary
Resource    rflib/rc.robot


*** Test Cases ***
测试1
    [Setup]  DeleteAllCourse



    Add Course    初中数学    初中数学   1

    ${lessons}=  Get Course List


    Should Be True   $lessons==['初中数学']


    [Teardown]     DeleteAllCourse



测试2
    [Setup]  DeleteAllCourse


    Add Course    初中语文    初中语文   2

    ${lessons}=  Get Course List

    Should Be True   $lessons==['初中语文']


    [Teardown]     DeleteAllCourse
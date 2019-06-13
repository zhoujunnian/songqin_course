*** Settings ***
Library    pylib.SchoolClassLib


*** Test Cases ***
添加班级1 - tc000001
    ${ret1}=    add school class    1     1班     60
    should be true     $ret1['retcode']==0

#列出班级，检验一下
    ${ret2}=    list school class    1
    ${fc}=   evaluate   $ret2['retlist'][0]
    should be true    $fc['id']==$ret1['id']
    should be true    $fc['invitecode']==$ret1['invitecode']

    [Teardown]    delete_school_class   &{ret1}[id]
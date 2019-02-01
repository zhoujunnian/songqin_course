*** Settings ***
Library    Collections
Library    pylib.WebOpAdmin


*** Test Cases ***

添加老师1
    [Setup]   Run Keywords   DeleteAll   course
    ...    AND  DeleteAll    teacher
    ...  AND   AddCourse   初中语文    初中语文描述    1
    ...  AND  AddCourse   初中数学    初中数学    2

    AddTeacher        庄子    zhuangzi    庄子老师   1   初中语文

    ${teachers}=       GetTeacherList
    Should Be True    $teachers==[u'庄子']


    AddTeacher        孔子    kongzi    孔子老师   2     初中数学

    ${teachers}=       GetTeacherList
    Should Be True    $teachers==[u'庄子',u'孔子']


    [Teardown]    Run Keywords   DeleteAll  course   AND  DeleteAll   teacher

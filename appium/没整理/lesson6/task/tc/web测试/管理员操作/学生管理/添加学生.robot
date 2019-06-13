*** Settings ***
Library    Collections
Library    pylib.WebOpAdmin


*** Test Cases ***

添加学生3333
    [Setup]   Run Keywords   DeleteAll    student
    ...    AND  DeleteAll    traininggrade
    ...    AND  DeleteAll    training
    ...    AND  DeleteAll    teacher
    ...    AND  DeleteAll    course
    ...  AND   AddCourse   初中语文    初中语文描述    1
    ...  AND  AddCourse   初中数学    初中数学    2
    ...  AND   AddTeacher        庄子    zhuangzi    庄子老师   1   初中数学
    ...  AND   AddTeacher        孔子    kongzi    孔子老师   2     初中语文
    ...  AND   AddTraining      初中班   初中班     1     初中数学
    ...  AND   AddTrainingGrade      初中班1期    初中班1期     1     初中班

    AddStudent         关羽    guanyu   猛将关羽   初中班  初中班1期

    ${students}=       GetStudentList
    Should Be True    $students==[u'guanyu']


    AddStudent         张飞    zhangfei   猛将张飞   初中班  初中班1期

    ${students}=       GetStudentList
    Should Be True    $students==[u'zhangfei', u'guanyu']


    [Teardown]    Run Keywords   DeleteAll    student
    ...    AND  DeleteAll    traininggrade
    ...    AND  DeleteAll    training
    ...    AND  DeleteAll    teacher
    ...    AND  DeleteAll    course
    ...  AND   AddCourse   初中语文    初中语文描述    1
    ...  AND  AddCourse   初中数学    初中数学    2
    ...  AND   AddTeacher        庄子    zhuangzi    庄子老师   1   初中数学
    ...  AND   AddTeacher        孔子    kongzi    孔子老师   2     初中语文
    ...  AND   AddTraining      初中班   初中班     1     初中数学
    ...  AND   AddTrainingGrade      初中班1期    初中班1期     1     初中班

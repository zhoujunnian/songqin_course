*** Settings ***
Variables   cfg.py
Library    pylib.WebOpAdmin
Suite Setup        Run Keywords   LoginWebsite      &{adminuser}[name]    &{adminuser}[pw]
    ...    AND  DeleteAll    student
    ...    AND  DeleteAll    traininggrade
    ...    AND  DeleteAll    training
    ...    AND  DeleteAll    lesson
    ...    AND  DeleteAll    teacher
    ...    AND  DeleteAll    course
    ...  AND   AddCourse   初中语文    初中语文描述    1
    ...  AND   AddTeacher        孔子    kongzi    孔子老师   1     初中语文
    ...  AND   AddTraining      初中班   初中班     1     初中语文
    ...  AND   AddTrainingGrade      初中班1期    初中班1期     1     初中班
    ...  AND   AddStudent         关羽    guanyu   猛将关羽   初中班  初中班1期

Suite Teardown   Run Keywords   LoginWebsite      &{adminuser}[name]    &{adminuser}[pw]
    ...    AND  DeleteAll    student
    ...    AND  DeleteAll    traininggrade
    ...    AND  DeleteAll    training
    ...    AND  DeleteAll    lesson
    ...    AND  DeleteAll    teacher
    ...    AND  DeleteAll    course
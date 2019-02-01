*** Settings ***
Library    SeleniumLibrary
Resource   rflib/rc.robot


*** Test Cases ***
添加老师1
    [Setup]  run keywords   DeleteAllTeacher
    ...   AND  DeleteAllCourse
    ...   AND  Add Course   初中语文   初中语文   1
    ...   AND  Add Course   初中数学   初中数学   2



    Add Teacher     庄子    zhuangzi    庄子老师   2    初中语文

    Add Teacher     孔子     kongzi     孔子老师   1    初中数学
    ${teachers}=    Get Teacher List

    Should Be True    ['孔子','庄子']==$teachers

    [Teardown]  run keywords   DeleteAllTeacher   AND   DeleteAllCourse


*** Settings ***
Library  apiLib

*** Test Cases ***
添加课程1 - 0001
    ${coursesBefore}=    list course
    ${addRet}=    add course    python语言    python语言基础和提升    2
    should be equal as integers   &{addRet}[retcode]    0
    ${coursesAfter}=    list course

    ${newCourse}=  get new course    ${coursesBefore}     ${coursesAfter}

    should be equal as strings   &{newcourse}[name]   python语言
    should be equal as strings   &{newcourse}[desc]   python语言基础和提升
    should be equal as strings   &{newcourse}[display_idx]   2







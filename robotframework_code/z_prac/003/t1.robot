*** Settings ***
Library    SeleniumLibrary
Library    course_mgr
Library    Collections


*** Test Cases ***
测试1
     ${courseList}=   ListCourse
     :FOR   ${ele}  IN  @{courseList}
       \    log to console   ${ele}


     ${expected}=      Create List     python语言    初中化学
    Lists Should Be Equal     ${courseList}     ${expected}



测试2
    Open Browser    https://www.vmall.com/    chrome
    Set Selenium Implicit Wait    4
    ${eles}=    Get Webelements   css=.home-hot-goods .grid-items:not(.grid-items-sm) h3
    Sleep   20
    :FOR   ${ele}  IN  @{eles}
       \   log to console   ${ele.text}  #  如果有的单品在浏览器宽度范围之外，就看不到，ele.text返回结果为空字符串
       \   ${eletxt}=   evaluate  $ele.get_attribute('innerText')
       \   log to console   ${eletxt}

    Close Browser


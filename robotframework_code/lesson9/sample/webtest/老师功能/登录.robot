*** Settings ***
Force Tags     登录    冒烟测试

*** Test Cases ***
用例30001
    [Tags]    正确用户名   正确密码
    log to console    用例30001主体部分


用例30002
    [Tags]    正确用户名   正确密码
    log to console    用例30002主体部分
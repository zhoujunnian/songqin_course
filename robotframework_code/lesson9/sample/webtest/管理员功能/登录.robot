*** Settings ***
Force Tags     登录    冒烟测试
Default Tags   notag

*** Test Cases ***
用例10001
    [Tags]    正确用户名   正确密码   10001
    log to console    用例10001主体部分
    Fail


用例10002
    [Tags]    正确用户名   正确密码    10002
    log to console    用例10002主体部分


用例10003
    [Tags]    正确用户名   错误密码    10003
    log to console    用例10003主体部分


用例10004
    log to console    用例10004主体部分
    Fail
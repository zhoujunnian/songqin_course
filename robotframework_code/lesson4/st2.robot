*** Settings ***
Suite Setup       log to console   \n --- Suite st2 Setup ---
Suite Teardown    log to console   \n --- Suite st2 Teardown ---



*** Test Cases ***
测试1
    [Setup]    log to console  \n *** case 测试1 setup ****
    log to console   测试用例主体部分 11
    [Teardown]    log to console   \n *** case 测试1 teardown ****

测试2
    log to console   测试用例主体部分22

测试3
    log to console   测试用例主体部分33

*** Settings ***
Suite Setup       log to console   \n --- Suite st Setup ---
Suite Teardown    log to console   \n --- Suite st Teardown ---
Test Setup       log to console   \n --- Test st Default Setup ---
Test Teardown    log to console   \n --- Test st Default Teardown ---


*** Test Cases ***
测试1
    [Setup]    log to console  \n *** case 1 setup ****
    log to console   测试用例主体部分11
    [Teardown]    log to console   \n *** case 1 teardown ****

测试2
    log to console   测试用例主体部分22

测试3
    log to console   测试用例主体部分33

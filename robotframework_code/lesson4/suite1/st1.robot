*** Settings ***
Suite Setup       log to console   \n --- Suite little Setup ---
Suite Teardown    log to console   \n --- Suite little Teardown ---
Test Setup       log to console   \n --- Test little Default Setup ---
Test Teardown    log to console   \n --- Test little Default Teardown ---


*** Test Cases ***
测试1
    [Setup]    log to console  \n *** 测试用例1 setup ****
    log to console   测试用例1 主体部分
    [Teardown]    log to console   \n *** 测试用例1 teardown ****

测试2
    log to console   测试用例2 主体部分

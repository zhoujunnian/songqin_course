*** Settings ***
Library    Selenium2Library
Library    Dialogs
Library    mylib1

*** Test Cases ***
商城测试
    [Documentation]    商城界面测试
    Open Browser    https://www.vmall.com/    chrome
    Set Selenium Implicit Wait    10


#   检查界面是否布局正确 ??????????????????
    Execute Manual Step    请检查界面布局是否清晰    界面布局不清晰

    Execute Manual Step    请检查logo图片是否是菊花    logo错误

    [Teardown]  close browser
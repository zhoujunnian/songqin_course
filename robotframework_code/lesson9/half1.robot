*** Settings ***
Library    Selenium2Library
Library    Dialogs
Library    mylib1

*** Test Cases ***
12306购票
    [Documentation]    购买火车票
    Open Browser    https://kyfw.12306.cn/otn/login/init    chrome
    Set Selenium Implicit Wait    10

    input text   id=username    pppoe4444
#   选择验证码 ??????????????????



    click element   id=loginSub

    click element   id=selectYuding

    click element   id=fromStationText
    input text      id=fromStationText      南京南\n

    click element   id=toStationText
    input text      id=toStationText        杭州东\n

    click element   css=#date_range li:nth-child(2)

    click element   css=a.btn72[onclick*='5l000G762520']

    Pause Execution    演示需要，暂停一下
    close browser
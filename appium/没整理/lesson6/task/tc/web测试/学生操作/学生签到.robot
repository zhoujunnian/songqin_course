*** Settings ***
Library    Collections
Variables   cfg.py
Library    pylib.WebOpAdmin    WITH NAME    WA
Library    pylib.WebOpStudent  WITH NAME    WS


*** Test Cases ***
学生签到5001
     WA.loginWebSite     &{adminuser}[name]   &{adminuser}[pw]
     WA.AddLesson     初中语文   初中语文第1课
     Sleep    2
     WS.loginWebSite     guanyu     sq888
     WS.CheckIn

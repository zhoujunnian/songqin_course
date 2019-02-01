*** Settings ***
Variables   cfg.py
Library    pylib.MobileOp
Suite Setup       createSession
Suite Teardown    closeSession
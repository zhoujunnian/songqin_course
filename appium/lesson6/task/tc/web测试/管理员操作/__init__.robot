*** Settings ***
Variables   cfg.py
Library    pylib.WebOpAdmin
Suite Setup       LoginWebsite      &{adminuser}[name]    &{adminuser}[pw]


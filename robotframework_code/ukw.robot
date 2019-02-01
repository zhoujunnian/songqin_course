| *** Settings *** |
| Library        | Selenium2Library |

| *** Test Cases *** |
| tc1 |
|    | baidu search | 松勤 | 松勤软件测试 |
|    | baidu search | 松勤软件 | 松勤软件测试 |

| tc3 |
|    | ${ret}= | multiply | 2 | 3 |
|    | log to console | ${ret} |

| tc4 |
|    | ${q} | ${r}= | divide | 8 | 2 |
|    | log to console | ${q}:${r} |

| *** Keywords *** |
| baidu search |
|    | [Arguments] | ${keyword} | ${firstlinktxt} |
|    | Open Browser | http://www.baidu.com | chrome |
|    | Input Text | id=kw | ${keyword}\n |
|    | Set Selenium Implicit Wait | 2 |
|    | ${firstRet}= | Get Text | css=div.result:first-of-type>h3 |
|    | Should Be Equal | ${firstRet} | ${firstlinktxt} |
|    | Close Browser |

| multiply |
|    | [Arguments] | ${x} | ${y} |
|    | ${ret}= | Evaluate | ${x} * ${y} |
|    | [Return] | ${ret} |

| divide |
|    | [Arguments] | ${x} | ${y} |
|    | ${q}= | Evaluate | ${x} / ${y} |
|    | ${r}= | Evaluate | ${x} % ${y} |
|    | [Return] | ${q} | ${r} |

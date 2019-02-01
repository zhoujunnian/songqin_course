| *** Settings *** |
| Library        | mylibrary |

| *** Variables *** |
| ${scalar_var1} | this is var1 |
| @{list_var1}   | 1 | 2 | 3 | 4 | 5 |
| &{dict_var1}   | e1=male | e2=female |

| *** Test Cases *** |
| tc0 |
|    | printarg | 54 |
|    | printarg | ${54} | # 整数 |
|    | printarg | ${2.34} | # 小数 |
|    | printarg | ${0xff} | # 16进制 |
|    | printarg | ${true} | # 布尔值 |
|    | printarg | ${None} | # Python None |
|    | printarg | ${EMPTY} | # 空字符串 |
|    | printarg | ${SPACE} | # 空格 |

| tc1 |
|    | @{var1}= | return list |
|    | printarg | ${var1} |

| tc1-2 |
|    | @{var1}= | return list |
|    | printarg | hello, ${var1} \  |

| tc2 |
|    | ${var1}= | return list |
|    | printarg | ${var1} |
|    | printarg | @{var1} |

| tc2-1 |
|    | ${var1}= | return list |
|    | printarg | @{var1}[0] |

| tc5 |
|    | ${var1}= | returndict |
|    | printarg | ${var1} |
|    | printarg | &{var1} |

| tc5-1 |
|    | ${var1}= | returndict |
|    | printarg | &{var1}[ele1] |

| tc6 |
|    | printarg | %{path} |

| tc7-1 |
|    | ${var1}= | Set Variable | Hello  |
|    | @{list}= | Create List | a | b |
|    | &{dict}= | Create Dictionary | a1=firefox | a2=chrome |
|    | ${ele1} | ${ele2}= | Create List | a | b |
|    | printarg | ${var1} |
|    | printarg | ${list} |
|    | printarg | @{list} |
|    | printarg | ${dict} |
|    | printarg | &{dict} |
|    | printarg | ${ele1} | ${ele2} |

| tc7-2 |
|    | printarg | ${scalar_var1} |
|    | printarg | ${list_var1} |
|    | printarg | ${dict_var1} |
|    | printarg | &{dict_var1} |

| tc7-3 |
|    | Set Test Variable | ${var_scalar} | hello |
|    | Set Suite Variable | ${var_suite} | hello |
|    | Set Global Variable | ${var_global} | hello |

| tc-cmdline |
|    | printarg | ${var_cmd1} |
|    | printarg | ${var_cmd2} |

| *** Settings *** |
| Library        | mylibrary1 |

| *** Test Cases *** |
| case1 |
|    | ${varlist}= | return list |
|    | log to console | ${varlist} |
|    | ${a}= | set variable | abc |
|    | ${b}= | set variable | ${1} |
|    | Should be true | '${a}'=='abc' |
|    | Should be equal | ${a} | abc |
|    | Should be equal | ${b} | ${1} |

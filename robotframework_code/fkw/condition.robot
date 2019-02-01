| *** Test Cases *** |
| mytest |
|    | ${color} = | set variable | Red |
|    | Run Keyword If | '${color}' == 'Red' | log to console | \nexecuted with single condition |
|    | Run Keyword If | '${color}' == 'Red' or '${color}' == 'Blue' or '${color}' == 'Pink' | log to console | \nexecuted with multiple or |
|    | ${color} = | set variable | Blue |
|    | ${Size} = | set variable | Small |
|    | ${Simple} = | set variable | Simple |
|    | ${Design} = | set variable | Simple |
|    | Run Keyword If | '${color}' == 'Blue' and '${Size}' == 'Small' and '${Design}' != '${Simple}' | log to console | \nexecuted with multiple and |
|    | ${Size} = | set variable | XL |
|    | ${Design} = | set variable | Complicated |
|    | Run Keyword Unless | '${color}' == 'Black' or '${Size}' == 'Small' or '${Design}' == 'Simple' | log to console | \nexecuted with unless and multiple or |

| mytest2 |
|    | ${color} = | set variable | Red2 |
|    | Run Keyword If | '${color}' == 'Red' | log to console | \nRed |
|    | Run Keyword Unless | '${color}' == 'Red' | log to console | \nNot Red |

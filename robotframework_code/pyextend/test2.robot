| *** Settings *** |
| Library        | mylibrary2.SubLibrary | localhost | 80

| *** Test Cases *** |
| case1 |
|    | ${varint}= | returnint |
|    | log to console | ${varint} |
|    | printaddr |

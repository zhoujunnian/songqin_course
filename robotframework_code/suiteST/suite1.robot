| *** Settings *** |
| Suite Setup    | log to console | *** 33333 *** suite 1 - suite setup |
| Suite Teardown | log to console | *** 33333 *** suite 1 - suite setup |
| Test Setup     | log to console | \n*** 44444*** suite 1 - test setup |
| Test Teardown  | log to console | \n*** 44444*** suite 1 - test teardown |

| *** Test Cases *** |
| testcase1 |
|    | [Setup] | log to console | \n*** 55555*** case 1 - setup |
|    | log to console | \ncase 1 - executing |
|    | [Teardown] | log to console | \n*** 55555*** case 1 - teardown |

| testcase2 |
|    | log to console | \ncase 2 - executing |

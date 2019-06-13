*** Settings ***
Library   pylib.MobileOp

*** Test Cases ***

查看第一篇文章

    ${title1}=    openFirstArticle

    ${title2}=    getOpenedArticleTitle

    should be equal as strings    ${title1}    ${title2}

    pressKey   back

    ${ret}=    isInMainActivity
    should be true      $ret
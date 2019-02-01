# 获取html内容字符串，进行分析
with open('bs1.html',encoding='utf8') as f:
    html_doc = f.read()

# 导入 BeautifulSoup
from bs4 import BeautifulSoup

# 指定用html5lib来解析html文档
soup = BeautifulSoup(html_doc, "html5lib")






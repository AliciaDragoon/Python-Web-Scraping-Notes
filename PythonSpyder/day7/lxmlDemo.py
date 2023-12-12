from lxml import etree

f = open("index.html", mode="r", encoding="utf-8")
content = f.read()  # 页面源代码

# 默认情况下，pycharm不知道类型，所以没有代码提示
page = etree.HTML(content)  # type: etree._Element
# print(type(page))  # <class 'lxml.etree._Element'>
# 用type()得到数据类型，在变量被赋值位置添加# type: 类型

page.xpath("")  # 筛选
# print(main_page)

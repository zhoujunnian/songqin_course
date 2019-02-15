# coding=utf-8
beforetax = [10000,15000,8000,4000,5000]
aftertax = []
for i in beforetax:
	aftertax.append(0.9*i)
print aftertax


"""
列表生成式：
典型的从源列表生成目标列表的处理场景
1）从源列表里面 依次取出元素
2）做同样的处理
3）放入另一个列表中
"""
beforetax =  [10000,15000,8000,4000,5000]
aftertax = [one*0.9 for one in beforetax]
aftertax = [int(one*0.9) for one in beforetax]
print aftertax

# 加上过滤条件
beforetax =  [10000,15000,8000,4000,5000]
aftertax = [one*0.9 for one in beforetax if one >= 10000]
print aftertax
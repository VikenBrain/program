# Todo zip()

# 前面介绍的map()函数时，我们举个例子将=某个函数应用到平行的两个列表。而zip()函数能够更简单的做到这一点

first_names = ['Peter', 'Christian', 'Klaus']
last_names = ['Jensen', 'Smith', 'Nistrup']
print([' '.join(x) for x in zip(first_names, last_names)])


# 这个可以应用到两个字段具体值的拼接，如果两个字段是数值可以进行相乘，这种方案是解决字符串的问题
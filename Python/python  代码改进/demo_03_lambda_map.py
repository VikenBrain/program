# Todo lambda

# lambda是一种匿名函数
stupid_func = (lambda x: x ** 2 + 5)
# print(stupid_func(1), stupid_func(3), stupid_func(5))


# 执行一些简单运算时，可以不用定义真实函数就能完成。
my_list =[2, 1, 0, -1, -2]
# print(sorted(my_list))
# 借助lambda表达式，可以实现更自由的排序标准。
# print(sorted(my_list, key= lambda x:x **2))

# Todo map

# Map 是一个简单的函数，他可以将某个函数应用到其它一些序列元素，如列表。如果我们希望有两个列表中对应的元素相乘
x, y = [1, 2, 3], [4, 5, 6]
z = []
for i in range(len(x)):
    z.append(x[i] * y[i])
print(z)

print(list(map(lambda x, y : x * y, [1, 2, 3], [4, 5, 6])))
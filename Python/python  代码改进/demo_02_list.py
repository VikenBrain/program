
# Todo 一般代码

def stupid_func(x):
    return x**2 + 5

# my_list = [1, 2, 3, 4, 5]
# new_list = []
# for x in my_list:
#     if x % 2 != 0:
#         new_list.append(stupid_func(x) )
#
# print(new_list)


# 列表推导式
my_list  = [1, 2, 3, 4, 5]
print([stupid_func(x) for x in my_list if x %2 !=0])
print([x ** 2 + 5 for x in my_list if x % 2 != 0])

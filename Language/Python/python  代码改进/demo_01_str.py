# Todo 字符串运算

# # 正序
my_string = "hello world...!"
# print(my_string * 2)
#
#
# # 反向
# print(my_string[::-1])


# 如果列表元素都是字符串，那么可以快速的使用join()方法将所有元素拼接在一起
word_list = ['awesome', 'is', 'this']
print(''.join(word_list[::-1]) + '!')
# 如果我么使用.join()方法拼接列表元素，其中（特殊字符，敲不出来）便是连接方式为空格。其中自然语言处理中，
# 这个方法会被经常使用，例如我们将句子拆分为了字符，那么处理后放入合并就需要使用.join()



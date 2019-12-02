### 列表（`list`）推导式

1.1 列表推导式

```python
variable = [out_exp_res for out_exp in input_list if out_exp == 2]
```

> - out_exp_res：列表生成元素表达式， 可以是有返回值的函数
> - for out_exp in input_list：迭代input_list 将out_exp传入out_exp_res表达式中
> - if out_exp == 2：根据条件过滤哪些值可以

```python
multiples = [i for i in range(30) if i%3 == 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```

1.2 使用（）生成generator

```puyjpm
multiples = (i for i in range(30) if i%3 == 0)
print(type(multiples))
# Output: <type 'generator'>
```



### 字典（`dict`）推导式

```python
mcase = {'a': 10, 'b': 34}
mcase_frequancy = {v: k for k, v in mcase.items()}
print(mcase_frequancy)

#  Output: {10: 'a', 34: 'b'}
```



### 集合（`set`）推导式

结合推导式和列表推导式有些类似。唯一的区别在于它使用大括号{}

```python
squared = {x**2 for x in {1, 1, 2}}
print(squared) # 打印出一个集合区间

# Output: set([1, 4])
```


 

### difficult problem

1. 大数据集下列对不齐的问题？

    ```python 
    采用固定列的方式
    ```



---

### code

#### 01 特征变量的命名

```python
# 两者有什么不同，暂时还不知道
data['url']
data.url
```

#### 02 删除表中的特征值

```python
# 这里不返回序列的方式也可以采用to_csv('file_name.csv', index=0)
data.drop(["code", "name"], axis=1, inplace=True)
# 这里值得注意的是axis=1表示要删除的列, inplace=True如果没有这个字段的话可能列是删不掉的
```

#### 03 删除缺失值和去重

```python
# 这里的axis=0代表的是删除缺失行， how='any'， 只要存在一个缺失就删除
new_data = data.dropna(axis=0, how='any', inplace=True) # 删除缺失项 
- axis：
    - axis=0:删除包含缺失值的行
    - axis=1:删除包含缺失值的列
- how：
	- how='any':只要有缺失值出现，就删除该行或列
	- how='all':所有的值都缺失，才删除行或列
- thresh：
    - axis中至少有thresh个非缺失值，否则删除
        - 比如axis=0， thresh=10：表示如果该行中非缺失值的数量小于10，将删除该行
- inplace: 
    - 是否在原数据上操作。如果为True，返回None
    - False返回新的copy，去掉了缺失值
# 去重, 去重的字段，first意思是保留第一个
data_cdn.drop_duplicates('query_string', 'first', inplace=True) # 去重
```



#### 03 对表中的特征值进行提取

- split切分

```python
data['uri'] = data.uri.apply(func = lambda x:x.split("/")[2])
```

- 正则提取

#### 04 特征名重命名

```python
data.rename(columns={
    'uri':'uri',
    'sendSize':'send_data',
    'contentLength':'resp_data',
    'readTime':'read_time',
    'complete_rate':'complete_rate',
}, inplace=True)
```

#### 05 特征值类型转化

```python
heartbeat_data['nls_ts'] = heartbeat_data['nls_ts'].astype('int')
# 这两个究竟有什么区别
heartbeat_data['nls_ts'] = heartbeat_data['nls_ts'].astype(int) 对数字模式的字符串进行转化
```

#### 06 特征值替换

```python
# 这里是只能替代字符串为数字，而不能替代数字为数字
f_data['refer'] = f_data.refer.apply(func=lambda x:x.replace('360_router_p4g','0'))
```

```python
 # 对ab_time中的数值进行数字等级替换,这里暂时只能做到一层替换
 data['abTime'] = data['abTime'].map(lambda x:0 if x<=200 else 1)
```



#### 07 绘制可视化图中文乱码

```python
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
```

#### 08 表的合并

```python
# 注意完了之后一定要去重
result = pd.merge(dt_a, dt_b, how='left', on=['code', 'region'])  # 左连接
result = pd.merge(dt_a, dt_b, how='right', on=['code', 'region']) # 右连接
result = pd.merge(dt_a, dt_b, how='outer', on=['code', 'region']) # 并集
result = pd.merge(dt_a, dt_b, how='inner', on=['code', 'region']) # 交集
```

#### 10 pandas读取文件

```python
 # chunksize 将数据以多么大小的单位读取
 data = pd.read_csv('file_name.csv', sep=',', chunksize=100000) 
 for chunk in data:
     print(chunk)
```

#### 11 表中特征列交换位置

```python
#调整字段的顺序即可
data_dispatch = data_dispatch[['uid', 'refer', 'type', 'num', 'create_time']]
```

#### 12 python数据进筛选取子集

- loc

    ```python
    # loc取子集用的是字符串
    recv_30 = data.loc[(data['recvTime'] <= 30) & (data['abTime']<=1000)]
    """
    和：&
    或：|
    """
    ```

- iloc

    ```python
    # iloc用的是数字
    ```

#### 13 特征进行比较

```python
 # 相同字段的字符串标记为1， 不同标记为0
 data['new'] = data.apply(lambda x: x['miner_province'] in x['province'], axis= 1).astype(int)
```

#### 14 pycharm 控制台打印文件不隐藏

```python
 pd.set_option('display.max_columns',1000)
 pd.set_option('display.width', 1000)
 pd.set_option('display.max_colwidth',1000)
```

#### 15 计算以`uri`进行分组的下载成功率排名

```python
def func(sub_pd):  
    ct = sub_pd.shape[0] 
    dt = sub_pd[sub_pd.complete_rate==0.0].shape[0] 
    return ct, dt, dt/ct 
num = data.groupby(["uri"]).apply(func)
print(num.sort_values(ascending=False)[:20]) 
```

#### 16 对int数据变量进行范围切分

```python
range_data  = []
for i in range(0, 13):
    range_data.append(float(i))

new_range_data  = []
for i in range(0, 12):
    new_range_data.append(i)
# print(new_range_data)

f_data['avgspeed'] = f_data['avgspeed'] // 1000 # 分组之前的处理
f_data['avgspeed'] = pd.cut(f_data['avgspeed'], range_data, right=False, labels=new_rnge_data)
```

#### 17 面向对象数据导入

```python
 # 通过时间判断文件是否已经存在，如果文件存在，就不用重复下载了
 download_data = "{}_{}.csv".format(MDEL()[2], base_cons.basic()[2]) 
 
 if os.path.exists(download_data): 
     print("我们的勇气绝对不能动摇！")
 else:
     miner_diapatch_error_list.MDEL().start() # 调用数据的接口
```

#### 18 时间转化

- 将Unix时间戳转化为北京时间

    ```python
    data['create_time'] =  pd.to_datetime(data['create_time'].values, utc=True, unit='s').tz_convert("Asia/Shanghai").to_period("S")
    ```

- 将时间转化为时间戳

 






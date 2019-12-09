最开始了解range是在爬虫里面有关于断点续传的知识。

所谓断点续传，也就是要从文件已经下载的地方开始继续下载。在以前的版本HTTP协议是不支持断点续传的，HTTP/1.1开始就支持了。一般断点下载时才用到Range和Content-Range实体头。

**Range** 

用于请求头中，指定第一个字节的位置和最后一个字节的位置，一般格式：

`Range:(unit=first byte pos)-[last byte pos] `

**Content-Range**

用于响应头，指定整个实体中的一部分的插入位置，他也指示了整个实体的长度。在服务器向客户返回一个部分响应，它必须描述响应覆盖的范围和整个实体长度。一般格式： 

`Content-Range: bytes (unit first byte pos) - [last byte pos]/[entity legth] `

举例：

```python
请求下载整个文件: 

GET /test.rar HTTP/1.1 
Connection: close 
Host: 116.1.219.219 
Range: bytes=0-801 //一般请求下载整个文件是bytes=0- 或不用这个头(非range请求)
一般正常回应

HTTP/1.1 200 OK 
Content-Length: 801      
Content-Type: application/octet-stream 
Content-Range: bytes 0-800/801 //801:文件总大小
```

假如要开发一份多线程的下载工具，会想着把文件分割成多个部分。比如4个部分， 然后创建4个线程， 每个线程负责下载一个部分，如果文件大小为403个byte，那么你的分割方式可以为：0-99 (前100个字节)，100-199(第二个100字节)，200-299(第三个100字节)，300-402（最后103个字节）。

```python
分割完成，每个线程都明白自己的任务，比如线程3的任务是负责下载200-299这部分文件，现在的问题是：线程3发
送一个什么样的请求报文，才能够保证只请求文件的200-299字节，而不会干扰其他线程的任务。这时，我们可以使
用HTTP1.1的Range头。Range头域可以请求实体的一个或者多个子范围，Range的值为0表示第一个字节，也就是
Range计算字节数是从0开始的：
    表示头500个字节：Range: bytes=0-499
    表示第二个500字节：Range: bytes=500-999
    表示最后500个字节：Range: bytes=-500
    表示500字节以后的范围：Range: bytes=500-
    第一个和最后一个字节：Range: bytes=0-0,-1
    同时指定几个范围：Range: bytes=500-600,601-999
所以，线程3发送的请求报文必须有这一行：
    Range: bytes=200-299
```




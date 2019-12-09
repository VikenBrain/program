

### URL、域名、DNS解析

#### 01 URL和URI

URL(Uniform Resource Locator 统一资源定位符) 是URI(Uniform Resource Identifier 统一资源标识符) 的子集，标识着资源在互联网中的具体地址。

uri的标准格式：

```cpp

                    hierarchical part
        ┌───────────────────┴─────────────────────┐
                    authority               path
        ┌───────────────┴───────────────┐┌───┴────┐
  abc://username:password@example.com:123/path/data?key=value&key2=value2#fragid1
  └┬┘   └───────┬───────┘ └────┬────┘ └┬┘           └─────────┬─────────┘ └──┬──┘
scheme  user information     host     port                  query         fragment

  urn:example:mammal:monotreme:echidna
  └┬┘ └──────────────┬───────────────┘
scheme              path

// 这里不对URI的格式进行详细的说明，因为更为普遍知晓的是其子集URL
```

URL的标准格式：

> 协议类型:[//服务器地址[:端口号]][/路径]文件名[?查询][#片段]
>  scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]
>
> 注： 在http协议中 user 和 password 在url中通常不是必须的，所以我们平时所看到的url是没有user 和 password 的，另外由于http协议的默认端口号是80，所以80端口也被省略了。在使用http协议的时候，一般除了域名，其他的都是可省略的，`http://`会由浏览器自动补上

```cpp
http://zh.wikipedia.org:80/w/index.php?title=Special:%E9%9A%8F%E6%9C%BA%E9%A1%A2&printable=yes
1. http                              // 协议，其他常用协议有ftp、file、telnet、mailto等
2. zh.wikipedia.org                  // 域名即服务器
3. 80                                // 服务器上的端口号（http协议默认的端口，可以省略）
4. /w/index.php                      // 路径
5. ?title=Special:XXXX&printable=yes  // query  
```

#### 02 域名

> 域名的来源： IP地址是Internet主机的作为路由寻址用的数字型标识，但却不容易记忆，为了更容易记忆一个主机或服务器，因而产生了域名（domain name）这一种字符型标识。再由DNS服务将其转换成计算机可以识别的IP，跟IP一样域名也是独一无二的，一旦注册，便与对应的IP唯一的绑定

```cpp
一级域名是顶级域名
.com/.cn/.org/.info/.edu/.name 等是顶级域名
taobao.com 是二级域名
XXX.taobao.com 是三级域名（子域名）
```

#### 03 DNS(Domain Name System) 域名系统

> 人们习惯记忆域名，但机器间互相只认IP地址，域名与IP地址之间是一对一（或者一对多）的，它们之间的转换工作称为域名解析，域名解析需要由专门的域名解析服务器来完成，整个过程是自动进行的。

解析过程：

```python
1. 浏览器将会检查缓存中有没有这个域名对应的解析过得IP地址，如果有该解析过程将会结束。
浏览器缓存域名也是有限制的，包括缓存的时间、大小，可以通过TTL属性来设置。
2. 如果用户的浏览器中缓存中没有，浏览器将会查找操作系统缓存中是否有这个域名对应 
的DNS解析结果。其实操作系统也会有一个域名解析的过程，在Windows中可以通过
C:WindowsSystem32driversetchosts文件来设置，你可以将任何域名解析到任何能够访问的IP
地址。那么浏览器会首先使用这个IP地址。也正是因为有这种本地DNS解析的规程，所以黑客就
有可能通过修改你的域名解析来把特定的域名解析到它指定的IP地址上，导致这些域名被劫持。
3. 读取网络设置中的“DNS服务器地址”，操作系统就会将这个域名发送给这里设置的
LDNS，也就是本地的域名服务器。这个DNS通常都提供给你本地互联网接入的一个DNS服务。
如果你在小区接入的互联网，那这个DNS就是提供给你接入互联网的应用提供商，即电信或者
是联通，也就是通常所说的SPA，可以通过ipconfig查询这个地址。
4. 如果LDNS仍然没有命中，就直接到Root Server域名服务器中请求解析。
5. 根域名服务器返回给本地服务器一个所查询域的主域名服务器地址（gTLD Server）。
gTLD是国际顶级域名服务器，如.com、.cn、.org等，全球只有13台左右。
6. 本地域名服务器（Local DNS Server）再向上一步返回的gTLD服务器发送请求。
7. 接受请求的gTLD服务器查找并返回此域名对应的Name Server域名服务器的地址，这
个Name Server通常就是你注册的域名服务器的域名服务商，例如你的域名服务商A那里申请一
个域名，那个gTLD将会把这个域名解析任务交由这个域名服务商的服务器来解析。
8. Name Server域名服务器会查询存储的域名和IP的映射关系表，正常情况下都根据域名
得到目标IP表，连同一个TTL值返回给DNS Server域名服务器。
9. 返回该域名对应的IP以及TTL值，Local DNS Server会缓存这个域名和IP的对应关系，
缓存时间由TTL值限制。
10. 把解析的结果返回给用户，用户根TTL值缓存在本地系统缓存中，域名解析过程结束。
```


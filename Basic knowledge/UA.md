### User-Agent

```Python
User-Agent: <product> / <product-version> <comment>
```

- <product>产品识别码
- <product-version>产品版本号
- <comment>零个或多个组成产品信息的注释

浏览器通常使用的格式为：

```python
User-Agent: Mozilla/<version> (<system-information>) <platform> (<platform-details>) <extensions>
```

- Mozilla/5.0：是一个通用标记符号，用来表示与Mozilla兼容，这几乎是现代标准浏览器的标配。
- Gecko/geckotrail 表示该浏览器基于 Gecko 渲染引擎。


Firefox UA 字符串
```python
Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion
```

Chrome UA 字符串
Chrome （或 Chromium/blink-based engines）用户代理字符串与 Firefox 的格式类似。为了兼容性，它添加了诸如 "KHTML, like Gecko" 和 "Safari" 这样的字符串。
```python
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
```

Opera UA 字符串
Opera 也是一款基于 blink 引擎的浏览器，这也是为什么它的 UA 看起来（和 Chrome 的）几乎一样的原因，不过，它添加了一个 "OPR/<version>"。
```python
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41
```
使用 Presto 引擎的、更老的 Opera 浏览器使用：
```python
Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00
Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1
```

Safari UA 字符串
这是 Safari 的移动版本的用户代理字符串。因为其中包含了单词 "Mobile" 。
```python
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1
```

Internet Explorer UA 字符串
```python
Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)
```

爬虫和机器人的UA字符串
```python
Googlebot/2.1 (+http://www.google.com/bot.html)
```

```python
Windows 系统：
Windows NT 5.0 // 如 Windows 2000 
Windows NT 5.1 // 如 Windows XP
Windows NT 6.0 // 如 Windows Vista 
Windows NT 6.1 // 如 Windows 7
Windows NT 6.2 // 如 Windows 8
Windows NT 6.3 // 如 Windows 8.1
Windows NT 10.0 // 如 Windows 10
Win64; x64 // Win64 on x64
WOW64 // Win32 on x64
Linux 系统：
X11; Linux i686; // Linux 桌面，i686 版本
X11; Linux x86_64; // Linux 桌面，x86_64 版本
X11; Linux i686 on x86_64 // Linux 桌面，运行在 x86_64 的 i686 版本
macOS 系统：
Macintosh; Intel Mac OS X 10_9_0 // Intel x86 或者 x86_64
Macintosh; PPC Mac OS X 10_9_0 // PowerPC
Macintosh; Intel Mac OS X 10.12; // 不用下划线，用点
```

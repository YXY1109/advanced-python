本课程介绍了如何使用AIO HTTP构建并发爬虫。主要内容包括：

1. **为什么选择AIO HTTP**：因为rsyncIO虽然可以实现TCP和UDP协议，但并没有实现HTTP协议，而AIO
   HTTP基于rsyncIO实现了一个完整的HTTP客户端和服务器，适合用于HTTP请求。

2. **AIO HTTP的安装与使用**：AIO HTTP支持Python 3.6版本，当前可能不支持3.7版本。可以通过pip安装AIO
   HTTP和相关的数据库驱动（如AIOMyCircle）。

3. **构建爬虫的基本步骤**：
    - **获取URL**：从初始页面获取所有链接。
    - **解析URL**：根据特定模式（如jobbobler.com/文章ID）判断是否为文章详情页。
    - **请求页面**：使用AIO HTTP异步请求页面。
    - **处理响应**：检查响应状态码，如200则解析内容并入库。

4. **示例代码**：使用AIO HTTP和pyquery（用于HTML解析）实现一个简单的爬虫，从伯乐在线网站（jobbobler.com）爬取文章链接并解析内容。

5. **推荐资源**：对于对爬虫技术感兴趣的学习者，推荐学习基于Twisted的Scrapy框架，这是Python中最流行的爬虫框架之一。

通过这些内容，课程帮助学习者理解如何使用AIO HTTP实现高效的并发爬虫，并加深对rsyncIO的理解。
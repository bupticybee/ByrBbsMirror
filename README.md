# ByrBbsMirror

> Across the Great Wall we can reach every corner in the world.

北邮人论坛镜像源代码,每个技术人都可以通过这份代码快速搭建起一个北邮人论坛镜像.

采用GPL-V3协议，禁止商用

## 背景

2016年北邮人论坛正式关闭对外访客，同天下午，北邮人论坛镜像开发完毕：

http://icybee.cn/article/58.html

## 使用

1. 安装nginx，需要支持sub_filter模块的版本
2. 将 nginx.conf中的内容添加到你的nginx配置文件中
3. 运行byrmirror/redir.py 启动重定向引擎
4. 将nginx中的img和js路径配置到statics中的资源文件路径下
5. 如果需要回帖功能，运行byrmirror/receiver.py 和 byrmirror/redir.py 启动镜像回帖功能后段(可选)

# License

[GPL V3](https://www.gnu.org/licenses/gpl-3.0.en.html)

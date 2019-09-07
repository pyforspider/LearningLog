# 1. epoll并不一定比 select好
# 2. 在并发度高，连接不活跃时，epoll好， 如 网页
# 3. 在连接活跃，并发度不高时， select好， 如 游戏

# 通过非阻塞io实现http请求

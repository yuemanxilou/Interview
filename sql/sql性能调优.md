链接：http://coolshell.cn/articles/1846.html
1为查询缓存优化你的查询
2 explain 你的select 查询
3 当只要一行数据时使用 limit 1
4 为搜索字段创建索引
5 在join表的时候使用相当类型的例，并将其索引
6 千万不要 order by rand()
7 避免select *
8 永远为每张表设置一个ID
9 使用enum 而不是varchar
10 从procedure analyse()取得建议
11 是可能的使用 not null
12 prepared statements
13 无缓冲的查询
14 把ip地址存成 unsigned int
15 固定长度的表会更快
16 垂直分割
17 拆分大的delete 或 insert语句 使用 limit
18  越小的列会越快
19 选择正确的存储引擎  myisam 适合大量查询操作 innodb适合写操作, 支持行锁、事物
20 使用一个对象关系映射器（Object Relational Mapper）
21 小心“永久链接”
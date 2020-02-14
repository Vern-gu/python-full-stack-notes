-- 多数据插入：
-- 基本语法：insert into 表名[(字段列表)] values(值列表),(值列表)...

-- 主键冲突：向已经有的主键插入重复的数据
-- 冲突更新：将原有的冲突的主键更新为新信息
-- insert into 表名[(字段列表)] value(值列表) on duplicate key update 字段= 值;
-- 冲突替换：干掉原来的数据，重新插入进去
-- replace into 表名[(字段列表)] value(值列表),(值列表)...;

-- 蠕虫复制：一分为二，成倍增加。从已有的数据中获取数据并插入到表中
-- insert into 表名[(字段列表)] select */字段列表 from 表名;

--=================================================================
-- 更新数据：更新数据普遍需要跟随条件
-- 如果没有条件，也可以使用limit来限制更新的数量
-- update 表名 set 字段名 = 新值[where 字段名= 值] limit 数量;

--=================================================================
-- 删除数据：删除数据时应当也添加条件限制，尽量不要全部删除
-- 也可以使用limit来限制删除的数量

-- 重置自增长：当自增长的数据删除后，往往下一个数据仍会接着原来的数据继续增长下去
-- truncate 表名;    本质是先删除数据再添加数据

--=================================================================
-- 查询数据：
-- 完整的查询指令语句：
-- select select选项 字段列表 from 表名 where 条件 group by 分组 having条件 order by 排序 limit 限制;
-- select选项：all（默认），distinct（去重复）
-- 字段列表中可设置别名，字段名 [as] 别名

-- 查询多表数据：
-- from 表1，表2...
-- 其结果为从第一张表取出一条数据去拼凑第二张表的记录，保留所有结果。在数学上称为笛卡尔积。应当避免笛卡尔积

-- 动态数据：from 后面跟的数据不是一个实体表，而是一个从表中查询出来得到的二维表结果(子查询)
-- 基本语法：from(select 字段列表 from 表)as 别名;

-- where子句：条件筛选，符合条件就显示，不符合则不显示

-- group by子句：根据指定的字段将数据分组，分组的目的是为了统计
-- 分组统计：group by 字段名; 根据“字段名”进行分组
-- group by 将数据按照指定的字段分组后，只会保留每组的第一条记录

-- 统计函数(聚合函数)：
-- count()统计每组中的数量，若统计目标为字段，则不统计null字段，若为*则代表统计记录
-- avg()求平均值
-- sum()求和
-- max()求最大值
-- min()求最小值
-- group_concat()将分组中指定的字段进行合并（字符串拼接）
select class_id,count(*),max(stu_height),avg(stu_age) from student group by class_id;

-- group by多分组：将数据按照某个字段进行分组之后，对已经分组的数据进行再次分组
-- 基本语法：group by字段1, 字段2...;   先按照字段1进行排序，之后将结果再按照字段2排序

-- 分组排序：按照group by分组后字段进行排序，默认是升序
-- 基本语法：group by字段[asc|desc],字段[asc|desc]...;   desc降序

-- 回溯统计：多分组之后向上统计过程中，需要层层上报，此过程为回溯统计
-- 每一次分组向上统计的过程都会产生一次新的统计数据，而且当前数据对应的分组字段为null
-- 基本语法：group by 字段 [asc|desc] with rollup;

-- having子句：本质同where一样，用来进行数据条件筛选
-- having在group by子句之后可以对分组数据进行筛选，但where不行

-- order by子句：根据校对规则对数据进行排序
-- 基本语法：order by 字段[asc|desc],字段[asc|desc]...;  默认升序
-- 也可以像group by一样多字段排序
select * from student order by id asc, stu_age desc;

-- limit子句：限制获取的数量，从第一条到指定的数量
-- 基本语法：limit 数量;
-- limit还可以分页：利用limit来获取指定区间的数据
-- 基本语法：limit offset,length; offset起始值（0开始），length获取数据的数量

--==================================================================
-- 运算符：
-- 算数运算符：+ - * / % 通常用于结果运算（select 字段中）
-- 比较运算符：通常用于条件中进行限定结果
-- 比较运算符中还有between来计算区间
-- select * from student where stu_age between 10 and 20;
-- 逻辑运算符
-- in运算符：代替=，当结果是一个结果集的时候可以使用
-- in(结果1,结果2...)    select * from student where id in ("Tom","ken");
-- is运算符：专门用来判断字段是否为null的运算符
-- is null/is not null
-- like运算符：用来模糊匹配

--==================================================================
-- 联合查询：合并多个相似的选择查询的结果集。
-- 等同于将一个表追加到另一个表中，从而实现将两个表的查询结果组合到一起
-- 应用场景：将同一表中的不同结果合并到一起显示（纵向合并）
--     在数据很多的情况下，会对表进行分表操作，对每张表进行部分数据统计，用联合查询将数据存放到一起显示
-- 基本语法：select语句 union[union选项]【默认distinct】  select语句
-- 1.获取男生身高升序，女生身高降序；
(select * from student where gender='男' order by height asc limit 10)
union
(select * from student where gender='女' order by height desc limit 10);
-- 若在联合查询中使用order by则两条select语句要加括号
-- 想要order by语句在联合查询中生效就必须要配合limit语句一起使用

--==================================================================
-- 连接查询：将多张表连到一起进行查询（会导致记录数行和字段数列发生改变）

-- 交叉连接：将两张表的数据彼此交叉显示
-- 基本语法：表1 cross join 表2
select * from student cross join test:
-- 交叉连接产生的结果一般为笛卡尔积，没有实际应用

-- 内连接：从一张表中取出数据根据匹配条件来匹配另一张表
-- 基本语法：表1 [inner] join 表2 on 匹配条件
select * from student inner join test on student.id =test.id;

-- 外连接（左/右连接）：按照某一张表作为主表（所有数据都保留），根据条件连接另一张表
-- 左连接：左表为主表；右连接：右表为主表
-- 基本语法：（左）主表 left join 从表 on条件；  （右）从表 right join 主表 on 条件
-- 外连接一定会全部显示某个表，而内连接不一定

-- 自然连接：将两张表中名称相同的列合并显示，并筛选显示。相当于on 字段 = 字段
-- 除交叉连接外的所有连接都可以加natural进行自然连接
select * from student natural join test;

-- using关键字：在连接查询中用于代替on关键字，进行条件匹配
-- 前提是条件的字段必须相同，有点类似自然连接自动匹配。
select * from student left join test using(id);

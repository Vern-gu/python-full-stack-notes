-- 创建数据库：
-- 基本语法：create database 数据库名 [库选项]
-- 库选项（可选）：数据库的相关属性
-- 库选项分为charset(字符集)、collate(校对集)
-- charset: 代表当前数据库下所有表存储的数据默认指定的字符集（不指定则默认DBMS）
-- 校对集随字符集
create database my_data_base charset utf8; -- 创建字符集

show databases; -- 列出所有数据库

-- 显示部分数据库：
-- 基本语法：show databases like '匹配模式'
-- _: 匹配当前位置单个字符
-- %: 匹配指定位置多个字符
show databases like '_ass%';

show create database passwords; -- 显示数据库创建语句（查看创建该数据库的信息）

use passwords; -- 选择数据库，use+数据库名，进入该数据库

-- 修改数据库（库选项）：
-- 基本语法：alter database 数据库名 charset = 字符集 （修改数据库字符集）
alter database passwords charset = gb2312; -- 字符集改为gb2312

drop database passwords; -- 删除数据库


-- 创建数据表：
-- 1.普通创建数据表：需要先选择数据库才能建表，也可以用库名.表名的方法
-- 基本语法：create table 表名(字段名 字段类型 [字段属性], 字段名 字段类型[]...)[表选项]
create table school.class(  -- 在school库中创建class表
name varchar(10)  -- 字段名为name，name不能超过10个字符
)charset gbk;
-- 表选项：分为engine(存储引擎)、charset(字符集)(优先级高于库选项)、collate(校对集)

-- 2.复制已有表结构：从已经存在的表复制一份（只复制结构：表中数据不复制）
-- 基本语法：create table 表名 like 表名;
-- (只要使用库名.表名，就可以在任何数据库下访问其他数据库的表名)
create table students like school.class;
-- 复制表：create table 表名 select ... from 表名 where 条件;

-- 查看表的方式、显示表的创建语句与查看库的方式类似
show tables;
show tables like '_l%';
show create table class;

-- 显示表结构：即显示表中所包含的字段信息（名字、类型、属性等）
describe class;
desc class;
show columns from class;

-- 设置表选项：
-- 其设置方法与库属性的设置方法类似
alter table class charset gb2312;

-- 修改表名字：和库不同表的名字是可以改的
-- 基本语法：rename table 旧表名 to 新表名;
rename table class to student;

-- 为已创建好的表添加新字段：
-- 基本语法：alter table 表名 add column 字段名 字段类型 位置(first/after字段名);
alter table student add age int unsigned;
-- (column可有可无)新增字段默认是加到表的最后
-- 在int字段类型后添加unsigned可以使当前字段存储的数据没有负数
-- 添加zerofill可以自动用0填充长度（添加了zerofill就会开启unsigned）

-- 修改字段名：
-- 基本语法：alter table 表名 change 旧字段名 新字段名 字段类型 [位置];
alter table student change id num int first;

-- 修改字段类型：(可以用来修改字段位置)
-- 基本语法：alter table 表名 modify 字段名 新类型 [新位置];
alter table student modify age int(2) after name;

-- 删除字段：
-- 基本语法：alter table 表名 drop 字段名;
alter table student drop age;

-- 删除表：与删除库类似可同时删除多个表
drop table teacher, student;

-- 将数据插入到表中：
-- 基本语法：insert into 表名[(字段列表)] value('数据')(数据要对应字段列表);
insert into student (id,name,age,gender) value('1','Tom','13',1);

-- 表中数据查询操作：
-- 查询表中全部数据：select * from 表名;
select * from student;
-- 查询表中部分字段：select 字段列表 from 表名;
select name,age from student;
-- 简单条间查询数据：select 字段列表/* from 表名 where 字段名=值
select name from student where age=15; -- 获取年龄为15的人的名字

-- 数据删除操作：
-- 基本语法：delete from 表名 [where 条件]; 如果没有where条件，则删除整个表
delete from student where age=15; -- 删除student表中age=15的全部数据

-- 更新操作：通常用于修改部分字段数据
-- 基本语法：update 表名 set 字段名=新值[where 条件];如果没有where条件，则该字段所有数据都会被统一
update student set name = 'Maya' where id=1

-- 其它：
set names 字符集; -- 用于设置MySQLD 的字符信息，使其与MySQL字符信息统一
show variables like 'character_set%'; -- 查看系统保存的三种关系处理的字符集
show variables like 'auto_increment%'; -- 查看自增长初始变量

-- 主键的操作：
-- 创建主键：create table 表名(id int primary key)charset utf8;
--           create table 表名(id int,primary key(id))charset utf8;
--           alter table 表名 add primary key(字段名)；
-- 删除主键：alter table 表名 drop primary key;

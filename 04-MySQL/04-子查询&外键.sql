-- 子查询：sub query 当一个查询是另一个查询的条件时，称为子查询
-- 它是select sql语言中嵌套查询下层的程序模块
-- 子查询与主查询的关系：子查询是嵌入到主查询中的

-- 子查询的分类（按功能）：
-- 1.标量子查询：子查询得到的结果是一个数据（一行一列）
-- 基本语法：select * from 数据源 where 条件判断 =/<>(select 字段名 from 数据源 where 条件判断);

-- 2.列子查询：子查询得到的是一列数据（一列多行）
-- 基本语法：主查询 where 条件 in（列子查询）;

-- 3.行子查询：子查询得到的结果是一行多列
-- 基本语法：主查询 where 条件[(多个字段)] = （行子查询）
select * from student where (stu_age,stu_height) = (select max(stu_age),max(stu_height)from student);

-- 4.表子查询：子查询得到的结果是多行多列（属于from子查询）
-- 基本语法：select 字段表 from 表子查询) as 别名;
select * from (select * from student order by age desc) as a group by class_id;

-- 5.exists子查询：查询返回的结果只有0或1，1代表成立
-- 基本语法：where exists（查询语句）; exists 就是根据查询的结果进行判断，如果结果存在就返回1
-- where 1 ：永远为真


-- 子查询中特定关键字：
-- in：主查询 where 条件 in(列子查询)

-- any：任意一个。 =any(列子查询)：条件在查询结果中有任意一个匹配即可，等价于in
-- <>any(列子查询)：条件在查询结果中不等于任意一个，只要有不等于的情况即为true

-- some：与any完全一样

-- all：=all(列子查询)：等于里面所有
-- <>all(列子查询)：不等于其中所有

--===================================================================
-- 外键：如果公共关键字在一个关系中是主关键字，则这个关键字被称为是另一个关系的外键
-- foreign key ：A表中有字段，其值指向B表的主键。B为主表，A为从表

-- 外键的操作：
-- 随表增加外键：创建表时在字段后增加[constraint`外键名`]foreign key (外键字段) references 主表(主键)
-- 表后增加：alter table 从表 add [constraint`外键名`] foreign key (外键字段)  references 主表(主键)
-- 删除外键：alter table 从表 drop foreign key `外键名`
-- 外键删除后，其索引仍然存在
-- 删除索引：alter table 表名 drop index 索引名字

-- 外键基本要求：
-- 1.外键字段需要保证与关联的主表的主键字段类型完全一致
-- 2.基本属性也要相同
-- 3.若是在表后添加外键，从表的数据要与主表有一定的关联关系
-- 4.外键只能使用innodb存储引擎

-- 外键约束：
-- 通过建立外键关系后，对主表和从表都会有一定的数据约束
-- 约束：从表不能插入主表不存在的数据、主表不能删除一个被从表引入的数据
-- 可以在创建外键的时候，对外键约束进行选择性地操作
-- 基本语法：add foreign key(外键字段) references 主表(主键)on 约束模式
-- 约束模式有三种：
-- 1.district(严格模式)默认。不允许操作
-- 2.cascade（级联模式）一起操作。主表变化，从表数据就跟着变化
-- 3.set null（置空模式）主表删除，从表对应记录就为空。（前提 从表中对应外键字段允许为空）
-- 外键约束主要约束的对象是主表操作，从表只是不能插入主表不存在的数据
-- 常用约束模式有：on update cascade ， on delete set null（更新级联，删除置空）
alter table my_student add foreign key (class_id) references my_class(class_id)
on update cascade on delete set null; -- 多个条件空格隔开

--==================================================================
-- 创建视图(虚拟表)：create view 视图名字 as select指令
create view student_class_v as select * from student left join class on student.id = class.id;
-- 查看视图：所有查看表的方式都可以查看视图
-- 修改视图：alter view 视图名字 as 新的select语句
-- 删除视图：drop view 视图名字

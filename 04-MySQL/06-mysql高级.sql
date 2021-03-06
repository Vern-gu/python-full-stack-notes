-- 系统变量：所有用户（客户端）都有效
-- 查看所有系统变量：show variables [like'pattern'];
-- 查询变量数据值：select @@变量名;
-- 局部修改系统变量：set 变量名 = 新值;
-- 全局修改系统变量：set global 变量名 = 值;  或者 set @@global.变量名 = 值;
-- 全局修改只针对新客户端生效，已连接的客户端无效

-- 会话变量：即用户变量，只对当前用户使用的客户端生效
-- 定义用户变量：set @变量名 = 值;
-- mysql中专有的赋值符号为 ':=' ；比较仍用 '='
-- 将数据赋予变量：select @变量1:=字段1,@变量2:=字段2...from 数据表 where 条件;
-- 只赋值，不看过程：select 字段1,字段2...from 数据源 where 条件 into @变量1,变量2...;
-- 查看会话变量：select @变量名;

-- 局部变量：使用declare关键字声明，出现位置一定在begin和end之间
-- 局部变量声明语法：declare 变量名 数据类型 [字段属性];

--======================================================================
-- 流程结构：代码的执行顺序
-- if分支：
-- 用在select查询中，当作一种条件来判断:if(条件,真结果,假结果)
select *,if(age>12,'符合','不符合')as judge from student;
-- 用在复杂的语句块中（函数/存储过程/触发器）
if 条件表达式 then
    满足条件要执行的语句;
else
    不满足条件要执行的语句;
end if;

-- while 循环
标识名字 while 条件 do
    if 条件判断 then
        要循环执行的代码;
        iterate/leave 标识名字;
    end if;
end while;

--======================================================================
-- 函数：分内置函数和用户自定义函数 select 函数名(参数列表)
-- 字符串函数：
-- char_length()判断字符串的字符数
-- concat()连接字符串
-- instr()判断字符在字符串中是否存在，存在返回其位置，否则0
-- lcase()全部小写
-- left()从左侧截取到指定位置的字符串
-- ltrim()消除左边对应的空格
-- mid()从中间指定位置开始截取，若不指定长度，则直接到最后

-- 时间函数：
-- now()返回当前时间（格式：日期 时间）
-- curdate()返回当前日期
-- curtime()返回当前时间
-- datediff()判断两个日期之间的天数差距，参数日期需使用字符串格式（引号'1990-12-10'）
-- date_add(日期,interval 时间数字 type)进行时间的增加（type:day/hour/minute/second）
-- unix_timestamp()获取时间戳
-- from_unixtime()将指定时间戳转换成对应的日期时间格式

-- 数学函数：
-- abs()绝对值
-- ceiling()向上取整
-- floor()向下取整
-- pow()求指数，谁的多少次方 pow(2,4)二的四次方
-- rand()获取一个随机数（0-1之间）
-- round()四舍五入函数

-- 其他函数：
-- md5()对数据进行gmd5加密
-- version()获取版本号
-- databse()显示当前所在数据库
-- uuid()生成一个唯一标识符（类似自增长）（但他是空间唯一数据）

--====================================================================
-- 自定义函数：
-- 修改临时语句结束符：delimiter 新符号（如$$），最后用delimiter;修改回原来的结束符
-- 创建函数：包含function关键字，函数名，参数（形参和实参[可选]），确认函数返回值
-- 函数体，返回值
修改语句结束符
create function 函数名(形参)returns 返回值类型
begin
    函数体
    return 返回值数据;  -- 返回数据必须与结构中定义的返回值类型一致
end
修改语句结束符（改回来）

-- 形参：需要为函数的形参指定数据类型
-- 基本语法：变量名 字段类型

-- 查看函数：show function status [like'pattern'];
-- 查看函数的创建语句：show create function 函数名字;
-- 调用函数：select 函数名(参数列表);
-- 删除函数：drop function 函数名;

-- 自定义函数属于用户级别，只有当前客户端对应的数据库中可以使用
-- 可以在不同的数据库下看到对应的函数，但是不可以使用
-- 自定义函数通常是为了将多行代码集合到一起解决一个重复性问题
-- 在函数内部不能使用select指令，除了select赋值变量

-- 从1一直加到用户输入的数，跳过5的倍数
delimiter $$
create function my_sum(num int) returns int
begin
    declare res int default 0;  -- 声明局部变量
    declare i int default 1;
    my_while:while i <= num do
        if i % 5 <> 0 then
            set res = res + i;
            iterate my_while;  -- 类似于continue，让if执行完毕后继续执行while
        end if;
        set i  = i + 1;
    end while my_while;
    return res;  -- mysql函数一定要有返回值
end
$$
delimiter ;
select my_sum(100);

--====================================================================
-- 变量作用域：
-- 局部作用域：使用declare关键字声明（函数/存储过程/触发器），只能在结构中使用
-- 会话作用域：用户定义的的，使用@符号定义的变量，使用set关键字，当前用户当前的登陆有效
-- 全局作用域：所有连接所有客户端都有效，但一般不会使用自定义变量来控制全局

--====================================================================
-- 存储过程：完成特定功能的sql语句集，经过第一次编译后再次调用就不需要编译（效率较高）
-- 过程与函数的不同点：
-- 函数标识符为function，过程为procedure
-- 函数必须有返回值，过程没有返回值
-- 过程没有返回值类型
-- 函数是使用select调用，而过程不是

-- 创建存储过程：
create procedure 过程名字([参数列表])  mypro(in int_1 int, out int_2 int, inout int_3 int)
begin
    过程体
end
结束符

-- 查看过程：
show procedure status [like 'pattern'];
show create  procedure 过程名
-- 调用过程：call 过程名([实参])
-- 删除过程：drop procedure 过程名

-- 过程的参数类型：
-- in  表示参数从外部传入到里面使用（过程中使用），可以实是直接数据，也可以是变量
-- out  表示参数是从过程里面把数据保存到变量中，交给外部使用，传入的必须是变量（若变量有值，则会先被清空）
-- inout  数据可以从外部传入到过程内部使用，同时内部操作以后，又会将数据返还给外部
-- out、inout类型在结束过程后会把过程中处理后形参的值还给变量

--====================================================================
-- 触发器（trigger）：是一种特殊类型的存储过程，主要是通过事件进行触发而被执行的
-- 优点：如果某张表的数据改变，可以利用触发器来实现其它表的无痕操作（用户无法得知）
-- 保证数据安全
-- 缺点：过分依赖触发器，会影响数据库的结构，增加维护的复杂程度

-- 创建触发器：
create trigger 触发器名字 触发时机 触发事件 on 表 for each row
begin

end

-- 触发时机：
-- before 表中数据发生改变前的状态
-- after 表中数据已经发生改变后的状态
-- 触发事件：insert、update、delete
-- 每一张表中，每一个触发时机绑定的触发事件对应的触发器类型只能有一个
-- 换言之一张表中只能最多有六个触发器

-- 查看触发器：show triggers;
-- 查看触发器创建语句：show create trigger 触发器名字
-- 删除触发器：drop trigger 触发器名字;

-- 记录关键字：old、new
-- 触发器在执行之前就可以获得数据操作前后的一个对应状态
-- 没有操作之前的状态（数据）保存到old关键字中，操作后的状态都在new中
-- 基本语法：关键字.字段名
-- insert插入前全为空，没有old、、delete清空数据，没有new


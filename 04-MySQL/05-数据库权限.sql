-- 数据库备份：
-- 基本语法：mysqldump -hPup 数据库名字[表1[表2...]] > 备份文件地址
-- 可选择整库备份或者单表/多表备份
mysqldump -hlocalhost -P3306 -uroot -p school > D:/newfolder/school.sql

-- 数据库的还原：（必须指定数据库）
-- 1.登陆之前利用MySQL客户端还原
-- 基本语法：mysql -hPup 数据库 < 文件位置
-- 2.提供了一种导入sql指令的方式
-- 基本语法：source sql文件位置

-- 数据导入：把文件系统数据导入到数据库中，(ubuntu)先将文件放入MySQL搜索路径/var/lib/mysql-files/
load data infile '绝对路径' into table '表名' fields terminated by '分隔符' lines terminated by '\n';
-- 数据导出：将数据表记录保存到系统文件里(ubuntu)只能保存到搜索路径中
select ... from 表名 where 条件 into outfile '绝对路径' fields terminated by '分隔符' lines terminated by '\n';

--====================================================================
-- 用户权限管理：
-- 权限分为:
-- 数据权限（增删改查select,add,delete,update）
-- 结构权限（create、drop）
-- 管理权限（create/drop user, grant, revoke等）
-- 创建用户：create user 用户@host identified by '明文密码';
-- 用户：用户名@主机地址    主机地址可以为空'' 或者使用'%'
-- 删除用户：drop user 用户@host;
-- 修改用户密码：set password for 用户@host = '新明文密码'; （MySQL8）8以下版本需要password()函数
-- alter user 用户名@host identified by '密码';

-- 授予权限（grant）：将权限分配给指定的用户
-- 基本语法：grant 权限列表 on 数据库/*.表/* to 用户; (*.*代表整个数据库)
-- 权限列表用逗号分隔，也可用all privileges代表全部权限
grant select,delete on school.test to 'Nya'@'%';
-- 取消权限（revoke）：将权限从用户手中回收
-- 基本语法：revoke 权限列表 on 数据库.表 from 用户
revoke delete on school.test from 'Nya'@'%';
-- 刷新权限(flush)：将当前对用户的权限操作进行刷新，使其立即生效
-- 基本语法： flush privileges

-- root密码找回（MySQL8以前版本可用）
-- 1.停止服务
-- 2.重启服务：mysqld.exe --skip-grant-tables (跳过权限启动服务)
-- 3.mysql直接连接数据库，使用修改密码的指令

--===================================================================
-- 事务：访问并可能更新数据库中各种数据项的一个程序执行单元
-- 自动事务一般是开启的，可以通过 set autocommit = off 关闭
-- 自动事务关闭后由用户决定commit（提交）或rollback（撤销）
commit;  rollback;

-- 开启事务：start transaction;/begin;
-- 这条语句后的所有sql指令都不会自动提交

-- 回滚点：savepoint 回滚点名字 （相当于存档点）
-- rollback to 回滚点名字 （回滚点之后的操作撤销）
-- 在事务处理中如果有多个步骤可以设置多个回滚点（新回滚点覆盖旧的）

-- 事务特点：原子性（不可分割）、一致性、隔离性、持久性

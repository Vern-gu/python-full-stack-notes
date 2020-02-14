# MVC中有一个很重要的部分就是ORM
# ORM（对象-关系-映射）：实现了数据模型与数据库的解耦
# 根据对象的类型生成表结构
# 将对象、列表的操作转化为sql语句
# 将sql查询到的结果，转化为对象、列表


# python manage.py startapp model
# 添加模型加入settings中的app字典
# 在models.py中定义属性，会生成表中的字段
# django中的模型所提供的属性具有以下信息：
#       所定义的类属性决定了字段的属性
#       所定义的类属性还决定了默认的HTML控件
#       最低限度的验证，阻止非法信息
# django会为表增加自动增长的主键列（若用户自定义则django将不会再默认生成主键列）


# 在models.py中所定义的属性（字段类型）都在django.db.models.fields目录下
# 使用方法：
#       导入 from django.db import models
#       通过models.Field创建字段类型的对象赋值给属性
# 对于重要数据仅作逻辑删除，不作物理删除
# 逻辑删除：定义isDelete属性，类型为BooleanField，默认值为False


# 字段类型：
# AutoField：自增长，不指定时，django会自动添加一个自增长主键字段
# BooleanField：true/false
# NullBooleanField：null/true/false
# CharField(max_length=字符长度)：字符串
# TextField：大文本字段，一般超过4000时使用
# IntegerField：整数
# Decimal Field(max_digits=所有数字位数,decimal_places=小数位数)：十进制浮点数
# DateField(auto_now=False, auto_now_add=False)：日期，第一个参数自动设置修改时间，第二个参数自动设置创建时间
# TimeField：时间（同DateField）
# DateTimeField：日期时间（同Datefield）


# 字段选项：实现对字段的约束
# null：若为True则django将空值以NULL存储到数据库
# db_index：若值为True则会在表中为此字段添加索引
# default：默认值
# primary_key：若为True则该字段会成为模型的主键字段
# unique：若为True，这个字段在表中必须有唯一值


# 关系：(models对象方法)
# ForeignKey：一对多，将字段定义在多的一端中
# ManyToManyField：多对多，将字段定义在两端中
# OneToOneField：一对一，将字段定义在任意一端中


# 在模型类中还能再定义一个Meta类
# 主要用于设置表的元信息
# db_table = '表名'
# ordering = ['字段名']  按该字段值的大小排序，['-字段名']表示倒序排序


# 自定义管理器：管理器充当着ORM的重要角色
# 管理器是模型类的属性，用于将对象与数据表映射
# 将写的代码转化为sql语句
# django默认的管理器为objects
# 可以通过继承models.Manager类来实现自定义管理器
# 一个模型可以拥有多个管理器对象
# 管理器主要用于修改默认查询集的结果以及快速添加数据


# 查询集：表示从数据库中获取的对象集合
# 查询集可以含有多个过滤器
# 查询集可以看作是select语句，返回的列表
# 过滤器类似于where、limit子句，查询的方法
# all() 获取所有的数据
# filter()  获取满足条件的数据
# exclude()  获取不满足条件的数据
# order_by()  排序
# values()  对象构成字典，然后组合成列表返回
# filter(键1=值1，键2=值2)等价于filter(键1=值1).filter(键2=值2)

# get()  返回单个满足条件的对象（如果未找到或找到多条都会报错）
# count()  返回当前查询的总条数
# first()  返回第一个对象
# last()  返回最后一个对象
# dates('日期时间类型的字段名','year/month/day',order='DESC')
# dates方法会返回一个列表，列表中的元素为每一篇文章的创建时间，且是 Python 的 date 对象，精确到月份，降序排列
# exists()  判断查询集中是否有数据，如果有则返回True
# [0:1]  写在最后限制查询集相当于limit子句，limit 0,1(其实就是列表操作，但不支持负索引)
# 查询方法的使用：属性名__比较运算符=值
# contains包含、startswith开头、endswith结尾
# isnull、isnotnull 是否为空、in 范围查询
# title__contains='Fa'、id__in=[1,2,3]
# 在contains等前加一个‘i’筛选时就不区分大小写
# gt\gte\lt\lte  大于、大于等于、小于、小于等于

# 用aggregate()调用聚合函数:Avg\Max\Min\Sum（aggregate()方法一般放在最后使用）
# from django.db.models import *
# maxDate = list.aggregate(Max('pub_date'))

# F对象：可用于两个字段作比较(需要from django.db.models import F, Q)
# django还支持F()对象进行运算
# filter(read_qty__lte=F('comment_qty')*2)
# F()对象中还可以写作“模型类__列名”进行关联查询
# list.filter(isDelete=F('HeroInfo__isDelete'))

# 过滤器方法中多个关键字参数查询会合并为逻辑与(and)进行
# 而要实现逻辑或(or)，需要使用Q()对象
# list.filter(Q(pk__gte=4)|Q(pk__lt=2)  # '|' 换为'&'则实现逻辑与(and)

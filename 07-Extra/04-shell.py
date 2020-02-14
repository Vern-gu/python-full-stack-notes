# 在终端内输入多个命令的组合可称之为shell脚本
# linux终端下同时要执行多个命令可使用“;”隔开
# 在终端内敲下命令后，shell进程（父进程）会创建（exec）一个子进程，使其执行命令，而shell会进入后台等待子进程结束
# 当一个命令写在一个括号内时，说明这个命令仅在子进程中运行，且结果并不传递给父进程（shell本身）

# man bash-builtins 查看shell的内建命令（如：export，shift，if，eval，for，[，while等等）
# 执行内建命令不会创建新的子进程，但执行结束后也会生成一个状态码，可以用 $? 读出
# 若返回的状态码为0，则命令运行成功，否则即运行错误

# 可以创建一个后缀名为.sh的文件作为shell脚本文件
# 文件开头需要定义解释器：#! /bin/sh
# 创建完成的文件可以通过指定解释器来直接运行：/bin/sh test1.sh （通过此方法可以不需要文件的运行权限）
# source filename命令是简单地读取脚本里面的语句依次在当前shell里面执行，没有建立新的子shell \
# 脚本里面所有新建、改变变量的语句都会保存在当前shell里面（与 . filename等价）

# ==================================================================================================================

# shell变量由大写字母加下划线组成，可以分为环境变量和本地变量
# 环境变量可以由父进程传递给子进程，printenv命令可以显示当前shell进程的环境变量
# 本地变量只存在于当前shell进程，用set命令可以显示当前shell进程中定义的所有变量（包括本地和环境）和函数
# 通过 export 变量名  可以将一个本地变量变为环境变量（定义变量时等号左右两边不能有空格）
# 也可直接 export VAL=value 来直接定义一个环境变量
# unset 变量名 来删除一个环境或本地变量
# echo $SHELL 查看当前的shell类型
# 注意:定义变量时不需要加$ , 取变量值时需要在变量前加$，如：echo $VAL
# 一般给变量赋的值都是str类型，可使用算术代换$(())或$[]，其中的shell变量的取值将转换为整数（只能做加减乘除的整数运算）

# *匹配0个或多个任意字符；?匹配一个任意字符；[]匹配方括号中任意一个字符；\为转译字符
# 要将一个变量中的值赋给另一个变量，可使用命令代换：``或$()，如DATE=$(date)或DATE=`date`
# shell中的单引号是字符串的界定符号，单引号内保持所有字符的字面值（但不能出现单引号）
# 而双引号会将变量展开，不会取变量字面值，而是取到其变量的值

# ==================================================================================================================

# 条件测试：test或[ ，若测试的值为真则返回0，否则返回1
# -eq等于、-ne不等于、-lt小于、-gt大于、-le小于等于、-ge大于等于
# [ -d 目录 ] 判断目录是否为目录
# [ -f 文件 ] 判断文件是否为普通文件
# [ -z 字符串 ] 判断字符串长度是否为0
# [ -n 字符串 ] 判断字符串长度是否不为0
# [ 字符串1 = 字符串2 ] # 判断两个字符串是否相等
# [ ! EXPR ] !表示逻辑非
# [ EXPR1 -a EXPR2 ] -a表示逻辑与
# [ EXPR1 -o EXPR2 ] -o表示逻辑或

# if语句：后面可以跟测试语句，表判断
# if [ -d ./test.txt ]; then echo $?
"""
#! /bin/sh
echo 'Is it morning? Please enter yes or no.'
read YES_OR_NO
if [ "$YES_OR_NO" = 'yes']; then
    echo 'Good morning'
elif [ "$YES_OR_NO" = 'no']; then
    echo 'Good afternoon'
else
    echo "Sorry, %YES_OR_NO not recognized. Enter yes or no."
    exit 1
fi
exit 0
"""

# case/esac语句，类似于C语言的switch/case语句
# case可以匹配字符串和Wildcard，每个匹配分支可以有若干条命令，末尾必须以;;结尾，执行结束不需要用break跳出
"""
#! /bin/sh
echo 'Is it morning? Please enter yes or no.'
read YES_OR_NO
case $YES_OR_NO in yes|YES|y|Yes)
    echo 'Good morning!';;
[Nn]*)
    echo 'Good afternoon!';;
*)
    echo "Sorry, $YES_OR_NO is not recognized."
esac

"""
# for/do/done循环，类似于python的for循环：
"""
#! /bin/bash
for FRUIT in apple banana orange; do
    echo "I like $FRUIT"
done
"""
# while 循环：
"""
#! /bin/bash
echo "enter password:"
read TRY
while [ $TRY != 'secret' ]; do
    echo "Sorry,please try again."
    read TRY
done
"""
# 通过算术运算控制循环次数
"""
#! /bin/sh
COUNTER=0
while [ $COUNTER lt 10 ]; do
    echo $COUNTER
    COUNTER=$(($COUNTER+1))           变量的赋值时，等号左右不能加空格
"""

# ====================================================================================================================

# 位置参数和特殊变量
"""
$0      shell本身的文件名
$1~$n   添加到shell的各个参数值，$1是第一个参数...
$#      表示添加到Shell的参数个数
$$      shell本身的pid
$!      shell最后运行的后台process的pid
$?      最后运行的命令的结束代码（返回值）
$@      表示参数列表“$1、$2...”可用在for循环in后面（$*同理）
"""
# 位置参数可以用shift命令左移。比如shift 3表示原来的$4现在变成$1，原来的$5现在变成$2等等，原来的$1、$2、$3丢弃，$0不移动。

# echo主要用于显示文本行或变量，或者把字符串输入到文件
#    它有两个参数：-e：可以解析转义字符；-n：文本后不添加换行（默认情况是回显内容后自动换行）
# tee命令可以将一个结果输出到标准输出（默认），并创建另一个副本结果输出到相应的文件
# /dev/null Linux黑洞文件，不想看输出的文件都可以重定向到此文件中去，ls -l > /dev/null

# ====================================================================================================================

# shell函数中没有返回值，也没有参数列表(但是可以用上文讲到的特殊变量进行传递参数)
# foo(){ echo "Function foo is called";}
# 左大括号和后面的命令之间必须有空格或换行；最后一条命令和右大括号在同一行，则命令的末尾必须有分号
"""
#! /bin/sh

is_directory(){
    DIR_NAME=$1
    if [ ! -d $DIR_NAME ]; then
        return 1
    else
        return 0
    fi
}
for DIR in $@; do
    if is_directory $DIR
    then :
    # then之后直接空格冒号，表示啥都不执行
    else
        echo "$DIR is not exist. Creating it now..."
        mkdir "$DIR" > /dev/null 2>&1
        if [ $? -ne 0 ]; then
            echo "Cannot create directory $DIR"
            exit 1
        fi
    exit 0
    fi
done
"""

# ===================================================================================================================

# shell脚本调试：
# -n：读一遍脚本中的命令但不执行，用于检查脚本中的语法错误
# -v：一边执行脚本，一边将执行过的脚本命令打印到标准错误输出
# -x：提供跟踪执行信息，将执行的每一条命令和结果依次打印出来（局部调试）
# $ sh -n ./script.sh
# #! /bin/sh -x
# (在脚本中)set -x/+x


# 文件描述符0，1，2分别对应标准输入、输出、错误

# ===================================================================================================================
# 一些常见的linux命令：
# wc [option] [file]   -l 统计行数、-c统计字节数、-w统计单词数
# sort [option] file    对输出的字符进行排序
#   -f忽略字符大小写、-n比较数值大小、-t指定分隔符、-k指定分隔后进行比较字段、-u重复的行只显示一次
# uniq  移除重复的行  -c、显示每行重复的次数、-d仅显示重复过的行、-u仅显示不重复的行

# ===================================================================================================================
# 开机自启脚本的创建
# 将启动脚本复制或软连接到/etc/init.d/目录下
# 设置脚本文件的权限  sudo chmod 755 文件名
# 执行如下命令将脚本放入启动脚本中
# cd /etc/init.d/
# update-rc.d 文件名 default 99  (99表示启动顺序，数字越大越靠后启动)

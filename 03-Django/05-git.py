# Git是分布式版本控制系统
# 安装：sudo apt-get install git
# git config --global user.name '' 更改名字及邮箱
# git config --global user.email 12@163.com


# 将github上的项目克隆到本地一份：
# git clone git@github:账号名/项目名.git

# 从远程库获取到本地：git pull
# 将本地提交到远程库：git push origin master
# 每次提交前，需要先获取，解决冲突后再次提交

# git init 创建本地仓库
# git add ./（文件名）  将当前目录的文件放入暂存区
# git commit -m '备注信息'  将暂存区内的文件放入仓库区

# git log 查看更改的历史纪录
# git log --pretty=oneline 简略显示记录

# git reset HEAD^  从仓库取回上一个版本的文件放入暂存区（HEAD~100 表示从新到旧的第100个文件）
# git checkout 文件名  将暂存区的文件拉回工作区重新编辑

# 树的概念：一种抽象数据类型，它是由n（n>=1）个有限节点组成一个具有层次关系的集合。
# 特点：每个节点有零个或多个子节点；
#     没有父节点的节点称为根节点；
#     每一个非根节点有且只有一个父节点；
#     除了根节点外，每个子节点可以分为多个不相交的子树；

# 节点的度：一个节点含有的子树的个数称为节点的度
# 树的度：树中，最大的节点的度
# 节点的层次：从根开始定义，根为第一层，以此类推
# 树的高度：树种节点的最大层次

# 二叉树：每个节点最多有两个子树的树结构，子树被称为左子树和右子树
# 二叉树的性质(特性)
# 性质1: 在二叉树的第i层上至多有2^(i-1)个结点（i>0）
# 性质2: 深度为k的二叉树至多有2^k - 1个结点（k>0）
# 性质3: 对于任意一棵二叉树，如果其叶结点数为N0，而度数为2的结点总数为N2，则N0=N2+1;
# 性质4:具有n个结点的完全二叉树的深度必为 log2(n+1)
# 性质5:对完全二叉树，若从上至下、从左至右编号，则编号为i 的结点，其左孩子编号必为2i，
#      其右孩子编号必为2i＋1；其双亲的编号必为i/2（i＝1 时为根,除外）


# 二叉树的实现：
class Node:
    """树的节点"""
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree:
    """二叉树"""
    def __init__(self):
        self.root = None
    def add(self,item):
        """树的添加元素"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]  # 使用队列的模式
        while queue:  # 只要队列不为空就一直可以循环
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    def breadth_travel(self):
        """树的广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            elif cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    def preorder(self,node):  # 深度优先遍历，分为先序、中序、后序
        """前序遍历"""        # 根-左-右
        if node is None:
            return
        print(node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    def inorder(self,node):  # 左-根-右
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem)
        self.inorder(node.rchild)
    def postorder(self,node):  # 左-右-根
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem)


tree = Tree()


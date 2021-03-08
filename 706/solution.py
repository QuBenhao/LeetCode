import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, values = test_input
        # Your MyHashMap object will be instantiated and called as such:
        obj = MyHashMap()
        ans = [None]
        for i in range(1, len(ops)):
            if ops[i] == "put":
                obj.put(values[i][0], values[i][1])
                ans.append(None)
            elif ops[i] == "get":
                ans.append(obj.get(values[i][0]))
            else:
                obj.remove(values[i][0])
                ans.append(None)
        return ans


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_key = 2069
        self.hash_table = [None] * self.hash_key

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        k = key % self.hash_key
        if not self.hash_table[k]:
            self.hash_table[k] = BinarySearchTree()
        self.hash_table[k].put(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        k = key % self.hash_key
        if not self.hash_table[k]:
            return -1
        value = self.hash_table[k].get(key)
        return value if value is not None else -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        k = key % self.hash_key
        if self.hash_table[k]:
            try:
                self.hash_table[k].delete(key)
            except:
                pass


class TreeNode(object):
    # 初始化树的节点
    def __init__(self, key, val, left=None, right=None, parent=None, balanceFactor=0):
        self.key = key  # 节点值，节点位置，索引
        self.payload = val  # 有效载荷，节点显示的值
        self.leftChild = left  # 左子节点
        self.rightChild = right  # 右子节点
        self.parent = parent  # 父节点
        self.balanceFactor = balanceFactor  # 节点的平衡因子

    # 判断是否有左子节点，若有则返回左子节点
    def hasLeftChild(self):
        return self.leftChild

    # 判断是否有右子节点，若有则返回右子节点
    def hasRightChild(self):
        return self.rightChild

    # 判断是否是左子节点(父节点存在，并且self与self父节点的左子节点相同)
    def isLeftChild(self):
        # 下面的含义是(self.parent is not None) and (self.parent.leftChild == self)
        return self.parent and self.parent.leftChild == self

    # 判断是否是右子节点
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    # 判断是否是根节点
    def isRoot(self):
        return not self.parent  # 没有父节点

    # 判断是否是叶节点
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)  # 没有左右子节点

    # 判断是否有子节点
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild  # 有左或右子节点

    # 判断是否有2个子节点
    def hasBothChildren(self):
        return self.rightChild and self.leftChild  # 有左右2个子节点

    # 替换节点数据
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key  # 更新节点值
        self.payload = value  # 更新有效载荷
        self.leftChild = lc  # 更新左子节点
        self.rightChild = rc  # 更新右子节点
        if self.hasLeftChild():  # 若有左子节点
            self.leftChild.parent = self  # 将该节点的左子节点的父节点指向self
        if self.hasRightChild():  # 若有右子节点
            self.rightChild.parent = self  # 将该节点的右子节点的父节点指向self

    # 中序遍历
    # 只要用了yield语句，普通函数就是生成器，也是迭代器，在定义过程中不需要像迭代器那样写__iter__()和__next__()方法。
    # yield语句的作用就是在调用的时候返回相应的值和作为生成器的标志。
    def __iter__(self):
        if self:  # 若当前节点存在，则
            if self.hasLeftChild():  # 若当前节点有左子节点，则
                for elem in self.leftChild:  # 循环输出当前节点的左子树的节点值
                    yield elem  # 在for循环中，每次执行到yield时，就返回一个迭代值，且不会终止循环；
                    # 下个循环时，代码从yield返回值的下一行继续返回
            yield self.key  # 返回当前节点值
            if self.hasRightChild():  # 若当前节点有右子节点，则
                for elem in self.rightChild:  # 循环输出当前节点的右子树的节点值
                    yield elem

    # 将被删除节点的继任者拼接到被删除的节点位置
    def spliceOut(self):
        if self.isLeaf():  # 若被删除节点是叶节点，则无需再拼接
            if self.isLeftChild():  # 若被删除节点是父节点的左子节点，则
                self.parent.leftChild = None  # 被删除节点为None，无需再拼接
            else:  # 若被删除节点是父节点的右子节点，则
                self.parent.rightChild = None  # 被删除节点为None，无需再拼接
        elif self.hasAnyChildren():  # 若被删除节点有子节点，则
            if self.hasLeftChild():  # 若被删除节点有左子节点，则
                if self.isLeftChild():  # 若被删除节点是左子节点，则
                    # 将被删除节点的父节点的左子节点指向被删除节点的左子节点
                    self.parent.leftChild = self.leftChild
                else:  # 若被删除节点是右子节点，则
                    # 将被删除节点的父节点的右子节点指向被删除节点的左子节点
                    self.parent.rightChild = self.leftChild
                # 将被删除节点的左子节点的父节点指向被删除节点的父节点
                self.leftChild.parent = self.parent
            else:  # 若被删除节点没有左子节点，则被删除节点有右子节点
                if self.isLeftChild():  # 若被删除节点是左子节点，则
                    # 将被删除节点的父节点的左子节点指向被删除节点的右子节点
                    self.parent.leftChild = self.rightChild
                else:  # 若被删除节点是右子节点，则
                    # 将被删除节点的父节点的右子节点指向被删除节点的右子节点
                    self.parent.rightChild = self.rightChild
                # 将被删除节点的右子节点的父节点指向被删除节点的父节点
                self.rightChild.parent = self.parent

    # 查找被删除节点的继任者，继任者节点最多只能有一个子节点
    def findSuccessor(self):
        succ = None  # 初始化被删除节点的继任者为None
        if self.hasRightChild():  # 若被删除节点有右子节点，则
            succ = self.rightChild.findMin()  # 获取被删除节点的右子树中的最小节点作为继任者
        else:  # 若被删除节点没有右子节点，则
            if self.parent:  # 若被删除节点有父节点，则
                if self.isLeftChild():  # 若被删除节点是父节点的左子节点，则
                    succ = self.parent  # 被删除节点的父节点是继任者
                else:  # 若被删除节点是父节点的右子节点，则被删除节点的继任者是其父节点的继任者，不会是被删除节点
                    self.parent.rightChild = None  # 暂时将None赋值给被删除节点，则继任者不会是被删除节点，方便下一行递归查找
                    succ = self.parent.findSuccessor()  # 将被删除节点的父节点的继任者作为继任者
                    self.parent.rightChild = self  # 获得继任者后，重新将被删除节点赋值给自己，以免被删除节点为None扰乱树结构
        return succ

    # 查找当前树的最小子节点，因此例是BST搜索树，左子节点的值是最小的，所以只找左子节点
    def findMin(self):
        current = self  # 将自身设置为当前节点
        while current.hasLeftChild():  # 若当前节点有左子节点，则循环
            current = current.leftChild  # 将当前节点的左子节点作为下一个当前节点
        return current  # 返回最终左子节点，即此树中的最小节点


# 二叉查找树类(此例为BST搜索树类)
class BinarySearchTree(object):
    # 初始化空二叉树
    def __init__(self):
        self.root = None
        self.size = 0

    # 获取树的大小
    def length(self):
        return self.size

    # 通过__len__方法使用len()
    def __len__(self):
        return self.size

    # 实现了__iter__方法的对象就是可迭代对象，__iter__覆盖for x in操作，因此它是递归的！
    # 因它是在TreeNode实例上递归的，所以__iter__方法在TreeNode类中定义
    def __iter__(self):
        return self.root.__iter__()  # 返回二叉查找树根节点的迭代，即遍历二叉查找树

    # 创建二叉搜索树
    def put(self, key, val):
        if self.root:  # 若树已经有根节点，则
            self._put(key, val, self.root)  # 从树的根开始，搜索二叉树
        else:  # 若树没有根节点，则
            self.root = TreeNode(key, val)  # 创建一个新的TreeNode并把它作为树的根节点
        self.size = self.size + 1  # 增加树的大小

    # 搜索树，put()的辅助函数
    def _put(self, key, val, currentNode):
        if key < currentNode.key:  # 若新的键值小于当前节点键值，则搜索左子树
            if currentNode.hasLeftChild():  # 若当前节点有左子树要搜索，则
                self._put(key, val, currentNode.leftChild)  # 递归搜索左子树
            else:  # 若当前节点无左子树要搜索，则
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                # 创建一个新的TreeNode并把它作为当前节点的左子节点
                self.updateBalance(currentNode.leftChild)  # 更新当前节点的左子节点的平衡因子
        elif key == currentNode.key:  # 若新的键值=当前节点键值，则
            currentNode.payload = val  # 更新当前节点的有效载荷
            self.size = self.size - 1  # 由于只修改，未增加，又因put()中+1，所以此处-1
        else:  # 若新的键值>=当前节点键值，则搜索右子树
            if currentNode.hasRightChild():  # 若当前节点有右子树要搜索，则
                self._put(key, val, currentNode.rightChild)  # 递归搜索右子树
            else:  # 若当前节点无右子树要搜索，则
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                # 创建一个新的TreeNode并把它作为当前节点的右子节点
                self.updateBalance(currentNode.rightChild)  # 更新当前节点的右子节点的平衡因子

    # 更新平衡因子
    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:  # 若节点的平衡因子不是-1、0、1，则
            self.rebalance(node)  # 该节点再平衡
            return
        if node.parent is not None:  # 若该节点有父节点，即该节点不是根节点，则
            if node.isLeftChild():  # 若该节点是左子节点，则
                node.parent.balanceFactor += 1  # 该节点的父节点的平衡因子+1
            elif node.isRightChild():  # 若该节点是右子节点，则
                node.parent.balanceFactor -= 1  # 该节点的父节点的平衡因子-1
            if node.parent.balanceFactor != 0:  # 若该节点的父节点的平衡因子不为0，则
                self.updateBalance(node.parent)  # 更新该节点的父节点的平衡因子

    # 左旋转（右重的树要左旋转才平衡）
    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild  # 待旋转节点的右子节点设为新的根节点
        rotRoot.rightChild = newRoot.leftChild  # 新根的原左子节点作为原根的新右子节点
        if newRoot.leftChild is not None:  # 若新根原来有左子节点，则
            newRoot.leftChild.parent = rotRoot  # 将新根的原左子节点的父节点指向原根
        newRoot.parent = rotRoot.parent  # 新根的父节点指向原根的父节点
        if rotRoot.isRoot():  # 若原根是树的根节点，则
            self.root = newRoot  # 将新根设为树的根节点
        else:  # 若原根不是树的根节点，则
            if rotRoot.isLeftChild():  # 若原根是左子树，则
                rotRoot.parent.leftChild = newRoot  # 将原根的父节点的左子节点指向新根
            else:  # 若原根是右子树，则
                rotRoot.parent.rightChild = newRoot  # 将原根的父节点的右子节点指向新根
        newRoot.leftChild = rotRoot  # 将新根的左子节点指向原根
        rotRoot.parent = newRoot  # 将原根的父节点指向新根
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor,0)
        # 更新原根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响，计算方法见上方注释
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)
        # 更新新根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响，计算方法见上方注释

    # 右旋转（左重的树要右旋转才平衡）
    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild  # 待旋转节点的左子节点设为新的根节点
        rotRoot.leftChild = newRoot.rightChild  # 新根的原右子节点作为原根的新左子节点
        if newRoot.rightChild is not None:  # 若新根原来有右子节点，则
            newRoot.rightChild.parent = rotRoot  # 将新根的原右子节点的父节点指向原根
        newRoot.parent = rotRoot.parent  # 新根的父节点指向原根的父节点
        if rotRoot.isRoot():  # 若原根是树的根节点，则
            self.root = newRoot  # 将新根设为树的根节点
        else:  # 若原根不是树的根节点，则
            if rotRoot.isLeftChild():  # 若原根是左子树，则
                rotRoot.parent.leftChild = newRoot  # 将原根的父节点的左子节点指向新根
            else:  # 若原根是右子树，则
                rotRoot.parent.rightChild = newRoot  # 将原根的父节点的右子节点指向新根
        newRoot.rightChild = rotRoot  # 将新根的右子节点指向原根
        rotRoot.parent = newRoot  # 将原根的父节点指向新根
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        # 更新原根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响，计算方法见上方注释
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(0,rotRoot.balanceFactor)
        # 更新新根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响，计算方法见上方注释

    # 再平衡
    def rebalance(self, node):
        if node.balanceFactor < 0:  # 若该节点的平衡因子<0，则
            if node.rightChild.balanceFactor > 0:  # 若该节点的右子节点的平衡因子>0，则
                self.rotateRight(node.rightChild)  # 右旋转该节点的右子节点
            self.rotateLeft(node)  # 左旋转该节点
        elif node.balanceFactor > 0:  # 若该节点的平衡因子>0，则
            if node.leftChild.balanceFactor < 0:  # 若该节点的左子节点的平衡因子<0，则
                self.rotateLeft(node.leftChild)  # 左旋转该节点的左子节点
            self.rotateRight(node)  # 右旋转该节点

    # 通过__setitem__方法使用mytree[3]="red"方式，否则只能用put()方法
    def __setitem__(self, k, v):
        self.put(k, v)

    # 根据索引key获取其对应的节点值
    def get(self, key):
        if self.root:  # 若树已经有根节点，则
            res = self._get(key, self.root)  # 从树的根开始，搜索二叉树
            if res:  # 若搜索到了，则
                return res.payload  # 返回存储在节点的有效载荷中的值，即节点显示的值
            else:  # 若没搜索到，则没有该索引对应的节点
                return None
        else:  # 若树没有根节点，则说明是空二叉树
            return None

    # 搜索树，get()的辅助函数
    def _get(self, key, currentNode):
        if not currentNode:  # 若没有当前节点，则返回None
            return None
        elif currentNode.key == key:  # 若当前节点的位置和待查找的位置相同，则
            return currentNode  # 返回当前节点的值
        elif key < currentNode.key:  # 若当前节点的位置>待查找的位置，则
            return self._get(key, currentNode.leftChild)  # 递归查找当前节点的左子树
        else:  # 若当前节点的位置<=待查找的位置，则
            return self._get(key, currentNode.rightChild)  # 递归查找当前节点的右子树

    # 通过__getitem__方法使用mytree[3]获取值的方式，否则只能用get()方法
    def __getitem__(self, key):
        return self.get(key)

    # 通过__contains__方法使用in方法
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    # 根据索引key删除其对应的节点
    def delete(self, key):
        if self.size > 1:  # 若树的大小>1，则
            nodeToRemove = self._get(key, self.root)  # 获取要删除的节点
            if nodeToRemove:  # 若该节点存在，则
                self.remove(nodeToRemove)  # 删除该节点
                self.size = self.size - 1  # 树的大小减1
            else:  # 若该节点不存在，则
                raise KeyError('错误，键值不在树中')  # 报错
        elif self.size == 1 and self.root.key == key:  # 若树的大小为1，且要删除的是根，则
            self.root = None  # 根节点为None
            self.size = self.size - 1  # 树的大小减1
        else:  # 若树的大小为0，则为空树
            raise KeyError('错误，键值不在树中')  # 报错

    # 通过__delitem__方法使用del方法
    def __delitem__(self, key):
        self.delete(key)

    # 删除节点
    def remove(self, currentNode):
        if currentNode.isLeaf():  # 若被删除节点是叶节点，则没有子节点
            if currentNode == currentNode.parent.leftChild:  # 若被删除节点是其父节点的左子节点，则
                currentNode.parent.leftChild = None  # 被删除节点为None
            else:  # 若被删除节点是其父节点的右子节点，则
                currentNode.parent.rightChild = None  # 被删除节点为None
        elif currentNode.hasBothChildren():  # 若被删除节点有2个子节点，则
            succ = currentNode.findSuccessor()  # 获取被删除节点的继任者(防止树结构混乱)
            succ.spliceOut()  # 将被删除节点的继任者拼接到被删除节点位置
            currentNode.key = succ.key  # 将被删除节点位置的值设置为继任者的值
            currentNode.payload = succ.payload  # 将被删除节点的有效载荷设置为继任者的有效载荷
        else:  # 若被删除节点只有1个子节点，则
            if currentNode.hasLeftChild():  # 若被删除节点只有左子节点，则
                if currentNode.isLeftChild():  # 若被删除节点是左子节点，则
                    # 将被删除节点的左子节点的父节点指向被删除节点的父节点
                    currentNode.leftChild.parent = currentNode.parent
                    # 将被删除节点的父节点的左子节点指向被删除节点的左子节点
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():  # 若被删除节点是右子节点，则
                    # 将被删除节点的左子节点的父节点指向被删除节点的父节点
                    currentNode.leftChild.parent = currentNode.parent
                    # 将被删除节点的父节点的右子节点指向被删除节点的左子节点
                    currentNode.parent.rightChild = currentNode.leftChild
                else:  # 若被删除节点无父节点，则被删除节点为根节点
                    # 替换被删除节点的左子节点的键、有效载荷、左子节点和右子节点数据
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
            else:  # 若被删除节点只有右子节点，则
                if currentNode.isLeftChild():  # 若被删除节点是左子节点，则
                    # 将被删除节点的右子节点的父节点指向被删除节点的父节点
                    currentNode.rightChild.parent = currentNode.parent
                    # 将被删除节点的父节点的左子节点指向被删除节点的右子节点
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():  # 若被删除节点是右子节点，则
                    # 将被删除节点的右子节点的父节点指向被删除节点的父节点
                    currentNode.rightChild.parent = currentNode.parent
                    # 将被删除节点的父节点的右子节点指向被删除节点的右子节点
                    currentNode.parent.rightChild = currentNode.rightChild
                else:  # 若被删除节点无父节点，则被删除节点为根节点
                    # 替换被删除节点的右子节点的键、有效载荷、左子节点和右子节点数据
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)


# class MyHashMap(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         # better to be a prime number, less collision
#         self.key_space = 2069
#         self.hashtable = [None] * self.key_space
#
#     def put(self, key, value):
#         """
#         value will always be non-negative.
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         hash_key = key % self.key_space
#         if not self.hashtable[hash_key]:
#             self.hashtable[hash_key] = ListNode(key, value, None, None)
#         else:
#             front = self.hashtable[hash_key]
#             back = front.last
#             while front.key <= back.key:
#                 if key == front.key:
#                     front.val = value
#                     return
#                 elif key < front.key:
#                     if front == self.hashtable[hash_key]:
#                         self.hashtable[hash_key] = ListNode(key, value, front.last, front)
#                         front.last = self.hashtable[hash_key]
#                     else:
#                         front.last.next = ListNode(key, value, front.last, front)
#                         front.last = front.last.next
#                     return
#                 else:
#                     front = front.next
#                 if key == back.key:
#                     back.val = value
#                     return
#                 elif key > back.key:
#                     temp = back.next
#                     back.next = ListNode(key, value, back, temp)
#                     if temp:
#                         temp.last = back.next
#                     else:
#                         self.hashtable[hash_key].last = back.next
#                     return
#                 else:
#                     back = back.last
#             back.next = ListNode(key, value, back, front)
#             front.last = back.next
#
#     def get(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
#         hash_key = key % self.key_space
#         front = self.hashtable[hash_key]
#         if not front:
#             return -1
#         back = front.last
#         while front.key <= back.key:
#             if key == front.key:
#                 return front.val
#             elif key < front.key:
#                 return -1
#             else:
#                 front = front.next
#             if key == back.key:
#                 return back.val
#             elif key > back.key:
#                 return -1
#             else:
#                 back = back.last
#         return -1
#
#     def remove(self, key):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: None
#         """
#
#         hash_key = key % self.key_space
#         front = self.hashtable[hash_key]
#         if not front:
#             return -1
#         back = front.last
#         while front.key <= back.key:
#             if key == front.key:
#                 if front == self.hashtable[hash_key]:
#                     self.hashtable[hash_key] = front.next
#                 else:
#                     front.last.next = front.next
#                 if front.next:
#                     front.next.last = front.last
#                 return
#             elif key < front.key:
#                 return
#             else:
#                 front = front.next
#             if key == back.key:
#                 back.last.next = back.next
#                 if back.next:
#                     back.next.last = back.last
#                 else:
#                     self.hashtable[hash_key].last = back.last
#                 return
#             elif key > back.key:
#                 return
#             else:
#                 back = back.last
#         return
#
#
# class ListNode(object):
#     def __init__(self, key, val, last, next):
#         """
#         :type key: int
#         :type val: int
#         :type last: HashNode
#         :type next: HashNode
#         :rtype: None
#         """
#         self.key = key
#         self.val = val
#         if not last:
#             self.last = self
#         else:
#             self.last = last
#         self.next = next

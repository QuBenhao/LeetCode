import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        operations, nums = test_input
        nums = nums.pop(0)[0]
        operations.pop(0)
        root = TreeNode(nums.pop(0))
        is_left = True
        curr_nodes = []
        curr_node = root
        while nums:
            num = nums.pop(0)
            if is_left:
                is_left = False
                if num:
                    curr_node.left = TreeNode(val=num)
                    curr_nodes.append(curr_node.left)
                else:
                    curr_node.left = None
            else:
                is_left = True
                if num:
                    curr_node.right = TreeNode(val=num)
                    curr_nodes.append(curr_node.right)
                else:
                    curr_node.right = None
                curr_node = curr_nodes.pop(0)
        result = [None]
        obj = BSTIterator(root)
        for op in operations:
            if op == "next":
                param = obj.next()
            else:
                param = obj.hasNext()
            result.append(param)
        return result


class BSTIterator(object):
    """
    def __init__(self, root):
        self.root = root
        self.arr = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            self.arr.append(node)
            in_order(node.right)

        in_order(root)
        self.curr = 0

    def next(self):
        val = self.arr[self.curr].val
        self.curr += 1
        return val

    def hasNext(self):
        return self.curr < len(self.arr)
    """

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.in_order(root)

    def in_order(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop(-1)
        if node.right:
            self.in_order(node.right)

        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return bool(self.stack)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target = test_input
        nums = nums.copy()
        num = nums.pop(0)
        root = TreeNode(num)
        if num == target:
            target = root
        copy_root = TreeNode(num)
        is_left = True
        curr_nodes = []
        curr_node = root
        copy_nodes = []
        copy_node = copy_root
        while nums:
            num = nums.pop(0)
            if is_left:
                is_left = False
                if num:
                    curr_node.left = TreeNode(val=num)
                    if num == target:
                        target = curr_node.left
                    curr_nodes.append(curr_node.left)
                    copy_node.left = TreeNode(val=num)
                    copy_nodes.append(copy_node.left)
                else:
                    curr_node.left = None
                    copy_node.left = None
            else:
                is_left = True
                if num:
                    curr_node.right = TreeNode(val=num)
                    if num == target:
                        target = curr_node.right
                    curr_nodes.append(curr_node.right)
                    copy_node.right = TreeNode(val=num)
                    copy_nodes.append(copy_node.right)
                else:
                    curr_node.right = None
                    copy_node.right = None
                curr_node = curr_nodes.pop(0)
                copy_node = copy_nodes.pop(0)
        return self.getTargetCopy(root, copy_root, target).val

    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        nodes = [original]
        nodes_ = [cloned]
        while nodes:
            next_nodes = []
            next_nodes_ = []
            for i in range(len(nodes)):
                if nodes[i] == target:
                    return nodes_[i]
                if nodes[i].left:
                    next_nodes.append(nodes[i].left)
                    next_nodes_.append(nodes_[i].left)
                if nodes[i].right:
                    next_nodes.append(nodes[i].right)
                    next_nodes_.append(nodes_[i].right)
            nodes = next_nodes
            nodes_ = next_nodes_
        return None


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

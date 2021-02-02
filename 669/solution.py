import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, low, high = test_input
        nums = nums.copy()
        if not nums:
            root = None
        else:
            root = TreeNode(nums.pop(0))
        is_left = True
        curr_nodes = []
        curr_node = root
        while nums:
            num = nums.pop(0)
            if is_left:
                is_left = False
                if num is not None:
                    curr_node.left = TreeNode(val=num)
                    curr_nodes.append(curr_node.left)
                else:
                    curr_node.left = None
            else:
                is_left = True
                if num is not None:
                    curr_node.right = TreeNode(val=num)
                    curr_nodes.append(curr_node.right)
                else:
                    curr_node.right = None
                curr_node = curr_nodes.pop(0)
        root = self.trimBST(root, low, high)
        ans = []
        l = [root]
        while l:
            node = l.pop(0)
            if node:
                ans.append(node.val)
            else:
                ans.append(None)
            if node and node.left:
                l.append(node.left)
            elif node:
                l.append(None)
            if node and node.right:
                l.append(node.right)
            elif node:
                l.append(None)
            if all(v is None for v in l):
                break
        return ans

    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root:
            return
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        elif root.val > high:
            root = self.trimBST(root.left, low, high)
        else:
            root = self.trimBST(root.right, low, high)
        return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

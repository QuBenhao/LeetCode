import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums1, nums2 = test_input
        root1 = TreeNode(nums1.pop(0))
        root2 = TreeNode(nums2.pop(0))
        is_left = True
        curr_nodes = []
        curr_node = root1
        while nums1:
            num = nums1.pop(0)
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
        is_left = True
        curr_nodes = []
        curr_node = root2
        while nums2:
            num = nums2.pop(0)
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
        return self.leafSimilar(root1, root2)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
                return
            yield from dfs(root.left)
            yield from dfs(root.right)

        return list(dfs(root1)) == list(dfs(root2))


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

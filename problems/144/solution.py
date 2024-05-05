import solution
from python.object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        return self.preorderTraversal(root)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(node):
            if not node:
                return
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)

        ans = []
        preorder(root)
        return ans

        # curr = root
        # ans = []
        # delay = []
        # while curr:
        #     ans.append(curr.val)
        #     if curr.right:
        #         delay.append(curr.right)
        #     temp = curr.left
        #     while temp:
        #         ans.append(temp.val)
        #         if temp.right:
        #             delay.append(temp.right)
        #         temp = temp.left
        #     if delay:
        #         curr = delay.pop()
        #     else:
        #         break
        # return ans


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

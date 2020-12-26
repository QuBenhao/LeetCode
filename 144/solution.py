import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input.copy()
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

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, targetVal, k = test_input
        target = None
        nums = list(nums)
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
                    if num == targetVal:
                        target = curr_node.left
                    curr_nodes.append(curr_node.left)
                else:
                    curr_node.left = None
            else:
                is_left = True
                if num:
                    curr_node.right = TreeNode(val=num)
                    if num == targetVal:
                        target = curr_node.right
                    curr_nodes.append(curr_node.right)
                else:
                    curr_node.right = None
                curr_node = curr_nodes.pop(0)
        return self.distanceK(root, target, k)

    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not k:
            return [target.val]
        elif k > 501:
            return []

        def dfs1(node, path):
            if node == target:
                return path + [node]
            if not node:
                return []
            left = dfs1(node.left, path + [node])
            if left:
                return left
            return dfs1(node.right, path + [node])

        dists = dfs1(root, [])
        parents_distance = dict()
        n = len(dists) - 1
        for i, node in enumerate(dists):
            parents_distance[node] = n - i

        ans = []

        def dfs2(node, dis):
            if not node:
                return
            if node in parents_distance:
                dis = k - parents_distance[node]
            if dis < 0 and not (
                    (node.left and node.left in parents_distance) or (node.right and node.right in parents_distance)):
                return
            if not dis:
                ans.append(node.val)
            dfs2(node.left, dis - 1)
            dfs2(node.right, dis - 1)

        dfs2(root, k)
        return ans


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

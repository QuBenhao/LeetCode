import solution
from collections import defaultdict
from python.object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        return self.verticalTraversal(root)

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        hashmap = defaultdict(list)

        def dfs(node, x, y):
            if not node:
                return
            hashmap[y].append((x, node.val))
            dfs(node.left, x + 1, y - 1)
            dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)
        return [list(list(zip(*sorted(hashmap[i])))[1]) for i in sorted(hashmap.keys())]

        # vertical_dict = defaultdict(list)
        # curr_nodes = [(0, root)]
        # while curr_nodes:
        #     next_nodes = []
        #     for v, node in curr_nodes:
        #         vertical_dict[v].append(node.val)
        #         if node.left:
        #             next_nodes.append((v-1, node.left))
        #         if node.right:
        #             next_nodes.append((v+1, node.right))
        #     next_nodes.sort(key=lambda x:(x[0],x[1].val))
        #     curr_nodes = next_nodes
        # ans = []
        # for k in sorted(vertical_dict.keys()):
        #     ans.append(vertical_dict[k])
        # return ans


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

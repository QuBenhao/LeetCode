import solution
from collections import deque, defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        trees = []
        for lt in test_input:
            root = TreeNode(lt[0])
            for i in range(1, len(lt)):
                if lt[i] < lt[0]:
                    root.left = TreeNode(lt[i])
                else:
                    root.right = TreeNode(lt[i])
            trees.append(root)
        root = self.canMerge(trees)
        ans = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                ans.append(None)
                continue
            ans.append(node.val)
            q.append(node.left)
            q.append(node.right)
        while ans and ans[-1] is None:
            ans.pop()
        return ans

    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """
        nodes = {}
        indeg = defaultdict(int)
        for t in trees:
            if t.val not in indeg:
                indeg[t.val] = 0
            if t.left:
                indeg[t.left.val] += 1
                if t.left.val not in nodes: nodes[t.left.val] = t.left
            if t.right:
                indeg[t.right.val] += 1
                if t.right.val not in nodes: nodes[t.right.val] = t.right
            nodes[t.val] = t

        # check single root
        sources = [k for k, v in indeg.items() if v == 0]
        if len(sources) != 1: return None

        self.cur = float('-inf')
        self.is_invalid = False
        seen = set()

        def inorder(val):
            # check cycle
            if val in seen:
                self.is_invalid = True
                return
            seen.add(val)
            node = nodes[val]
            if node.left: node.left = inorder(node.left.val)
            # check inorder increasing
            if val <= self.cur:
                self.is_invalid = True
                return
            self.cur = val
            if node.right: node.right = inorder(node.right.val)
            return node

        root = inorder(sources[0])
        # check full traversal
        if len(seen) != len(nodes) or self.is_invalid:
            return None
        return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

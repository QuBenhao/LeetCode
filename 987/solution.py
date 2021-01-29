import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input.copy()
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
        return self.verticalTraversal(root)

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        import collections
        vertical_dict = collections.defaultdict(list)
        curr_nodes = [(0, root)]
        while curr_nodes:
            next_nodes = []
            for v, node in curr_nodes:
                vertical_dict[v].append(node.val)
                if node.left:
                    next_nodes.append((v-1, node.left))
                if node.right:
                    next_nodes.append((v+1, node.right))
            next_nodes.sort(key=lambda x:(x[0],x[1].val))
            curr_nodes = next_nodes
        ans = []
        for k in sorted(vertical_dict.keys()):
            ans.append(vertical_dict[k])
        return ans

        # import collections
        # vertical_dict = collections.defaultdict(list)
        # curr_nodes = collections.deque([(0,0,root)])
        # while curr_nodes:
        #     v,l,node = curr_nodes.popleft()
        #     vertical_dict[v].append((l,node.val))
        #     if node.left:
        #         curr_nodes.append((v-1,l-1,node.left))
        #     if node.right:
        #         curr_nodes.append((v+1,l-1,node.right))
        # ans = []
        # for k in sorted(vertical_dict.keys()):
        #     ans.append([x[1] for x in sorted(vertical_dict[k],key=lambda x:(-x[0],x[1]))])
        # return ans


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

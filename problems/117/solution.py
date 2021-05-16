import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input.copy()
        root = Node(nums.pop(0))
        is_left = True
        curr_nodes = []
        curr_node = root
        while nums:
            num = nums.pop(0)
            if is_left:
                is_left = False
                if num:
                    curr_node.left = Node(val=num)
                    curr_nodes.append(curr_node.left)
                else:
                    curr_node.left = None
            else:
                is_left = True
                if num:
                    curr_node.right = Node(val=num)
                    curr_nodes.append(curr_node.right)
                else:
                    curr_node.right = None
                curr_node = curr_nodes.pop(0)
        node = self.connect(root)
        ans = []
        while node:
            curr = node
            while curr:
                ans.append(curr.val)
                curr = curr.next
            ans.append(None)
            node = node.left
        return ans

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        root.next = None
        nodes = []
        if root.left:
            nodes.append(root.left)
        if root.right:
            nodes.append(root.right)
        while nodes:
            new_nodes = []
            for i in range(len(nodes)):
                if nodes[i].left:
                    new_nodes.append(nodes[i].left)
                if nodes[i].right:
                    new_nodes.append(nodes[i].right)
                if i < len(nodes) - 1:
                    nodes[i].next = nodes[i + 1]
            nodes[-1].next = None
            nodes = new_nodes
        return root


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

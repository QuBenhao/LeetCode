import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        NodeList = []
        head = Node(0)
        last = head
        for val, random_index in test_input:
            last.next = Node(val, random=random_index)
            last = last.next
            NodeList.append(last)
        for node in NodeList:
            if node.random is not None:
                node.random = NodeList[node.random]
        head = self.copyRandomList(head.next)
        index_dict = dict()
        pointer = head
        i = 0
        while pointer:
            index_dict[pointer] = i
            pointer = pointer.next
            i += 1
        pointer = head
        ans = []
        while pointer:
            if pointer.random is not None:
                ans.append([pointer.val, index_dict[pointer.random]])
            else:
                ans.append([pointer.val, None])
            pointer = pointer.next
        return ans

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        copy_head = Node(0)
        last = copy_head
        pointer = head
        random_dict = dict()
        while pointer:
            last.next = Node(pointer.val, random=pointer.random)
            random_dict[pointer] = last.next
            last = last.next
            pointer = pointer.next
        pointer = copy_head.next
        while pointer:
            if pointer.random is not None:
                pointer.random = random_dict[pointer.random]
            pointer = pointer.next
        return copy_head.next


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

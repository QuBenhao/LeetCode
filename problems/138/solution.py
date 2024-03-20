import solution
from object_libs import list_to_linked_random_list, linked_random_list_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head = list_to_linked_random_list(test_input)
        root = self.copyRandomList(head)
        return linked_random_list_to_list(root)

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # 复制所有节点，插入原节点的后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next, None)
            cur = cur.next.next

        # 连接所有复制的节点的random指针
        cur = head
        copyHead = head.next
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 断开原链表与复制链表之间的连接
        cur = head
        cur_ = copyHead
        while cur and cur_:
            cur.next = cur_.next
            cur = cur.next
            if cur:
                cur_.next = cur.next
            cur_ = cur_.next
        return copyHead


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

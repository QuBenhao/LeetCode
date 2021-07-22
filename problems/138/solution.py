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

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head_list = []
        for l in test_input:
            l = list(l)
            if l:
                head = ListNode(l.pop(0))
            else:
                head = None
            head_list.append(head)
            for num in l:
                head.next = ListNode(num)
                head = head.next
        head = self.mergeKLists(head_list)
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        head = ListNode(0)
        curr = []
        for node in lists:
            if node:
                curr.append(node)
        if not curr:
            return None
        curr.sort(key=lambda x: -x.val)
        c = head
        while curr:
            node = curr.pop()
            c.next = node
            c = c.next
            node = node.next
            if node:
                curr.append(node)
                curr.sort(key=lambda x: -x.val)
        return head.next

        # # Python 3.9
        # from heapq import heappush, heappop
        # head = ListNode(0)
        # curr = []
        # for node in lists:
        #     if node:
        #         heappush(curr, (node.val, node))
        # if not curr:
        #     return None
        # c = head
        # while curr:
        #     _, node = heappop(curr)
        #     c.next = node
        #     c = c.next
        #     node = node.next
        #     if node:
        #         heappush(curr, (node.val, node))
        # return head.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

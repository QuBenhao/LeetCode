import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        intersectVal, listA, listB, skipA, skipB = test_input
        intersection_node = None
        headA = headB = None
        if listA:
            node = headA = ListNode(listA[0])
            count = 0
            for i in range(1, len(listA)):
                if count == skipA:
                    intersection_node = node
                node.next = ListNode(listA[i])
                node = node.next
                count += 1
        if listB:
            node = headB = ListNode(listB[0])
            if not skipB:
                headB = intersection_node
            else:
                count = 0
                for i in range(1, len(listB)):
                    if count == skipB - 1:
                        node.next = intersection_node
                        break
                    node.next = ListNode(listB[i])
                    node = node.next
                    count += 1
        res = self.getIntersectionNode(headA, headB)
        if res:
            return res.val

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        n1, n2 = headA, headB
        while n1 != n2:
            n1 = n1.next if n1 else headB
            n2 = n2.next if n2 else headA
        return n1


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

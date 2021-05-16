import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        l1, l2 = test_input

        nums1 = l1.copy()
        nums2 = l2.copy()
        if nums1:
            head1 = ListNode(nums1.pop(0))
        else:
            head1 = None
        if nums2:
            head2 = ListNode(nums2.pop(0))
        else:
            head2 = None
        curr = head1
        for num in nums1:
            curr.next = ListNode(num)
            curr = curr.next
        curr = head2
        for num in nums2:
            curr.next = ListNode(num)
            curr = curr.next
        head = self.mergeTwoLists(head1, head2)
        curr = head
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

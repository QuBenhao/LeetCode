import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums1, a, b, nums2 = test_input
        list1, list2 = ListNode(nums1[0]), ListNode(nums2[0])
        node1 = list1
        node2 = list2
        for i in range(1, len(nums1)):
            node1.next = ListNode(nums1[i])
            node1 = node1.next
        for i in range(1, len(nums2)):
            node2.next = ListNode(nums2[i])
            node2 = node2.next
        ans = []
        root = self.mergeInBetween(list1, a, b, list2)
        while root:
            ans.append(root.val)
            root = root.next
        return ans

    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        if a == list1.val:
            root = list2
        else:
            root = list1
        l1 = list1
        node = list2
        count = 1
        while count < a:
            l1 = l1.next
            count += 1
        r1 = l1
        while count <= b:
            r1 = r1.next
            count += 1
        r1 = r1.next
        while node.next is not None:
            node = node.next
        l1.next = list2
        node.next = r1
        return root


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

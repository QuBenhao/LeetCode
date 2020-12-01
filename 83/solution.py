import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        last = None
        for i in range(len(test_input)-1,-1,-1):
            last = ListNode(test_input[i], next = last)
        return self.deleteDuplicates(head=last)

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = []
        curr = head
        while curr:
            node = curr.next
            while node and node.val == curr.val:
                curr.next = node.next
                node = node.next
            nums.append(curr.val)
            curr = curr.next
        return nums
        # return head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

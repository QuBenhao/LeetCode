import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input.copy()
        if nums:
            head = ListNode(nums.pop(0))
            last = head
            for num in nums:
                last.next = ListNode(num)
                last = last.next
        else:
            head = None
        head = self.swapPairs(head)
        curr = head
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        back = ListNode()
        back.next = head
        front = head.next
        head = back
        while front:
            back.next.next = front.next
            front.next = back.next
            back.next = front
            back = front.next
            front = back.next
            if not front:
                break
            front = front.next
        return head.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

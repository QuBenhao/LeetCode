import solution
from typing import *
from python.object_libs import list_to_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        head0 = list_to_linked_list(nums0)
        return self.pairSum(head0)

    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. 快慢指针找中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 反转后半段链表
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # prev 是反转后的后半段头部

        # 3. 同时遍历前半段和反转后的后半段，计算最大 twin sum
        max_sum = 0
        first, second = head, prev
        while second:
            cur_sum = first.val + second.val
            if cur_sum > max_sum:
                max_sum = cur_sum
            first = first.next
            second = second.next

        return max_sum


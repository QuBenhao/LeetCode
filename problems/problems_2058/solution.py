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
        return self.nodesBetweenCriticalPoints(head0)

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Three-pointer sliding window: first/prev store the first and previous critical-point indices (starting at 1)
        # The minimum distance is between adjacent critical points; the maximum is between the first and last
        first = prev = 0
        mn = 10 ** 9
        a, b, c = head, head.next, head.next.next
        i = 2
        while c:
            if (b.val - a.val) * (b.val - c.val) > 0:  # Same sign => a local maximum or minimum
                if prev:
                    mn = min(mn, i - prev)
                else:
                    first = i
                prev = i
            a, b, c = b, c, c.next
            i += 1
        return [mn, prev - first] if mn < 10 ** 9 else [-1, -1]


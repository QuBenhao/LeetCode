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
        # 三指针滑窗：first/prev 记录第一个和上一个临界点的下标（下标从 1 起）
        # 最小距离必来自相邻两个临界点，最大距离必来自首尾两个临界点
        first = prev = 0
        mn = 10 ** 9
        a, b, c = head, head.next, head.next.next
        i = 2
        while c:
            if (b.val - a.val) * (b.val - c.val) > 0:  # 同号 => 极大值或极小值
                if prev:
                    mn = min(mn, i - prev)
                else:
                    first = i
                prev = i
            a, b, c = b, c, c.next
            i += 1
        return [mn, prev - first] if mn < 10 ** 9 else [-1, -1]


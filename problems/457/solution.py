import solution
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.circularArrayLoop(list(test_input))

    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n = len(nums)
        # change = True
        # while change:
        #     change = False
        #     for i, num in enumerate(nums):
        #         if not num:
        #             continue
        #         # Python里负数取模为正
        #         nxt = (i + num) % n
        #         # 指向自己、指向正负相反的地方、指向0,均构不成循环
        #         if nxt == i or nums[nxt] * num <= 0:
        #             change = True
        #             nums[i] = 0
        # return any(num for num in nums)

        n = len(nums)
        connect = defaultdict(list)
        marks = deque([])
        for i, num in enumerate(nums):
            nxt = (i + num) % n
            connect[nxt].append(i)
            if nxt == i or nums[nxt] * num < 0:
                marks.append(i)
                nums[i] = 0
        while marks:
            i = marks.popleft()
            for nxt in connect[i]:
                if nums[nxt]:
                    nums[nxt] = 0
                    marks.append(nxt)
        return any(num for num in nums)

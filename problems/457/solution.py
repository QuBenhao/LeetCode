import solution
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.circularArrayLoop(list(test_input))

    mark = 1001
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            if nums[i] >= self.mark:
                continue
            cur, tag, last = i, self.mark + i, -1
            flag = nums[cur] > 0
            while True:
                nxt = (cur + nums[cur]) % n
                last = nums[cur]
                nums[cur] = tag
                cur = nxt
                if cur == i:
                    break
                if nums[cur] >= self.mark:
                    break
                if flag and nums[cur] < 0:
                    break
                if not flag and nums[cur] > 0:
                    break
            if last % n != 0 and nums[cur] == tag:
                return True
        return False

        # n = len(nums)
        # connect = defaultdict(list)
        # marks = deque([])
        # for i, num in enumerate(nums):
        #     nxt = (i + num) % n
        #     connect[nxt].append(i)
        #     if nxt == i or nums[nxt] * num < 0:
        #         marks.append(i)
        #         nums[i] = 0
        # while marks:
        #     i = marks.popleft()
        #     for nxt in connect[i]:
        #         if nums[nxt]:
        #             nums[nxt] = 0
        #             marks.append(nxt)
        # return any(num for num in nums)

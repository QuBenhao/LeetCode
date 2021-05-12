import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.magicTower(list(test_input))

    def magicTower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = remain = cur = 0
        q = []
        for num in nums:
            cur += num
            if num < 0:
                heapq.heappush(q, num)
                if cur < 0:
                    ans += 1
                    m = heapq.heappop(q)
                    remain += m
                    cur -= m
        if cur + remain < 0:
            return -1
        return ans

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findXSum(*test_input)

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        counter = Counter()
        length = 0
        for i, num in enumerate(nums):
            counter[num] += 1
            length += 1
            if length == k:
                most_common = sorted(counter.items(), key=lambda item: (-item[1], -item[0]))
                top_x = [item[0] for item in most_common]
                tmp = 0
                for j in range(min(len(top_x), x)):
                    tmp += top_x[j] * counter[top_x[j]]
                ans.append(tmp)
                counter[nums[i - k + 1]] -= 1
                length -= 1
        return ans

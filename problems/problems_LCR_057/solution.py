import math

from sortedcontainers import SortedList

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.containsNearbyAlmostDuplicate(*test_input)

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # st = SortedList()
        # for i, num in enumerate(nums):
        #     if i > k:
        #         st.remove(nums[i - k - 1])
        #     if st:
        #         idx = st.bisect_left(num)
        #         if idx < len(st) and abs(st[idx] - num) <= t:
        #             return True
        #         if idx > 0 and abs(st[idx-1] - num) <= t:
        #             return True
        #     st.add(num)
        # return False

        # 桶排序
        bucket_map = {}
        size = t + 1
        for i, num in enumerate(nums):
            bucket = math.floor(num / size)
            if bucket in bucket_map:
                return True
            if bucket - 1 in bucket_map and abs(num - bucket_map[bucket - 1]) <= t:
                return True
            if bucket + 1 in bucket_map and abs(num - bucket_map[bucket + 1]) <= t:
                return True
            bucket_map[bucket] = num
            if i >= k:
                bucket_map.pop(math.floor(nums[i-k]/size))
        return False

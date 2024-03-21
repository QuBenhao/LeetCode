import solution
from sortedcontainers import SortedList
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.containsNearbyAlmostDuplicate(*test_input)

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # O(N)
        if t < 0 or k < 0:
            return False
        all_buckets = {}
        bucket_size = t + 1  # 桶的大小设成t+1更加方便
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size  # 放入哪个桶

            if bucket_num in all_buckets:  # 桶中已经有元素了
                return True

            all_buckets[bucket_num] = nums[i]  # 把nums[i]放入桶中

            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t:  # 检查前一个桶
                return True

            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t:  # 检查后一个桶
                return True

            # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
            if i >= k:
                all_buckets.pop(nums[i - k] // bucket_size)

        return False

        # # O(N logk)
        # window = SortedList()
        # for i in range(len(nums)):
        #     # len(window) == k
        #     if i > k:
        #         window.remove(nums[i - 1 - k])
        #     window.add(nums[i])
        #     idx = bisect.bisect_left(window, nums[i])
        #     if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
        #         return True
        #     if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= t:
        #         return True
        # return False

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
        bucket_size = t + 1  # A bucket size of t+1 is more convenient
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size  # Determine which bucket to use

            if bucket_num in all_buckets:  # The bucket already contains an element
                return True

            all_buckets[bucket_num] = nums[i]  # Put nums[i] into its bucket

            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t:  # Check the previous bucket
                return True

            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t:  # Check the next bucket
                return True

            # If no match is found, delete the old bucket when i >= k so that stored indices differ from the next index i+1 by at most k
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
